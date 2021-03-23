# Credit card validator
A credit (or debit) card, of course, is a plastic card with which you can pay for goods and services. Printed on that card is a number that’s also stored in a database somewhere, so that when your card is used to buy something, the creditor knows whom to bill. There are a lot of people with credit cards in this world, so those numbers are pretty long: American Express uses 15-digit numbers, MasterCard uses 16-digit numbers, and Visa uses 13- and 16-digit numbers. And those are decimal numbers (0 through 9), not binary, which means, for instance, that American Express could print as many as 10^15 = 1,000,000,000,000,000 unique cards! 

Actually, that’s a bit of an exaggeration, because credit card numbers actually have some structure to them. All American Express numbers start with 34 or 37; most MasterCard numbers start with 51, 52, 53, 54, or 55 (they also have some other potential starting numbers which we won’t concern ourselves with for this problem); and all Visa numbers start with 4. But credit card numbers also have a “checksum” built into them, a mathematical relationship between at least one number and others. That checksum enables computers (or humans who like math) to detect typos (e.g., transpositions), if not fraudulent numbers, without having to query a database, which can be slow.

According to Luhn’s algorithm, you can determine if a credit card number is (syntactically) valid as follows:

1.Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.

2.Add the sum to the sum of the digits that weren’t multiplied by 2.

3.If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!

The python program credit.py gets input from the user and classifies the given card number as 'AMEX' or "MASTERCARD" or "VISA" or "INVALID" using Luhn's algorithm.
