"""
Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange). For
example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key. The advantage
with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and without
both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified
method is to use a password as a key. If the password is shorter than the
message, which is likely, the key is repeated cyclically throughout the
message. The balance for this method is using a sufficiently long password key
for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower
case characters. Using resources/0059_cipher.txt, a file containing the
encrypted ASCII codes, and the knowledge that the plain text must contain
common English words, decrypt the message and find the sum of the ASCII values
in the original text.

link: https://projecteuler.net/problem=59

Solution:

We can see that the cipher contains the same 3-letter combinations a couple
of times. We can assume that these are the most common letter combinations in
the message. With this insight, we can reduce the search space by not checking
the same triplets again.

By XORing potential key parts values with segments of the cipher and ensuring
the resulting ASCII values are between 32 and 126, we can filter out keys that
produce non-printable or non-standard characters, which are unlikely to be
part of a meaningful decrypted text. This method significantly narrows down
the pool of potential keys, making the decryption process more efficient by
focusing only on those key values that have a high likelihood of producing
valid plaintext, thereby streamlining the search for the correct encryption
key.

Additionally, we know that the message is in English, so the most common
triplets are most likely the most frequent three-letter combinations in
English. Therefore, if we find that one of the triplets matches one of the
most common three-letter combinations in English, we can assume that we have
found the correct key.

To verify that we have found the correct key, we can check if the decrypted
message is in English. For this, we can count the number of words in the
message that contain only letters and compare it with the total number of
words in the message. If the ratio is greater than some threshold, we can
assume that the message is indeed in English.
"""
import re

from itertools import product, cycle
from collections import Counter
from string import ascii_lowercase

COMMON_3_LETTER_COMBINATIONS = {'the', 'and', 'tha', 'ent', 'ing', 'ion'}
CONFIDENCE_THRESHOLD = 0.8


def is_english(message: str) -> bool:
    words = message.split()
    exact_words_count = sum(bool(re.fullmatch(r'^\w+$', w)) for w in words)
    return exact_words_count / len(words) > CONFIDENCE_THRESHOLD


def solution(file_path: str) -> int:
    with open(file_path, 'r') as f:
        cipher = tuple(map(int, f.read().split(',')))

    triples = (cipher[i:i+3] for i in range(0, len(cipher) - 3, 3))
    common = [common for common, _ in Counter(triples).most_common()]

    key_parts = [[], [], []]
    for k in map(ord, ascii_lowercase):
        for i in range(3):
            if all(31 < c[i] ^ k < 127 for c in common):
                key_parts[i].append(k)

    for key in product(*key_parts):
        for triples in common:
            message = ''.join(chr(k ^ c) for k, c in zip(key, triples))
            if message not in COMMON_3_LETTER_COMBINATIONS:
                continue

            decrypted = ''.join(chr(k ^ c) for k, c in zip(cycle(key), cipher))
            if is_english(decrypted):
                return sum(map(ord, decrypted))


# test
if __name__ == '__main__':
    print(solution('resources/0059_cipher.txt'))  # 129448
