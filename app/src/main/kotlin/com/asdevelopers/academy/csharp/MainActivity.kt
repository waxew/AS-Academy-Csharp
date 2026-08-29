package com.asdevelopers.academy.csharp

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import com.asdevelopers.academy.core.ui.AcademyCourseApp

/**
 * Activity اختصاصی دوره C#.
 * تمام Navigation، Progress، Search، Bookmark و Lesson rendering از AS-Academy-Core می‌آید.
 */
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            // C# runner فعلاً غیرفعال است تا اجرای جعلی یا ناامن کد به کاربر نمایش داده نشود.
            AcademyCourseApp(courseId = "csharp", codeRunner = null)
        }
    }
}
