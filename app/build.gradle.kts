plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.compose.compiler)
}

android {
    namespace = "com.asdevelopers.academy.csharp"
    compileSdk = 37

    defaultConfig {
        applicationId = "com.asdevelopers.academy.csharp"
        minSdk = 23
        targetSdk = 37
        versionCode = 21000
        versionName = "2.1.0"
    }

    val releaseStoreFile = providers.environmentVariable("ANDROID_SIGNING_STORE_FILE").orNull
    val releaseStorePassword = providers.environmentVariable("ANDROID_SIGNING_STORE_PASSWORD").orNull
    val releaseKeyAlias = providers.environmentVariable("ANDROID_SIGNING_KEY_ALIAS").orNull
    val releaseKeyPassword = providers.environmentVariable("ANDROID_SIGNING_KEY_PASSWORD").orNull
    val hasReleaseSigning = !releaseStoreFile.isNullOrBlank() &&
        !releaseStorePassword.isNullOrBlank() &&
        !releaseKeyAlias.isNullOrBlank() &&
        !releaseKeyPassword.isNullOrBlank()

    signingConfigs {
        if (hasReleaseSigning) {
            create("release") {
                storeFile = file(requireNotNull(releaseStoreFile))
                storePassword = releaseStorePassword
                keyAlias = releaseKeyAlias
                keyPassword = releaseKeyPassword
                enableV1Signing = true
                enableV2Signing = true
                enableV3Signing = true
                enableV4Signing = true
            }
        }
    }

    buildTypes {
        getByName("release") {
            isMinifyEnabled = false
            if (hasReleaseSigning) {
                signingConfig = signingConfigs.getByName("release")
            }
        }
    }

    buildFeatures { compose = true }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

    sourceSets.named("main") {
        assets.srcDir(layout.buildDirectory.dir("generated/courseAssets"))
    }
}

val syncCourseAssets by tasks.registering(Copy::class) {
    from(rootProject.layout.projectDirectory.dir("course"))
    into(layout.buildDirectory.dir("generated/courseAssets/course/csharp"))
}

tasks.named("preBuild").configure { dependsOn(syncCourseAssets) }

dependencies {
    implementation(project(":core"))
    implementation(project(":course"))
    implementation(libs.androidx.core.ktx)
    implementation(libs.androidx.activity.compose)
    implementation(libs.androidx.lifecycle.runtime)
    implementation(platform(libs.compose.bom))
    implementation(libs.compose.ui)
    implementation(libs.compose.material3)
}
