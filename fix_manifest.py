import re

file_path = 'patches/src/main/kotlin/app/morphe/patches/shared/layout/branding/BaseCustomBrandingPatch.kt'
with open(file_path, 'r') as f:
    content = f.read()

# Instead of relying on activity aliases for root, we just hardcode the application tag.
content = content.replace('application.setAttribute(\n                    "android:icon",\n                    "@mipmap/morphe_launcher_black"\n                )', 
'''application.setAttribute(
                    "android:icon",
                    "@mipmap/morphe_launcher_black"
                )
                application.setAttribute(
                    "android:roundIcon",
                    "@mipmap/morphe_launcher_black"
                )
                
                // Also overwrite the original activity's icon and label directly!
                val originalActivity = application.childNodes.toList()
                    .filterIsInstance<org.w3c.dom.Element>()
                    .firstOrNull {
                        it.tagName == "activity" && it.getAttribute("android:name") == activityAliasNameWithIntents
                    }
                if (originalActivity != null) {
                    originalActivity.setAttribute("android:icon", "@mipmap/morphe_launcher_black")
                    originalActivity.setAttribute("android:roundIcon", "@mipmap/morphe_launcher_black")
                    originalActivity.setAttribute("android:label", "YTritik")
                }''')

with open(file_path, 'w') as f:
    f.write(content)

