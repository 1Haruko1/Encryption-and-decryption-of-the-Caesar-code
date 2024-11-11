## Шифрование и дешифрование кодом Цезаря

Этот код представляет собой консольное приложение, позволяющее шифровать и дешифровать текст с помощью шифра Цезаря для русского и английского алфавитов.

### Как использовать:

1. Запустите код: Запустите файл Python с кодом.
2. Ввод данных: В консоли введите текст, сдвиг и режим шифрования/дешифрования, разделяя их символом "/".
    * Текст: Любая строка символов.
    * Сдвиг: Целое число от 1 до 25, определяющее смещение букв в алфавите.
    * Режим: "encode" для шифрования, "decode" для дешифрования.
    * Пример: `Привет, мир!/3/encode`
3. Вывод: Программа выведет зашифрованный/расшифрованный текст в консоль.
4. Завершение работы: Чтобы завершить работу программы, введите "end" в консоли.


### Код создан на основе IDeF0 диаграммы

[ссылка на схему](https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=%D0%94%D0%B8%D0%B0%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B0%20%D0%B1%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F.drawio#R%3Cmxfile%3E%3Cdiagram%20name%3D%22%D0%A1%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0%20%E2%80%94%201%22%20id%3D%22i6U5Zhl4WnuqZG08Giuk%22%3E7V1Zc%2BO4Ef41qkoerCJ4gXzUuXnYTW1ltirJU4q2aIkZWXQoemzvrw8vgI2LN2kdMw8aCQZBCt399YnWzFi9fPwSea%2BH38Kdf5zp2u5jZqxnuq7bmpX8l4585iPINIx8ZB8Fu2KsHPgW%2FOkXg1ox%2Bhbs%2FDMzMQ7DYxy8soNP4enkP8XMmBdF4Ts77Tk8snd99fa%2BMPDtyTuKo%2F8MdvEhH3V0XI7%2FzQ%2F2B3JnZLv5X148Mrn4JueDtwvfwZCxmRmrKAzj%2FN3Lx8o%2FprtH9iW%2Fbqv4K32wyD%2FFTS5Y%2FcP94z9%2FHHC0W5%2BOzvf35d8fzAdUUOMcf5Jv7O%2BSDSg%2BhlF8CPfhyTtuytFlFL6ddn66rJZ8Kuf8GoavySBKBv%2Frx%2FFnQU3vLQ6ToUP8ciz%2BKj568W3O4Vv05Fc9bz4vfUZwYfGFf%2FHDFz%2BOPpMJkX%2F04uAHS0Sv4IU9nUcv%2FT0MkkfRtYJxDVwQrWBb3dDYJWIv2vtxcVW56ckb8BjlUEaKNmTJ7%2FbDO74VX2GW7PXCSV%2BXySuaOWb2qmUjm%2Bw1m7NcZK9a%2BkjpGzN7tbLJrS7Xsgk6uTz%2FUzKCwLgmMA%2FLGu%2BHIPa%2FvXoZSd8ThGjIBj%2F8KPY%2FKglM%2FupyhNKKz%2B%2BlsCIigQcgqLam5gmGmm1JZ4qkEyTstFuk0JR8ejp653PwxO4Lu4nKXaoVArAHlmQLyFhPWaHbS0igu3MLu%2BU%2Fh10xl3FBdMR1edLWrDuySFpykVQLiG4fk41e7oIfydt9%2Bjad5G6I%2FEBZSl6NbIktuSx5RnilfLGFBu5uE%2BlOXleqZThOTKQsZnnPOwb7U8qYCbf5UTKQymKQ6MNF8YeXYLfLtYB%2FDv70HrOlUj59TXc%2Bo4W1nFnrdK0E%2BM%2B5DkiXPsdR%2BN1fhccwWXd9Ck%2FpKs%2FB8cgNDQALtlWLCvaUoOBImcfNyZeRcmkQKKaw7ACkTQnqvaT4eXo8v6o4ohXGO02XrNUBVRx7pwyIbBa8DGJoAQ50puRAd2i1lOxN9Pmv9MMcW%2BTzv4up2Yf1B5y6%2FrwSfWZoHOl0jiZNFRi%2FkEDcsY1IbQjUkSqxblal00K5dcedO0EYyu4VCIO0KSEGSbyW2zZ9BRo4HaGCX0i3jWmhQpdDxbYQtRwMUuHbApN1lXmJ1MlcFhOgOAPa2%2F97S0Mdy%2BfwFD%2FkMrNIJrivHzkGFH9mIMACeJK%2FrgEorAHybInHCicjgG4YTLYaAFGfJ88M%2BRIhoZW%2BEp5%2Fnc0h31fXGkNlz72FT4WBC7IsaAuh9kZgN92eIijlDoTCvLGAna9GYUkAgncVm5G7EKhW%2Br1P0KnaIanndqeK22%2FYmABc7QzD1UL4E1kiV8v0Kh8mHY6rJeGXwfwXE2HowJQui9yByT797kdB8tVSkl%2BlqULJ18FUmWumVv5zWFbRJnZybLnlohOtypkBNLKtDp0xAXCVOUHWvwqEGAASEGZDajTq%2B3WQgOWUXwD1sm6A%2FWug9LasResA4hsCO6xYfrkGRgCqQjcGYgzEWUCiqpBGuszR%2BEIRbDVZLqA8sgL2%2BoaYR9RkscF7yh1b1o6h0yzAXGgEvpDl01itNgKBHZa%2BliSWbsgybKMJPsm9T5uzLu0FxlaY09hn23Bnfa67iNnmGrRqQ9yGpkZPG8LiRN3mwx0j63q9UrJhfGANtL8l5ZZfvUf%2FOB4%2Bi1SvZGVBGmlBS3GXGawZkUnpQ2KVYZO1xVA%2Fy5FMCZ%2Bfz%2F44xpskK1GGnTbAPzVADIcL%2FuQkbliuQENWdWnY0gjMPdOGRiPHaVOXQ1DQJRJqSay0ScshyM3uJyiMrBqUbOxp8cScGm7lVUiuDiI3m8JaLg0jTnBXwKKCIR9RXmn4%2BBoM6SFklaOuLYmxGJPaVZIkwG2Lqu6ac5uhgtVZWIWlbD7CMra4Gj%2FFdUxx5dDYkqnWaeVVEenHAq1EW4mGOKRWM8xEEUPpQlmm3iUegvZcPRnGIu1l9WTjkV4S9ewH1SAcbjnGrEU9z3WGwxO4dhBLVN4GbgP9CUeU%2F0x2XZS4ZuAf96wjawV8J8ESvWmwxBz8CEG%2FylC1kQ3zF9IqCBjlcFVVVH1LhC8nWIIHC5akGSwbM1L6cPHBEl0RLPmqTNfUsQ0bcUpYlxS8TRrbMO4utmFjwcuxOx7vEJeiBJ1INRoK6N0A0F2Qojdq1i6BNEnt6s6VX3L8RmRdWrabF9LQER1kqHQwviKhy4Y1t38hT0zDrTCRtQBf1Z0xcVFOKxlgm8h8xTp%2FveaymwEgzeKOONmyGl48KaQNHgOCdTasXzHXDFp3c0u%2BhYhsjskhW3OQtOaw1kZnAdOZGDAVESYuHU4xCWIgPFeqVVUMgxpatWUjMVwq7Ju7xhibizNTXoQYgyTSMFqBBimRvXWXlHia9S4pbohfE7mkEh2QxhWRIFswqKw8xoOInA5TgntB%2FigpRxjCHzVYd1Tvp4nG90ZNhfEs6oLawjlVTZXFpCwYI5dWrCOhMCu7pJ7jMiN3xJj21N6xw5VpYReLMD9tI4QxTUnmxGldwfalG4yuac6xy5LPwt0sRtlaLrfWyGaiqTYTqWxDOYRgIfWr5XoFmnoL4HPeu8HnckeSsKRS253S3jPvriWKa3I2Ny%2BBzaWZW4iHhbFFWdH1RCZ7aXOtCFTY6eTNAsi9Dt5DuVedNFdG06gxCm2L5L1Y17ctH6gMQ1mqs2aN%2Bq4UwUEDfD0aJd%2BCu6ht5WJym3uOkYi%2Fa6B0sEJK6yo68GiesSsC4016xsVG13rGxDi9FM9Ybtn89IwVfDxMppa4xhfsDCuOorUNjHI6zgA6TjSYqedcoYy%2B2ClFSGdztq755V6p5AzJT69UWseOHHPOnfp0tY6GrHQxc2JjVl5AsRDLa%2BDB0IpMb4XgNeusRnO7GNwc5k%2FFx8lhxK18BDjtri08xPemdCSFm1ITbzRn2Lq7Jkm56LM1kUjjZb8dkPCr8bA0di9QSWgz1fcW8P1IAUSh1zuDzJr9KIbJHXC7TeZ%2Ft2nruFEsrDUI3Mvvc371Tgw%2Fk34sj97T933Guw9PuainXVuCUxAH3nGm7KQEz%2BdjsENr8GAW8I1rS9mMCt8%2Ff%2FjqFpbido70zamvT%2FvmUKw3AJ1WLI%2FBtAk9lk6n0R1ZgmkLwGPSxIvWcouuQb%2BAo%2FJooHMCCHGx1xLn6ip6%2BMNCw%2Fms4qnUm4wpEI%2BhPqYw%2BGn5fvRRnOKRh1gFoYV9Ttjj0YVoPkZM584OR6urArMbgCXUQEWgH4YGih2hZslVT5t2oOP2q7uc4AkR2GF6AtjkWlLnbvQz6sYPphBBHqDKbC3%2FCM0z3qqgSrA2gg9X1tmrtmBxWPYKFm9d1CvLk9T3xENaVZNKWr9rglsg4TGqS54771V7gW4myq2iXGNYASbirQD81UcV7MHdzjvrn4dM251z7VU0o2NZb74Y78Tiaat57U5ObKWcS3DWBfhCLZNqH7Vn590%2B%2BCJG4zgop%2FXI8KQF8T75nHOTHVNuRYVR1HODKvLxCBwnhElz%2BNsSFunyClUBsffkindDtpKjCmQLUcmsZc9T%2B%2FMpV7Ch0HSBctM%2FpX%2FVv%2FsyfHdmZHA%2Fw%2BFKFLE%2BrSKWpJDHyT9d%2B%2B9wJGaUoHERryOba9w0lexyq%2FH6e2yNK3f1B9O4AvyOpoAbtNretPwKte4dIucwpep2BMxXf0mtZWxWa%2BPoKX%2Bc4MowfKBe5AKGI2RLeuzLQHy0JJ49avuVmwJxS%2Bep1xnCk6Xm%2BldDuKLSZ3oIHwm%2FObveYG6t1hs9Ul9am2cj4e4hPbWhkoE9tn3KXYRer8YeyF%2BB8u2Feg7cS%2BiDrVru3Z0qNBM3UWjTHsmVN0meLEk41xDTG0Cbm26N5msXRaxPHzbtH4Xthgq2r%2BZ0%2BV%2Fs0EnDv4l0naM4%2FNEhrnaxyTbC%2BIMk2xDmWhTp%2FWyoCXJtip5SXCxLk%2FUgE1O8XFaoc8K2Tz5nCIDmyYiQazbzOEYLG2FJsP5n%2FqYNnOK0Kwvm6GpxiNrYF0lXw2gm55KpWjuqG%2F5yxq%2B07W%2FDDlX0crd0aHoJOA2MXJn5N1h6mPZxp4xDhBnCi%2Bw3c0brJ4slAY0aVmpWZNq9aKfH6UwamxNLpBAYuYGUyRDs6Bo8Kkq0nezAeAdll3yMwtQfLXEw0eCH38Jdagtu%2Fg8%3D%3C%2Fdiagram%3E%3C%2Fmxfile%3E)

### Пример работы:

```
ЧТОБЫ ЗАВЕРШИТЬ ПРОГРАММУ, НАПИШИТЕ "end"
ВВЕДИТЕ ТЕКСТ, ОТСТУП И РЕЖИМ (encode/decode) ЧЕРЕЗ СИМВОЛ "/": Привет, мир!/3/encode
Слпвлв, прг!
ВВЕДИТЕ ТЕКСТ, ОТСТУП И РЕЖИМ (encode/decode) ЧЕРЕЗ СИМВОЛ "/": Слпвлв, прг!/3/decode
Привет, мир!
ВВЕДИТЕ ТЕКСТ, ОТСТУП И РЕЖИМ (encode/decode) ЧЕРЕЗ СИМВОЛ "/": end
```


### Функции:

* `ceasar_code(text, shift, mode)`:
    * Принимает текст, сдвиг и режим шифрования/дешифрования.
    * Возвращает зашифрованный/расшифрованный текст.
* `main`: 
    * Выводит приветствие.
    * В бесконечном цикле:
        * Считывает ввод пользователя.
        * Проверяет ввод на корректность.
        * Вызывает функцию `ceasar_code` для шифрования/дешифрования.
        * Выводит результат.
    * Завершает работу при вводе "end".

### Преимущества:

* Поддержка русского и английского алфавитов.
* Простой и интуитивно понятный интерфейс.
* Возможность шифровать и дешифровать текст.

### Ограничения:

* Шифр Цезаря - это простой шифр, который легко взломать.
* Не поддерживает другие символы, кроме букв русского и английского алфавитов.
* Не сохраняет зашифрованный текст в файл.