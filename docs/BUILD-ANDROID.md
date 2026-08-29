# ساخت برنامه Android دوره C#

این ریپو `AS-Academy-Core` را به‌صورت Git submodule مصرف می‌کند و منطق مشترک را کپی نمی‌کند.

```bash
git clone --recurse-submodules https://github.com/waxew/AS-Academy-Csharp.git
cd AS-Academy-Csharp
AS-Academy-Core/gradlew -p . :app:assembleDebug
```

محتوای پوشه `course/` هنگام build به مسیر assets مورد انتظار Core یعنی `course/csharp/` کپی می‌شود؛ بنابراین Course Package تنها یک منبع حقیقت دارد.
