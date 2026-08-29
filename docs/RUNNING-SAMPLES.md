# اجرای نمونه‌ها

پیش‌نیاز: .NET SDK سازگار با TargetFramework نمونه.

```bash
dotnet --info
dotnet run --project samples/01-HelloAcademy/HelloAcademy.csproj
dotnet run --project samples/02-ExpenseTracker/ExpenseTracker.csproj
```

برای بررسی build:

```bash
dotnet build samples/01-HelloAcademy/HelloAcademy.csproj
dotnet build samples/02-ExpenseTracker/ExpenseTracker.csproj
```

نمونه‌ها برای آموزش کوچک و مستقل نگه داشته می‌شوند؛ اپلیکیشن اصلی Academy و engineهای عمومی در `AS-Academy-Core` قرار دارند.
