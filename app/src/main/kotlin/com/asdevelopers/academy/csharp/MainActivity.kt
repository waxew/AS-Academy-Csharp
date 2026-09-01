package com.asdevelopers.academy.csharp

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import com.asdevelopers.academy.course.model.CourseBranding
import com.asdevelopers.academy.mainui.AcademyFolderCourseHost

/**
 * Thin C# Course App entry point.
 *
 * Core owns shared runtime/engines, MainUi owns shared presentation/navigation and MainCourse owns
 * every lesson, exercise, quiz and project. No curriculum text is duplicated in this application.
 */
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            AcademyFolderCourseHost(
                courseId = "csharp",
                title = "آموزش جامع C#",
                branding = CourseBranding(
                    primaryColorHex = "#512BD4",
                    secondaryColorHex = "#6F42C1",
                    accentColorHex = "#9B72CF"
                )
            )
        }
    }
}
