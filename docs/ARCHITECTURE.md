# C# app architecture

از نسخه معماری جدید AS Academy، این ریپو یک Course App نازک است.

## Source of Truth

- Engine / runtime: `AS-Academy-Core`
- Shared presentation: `AS-Academy-MainUi`
- C# educational content: `AS-Academy-MainCourse/courses/csharp/course`
- This repository: Android application ID, release/signing configuration and C#-specific host configuration.

## Content rule

فایل‌های `course/` موجود در این ریپو فقط snapshot میراثی قبل از مهاجرت هستند و نباید برای محتوای جدید ویرایش شوند. Build اپ، Course Package را مستقیماً از submodule `AS-Academy-MainCourse/courses/csharp/course` وارد assets می‌کند.

تمام Lesson/Chapter/Exercise/Quiz/Exam/Project/Capstone/Glossary جدید باید ابتدا در MainCourse ثبت شود.

## MainUi migration

`AS-Academy-MainUi` به‌عنوان dependency معماری پروژه pin شده است. تا پایان تثبیت API اجرایی MainUi، entry point فعلی سازگار با Core حفظ می‌شود تا Release موجود نشکند. پس از سبز شدن MainUi contract/build، `MainActivity` فقط `AcademyMainUi` را launch خواهد کرد و UI قدیمی Core حذف می‌شود.
