pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}

dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
    versionCatalogs {
        create("libs") {
            from(files("AS-Academy-Core/gradle/libs.versions.toml"))
        }
    }
}

rootProject.name = "AS-Academy-Csharp"
include(":app", ":core", ":course", ":main-ui")
project(":core").projectDir = file("AS-Academy-Core/core")
project(":course").projectDir = file("AS-Academy-Core/course")
project(":main-ui").projectDir = file("AS-Academy-MainUi/main-ui")
