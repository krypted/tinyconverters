# tinyconverters

This repository includes a number of microservices that can be used to perform small transmogrifications between file formats, data formats, types, etc. For example, there are scripts that move information to and from json or switch from hex, and stuff like that. There are also a couple of linters and copiers to help validate that the changes completed properly, didn't trash data, and are lintable.

Most of these are written in python. Some are in go, swift, or javascript as well, where anything in go, swift, or javascript should also be available in python. Some are written specifically to be run as a Google Cloud Function or Lambda. In those cases there should either be a prefix or a curl example in the comments.

The LICENSE chosen was meant to be as permissive as possible. No need for any mention or whatever, although it's always kind to hear your name here and there!
