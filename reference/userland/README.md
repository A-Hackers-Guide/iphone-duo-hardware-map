# Userland: iOS 27.2 dyld shared cache

4,776 images. 426 hardware-facing images have full pages (classes, methods, properties, Swift types, strings; their classes also have pages under [`../objc/`](../objc/README.md)); 3,503 others have light pages (libraries and type names); 847 were not generated before the run was stopped (`tools/gen_dsc_all.py` resumes). **[DSC]**

| Image | Version | Page |
|---|---|---|
| [`/usr/lib/libobjc.A.dylib`](usr__lib__libobjc.A.dylib.md) | 973.1.0.0.0 | light |
| [`/usr/lib/libsharedcache.dylib`](usr__lib__libsharedcache.dylib.md) | 0.0.0.0.0 | light |
| [`/usr/lib/system/libdyld.dylib`](usr__lib__system__libdyld.dylib.md) | 27104.0.0.0.0 | light |
| [`/usr/lib/dyld`](usr__lib__dyld.md) | 27104.0.0.0.0 | light |
| [`/usr/lib/system/libsystem_pthread.dylib`](usr__lib__system__libsystem_pthread.dylib.md) | 553.40.2.0.0 | full |
| [`/usr/lib/system/libsystem_malloc.dylib`](usr__lib__system__libsystem_malloc.dylib.md) | 886.40.15.0.0 | light |
| [`/usr/lib/system/libxpc.dylib`](usr__lib__system__libxpc.dylib.md) | 3298.52.1.0.0 | light |
| [`/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`](System__Library__Frameworks__CoreFoundation.framework__CoreFoundation.md) | 5027.1.8.0.0 | light |
| [`/System/Library/Frameworks/Foundation.framework/Foundation`](System__Library__Frameworks__Foundation.framework__Foundation.md) | 5027.1.8.0.0 | light |
| [`/usr/lib/swift/libswift_Concurrency.dylib`](usr__lib__swift__libswift_Concurrency.dylib.md) | 6.4.2.1.9 | light |
| [`/usr/lib/swift/libswiftCore.dylib`](usr__lib__swift__libswiftCore.dylib.md) | 6.4.2.1.9 | light |
| [`/System/Library/Frameworks/Network.framework/Network`](System__Library__Frameworks__Network.framework__Network.md) | 6681.52.6.0.0 | full |
| [`/usr/lib/libquic.dylib`](usr__lib__libquic.dylib.md) | 6681.52.6.0.0 | light |
| [`/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics`](System__Library__Frameworks__CoreGraphics.framework__CoreGraphics.md) | 2050.1.6.0.0 | light |
| [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) | 1223.10.21.0.0 | full |
| [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) | 9127.1.13.13.0 | full |
| [`/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams`](System__Library__PrivateFrameworks__BiomeStreams.framework__BiomeStreams.md) | 259.0.0.0.0 | light |
| [`/System/Library/Frameworks/CoreServices.framework/CoreServices`](System__Library__Frameworks__CoreServices.framework__CoreServices.md) | 1517.1.12.0.0 | light |
| [`/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation`](System__Library__Frameworks__ExtensionFoundation.framework__ExtensionFoundation.md) | 290.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/GenerativeFunctionsFoundation`](System__Library__PrivateFrameworks__GenerativeFunctionsFoundation.framework__GenerativeFunctionsFoundation.md) | 297.12.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels`](System__Library__PrivateFrameworks__GenerativeModels.framework__GenerativeModels.md) | 297.12.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari`](System__Library__PrivateFrameworks__MobileSafari.framework__MobileSafari.md) | 625.2.8.21.5 | light |
| [`/System/Library/Frameworks/ImageIO.framework/ImageIO`](System__Library__Frameworks__ImageIO.framework__ImageIO.md) | 2851.1.8.0.0 | light |
| [`/usr/lib/system/libsystem_c.dylib`](usr__lib__system__libsystem_c.dylib.md) | 1786.40.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities`](System__Library__PrivateFrameworks__AXCoreUtilities.framework__AXCoreUtilities.md) | 3245.8.9.0.0 | light |
| [`/System/Library/AccessibilityBundles/ContactsUI.axbundle/ContactsUI`](System__Library__AccessibilityBundles__ContactsUI.axbundle__ContactsUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PhotosUICore.axbundle/PhotosUICore`](System__Library__AccessibilityBundles__PhotosUICore.axbundle__PhotosUICore.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/HealthKit.axbundle/HealthKit`](System__Library__AccessibilityBundles__HealthKit.axbundle__HealthKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PreferencesFramework.axbundle/PreferencesFramework`](System__Library__AccessibilityBundles__PreferencesFramework.axbundle__PreferencesFramework.md) | 3050.3.8.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend.dylib`](usr__lib__objc__libobjcMsgSend.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/Frameworks/SwiftUICore.framework/SwiftUICore`](System__Library__Frameworks__SwiftUICore.framework__SwiftUICore.md) | 8.1.13.7.0 | light |
| [`/System/Library/Frameworks/Security.framework/Security`](System__Library__Frameworks__Security.framework__Security.md) | 62460.40.78.0.0 | full |
| [`/System/Library/Frameworks/CoreData.framework/CoreData`](System__Library__Frameworks__CoreData.framework__CoreData.md) | 1634.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities`](System__Library__PrivateFrameworks__AccessibilityUtilities.framework__AccessibilityUtilities.md) | 3245.8.9.0.0 | light |
| [`/System/Library/AccessibilityBundles/SpringBoardHome.axbundle/SpringBoardHome`](System__Library__AccessibilityBundles__SpringBoardHome.axbundle__SpringBoardHome.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ContactsAutocompleteUI.axbundle/ContactsAutocompleteUI`](System__Library__AccessibilityBundles__ContactsAutocompleteUI.axbundle__ContactsAutocompleteUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/RemoteUIFramework.axbundle/RemoteUIFramework`](System__Library__AccessibilityBundles__RemoteUIFramework.axbundle__RemoteUIFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/EventKitUIFramework.axbundle/EventKitUIFramework`](System__Library__AccessibilityBundles__EventKitUIFramework.axbundle__EventKitUIFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AVKit.axbundle/AVKit`](System__Library__AccessibilityBundles__AVKit.axbundle__AVKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AuthKitUI.axbundle/AuthKitUI`](System__Library__AccessibilityBundles__AuthKitUI.axbundle__AuthKitUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/OnBoardingKit.axbundle/OnBoardingKit`](System__Library__AccessibilityBundles__OnBoardingKit.axbundle__OnBoardingKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Pegasus.axbundle/Pegasus`](System__Library__AccessibilityBundles__Pegasus.axbundle__Pegasus.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PosterKit.axbundle/PosterKit`](System__Library__AccessibilityBundles__PosterKit.axbundle__PosterKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SwiftUI.axbundle/SwiftUI`](System__Library__AccessibilityBundles__SwiftUI.axbundle__SwiftUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PencilKit.axbundle/PencilKit`](System__Library__AccessibilityBundles__PencilKit.axbundle__PencilKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PDFKit.axbundle/PDFKit`](System__Library__AccessibilityBundles__PDFKit.axbundle__PDFKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MessageUIFramework.axbundle/MessageUIFramework`](System__Library__AccessibilityBundles__MessageUIFramework.axbundle__MessageUIFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PosterUIFoundation.axbundle/PosterUIFoundation`](System__Library__AccessibilityBundles__PosterUIFoundation.axbundle__PosterUIFoundation.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/WorkflowUIServices.axbundle/WorkflowUIServices`](System__Library__AccessibilityBundles__WorkflowUIServices.axbundle__WorkflowUIServices.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SpringBoardUIServices.axbundle/SpringBoardUIServices`](System__Library__AccessibilityBundles__SpringBoardUIServices.axbundle__SpringBoardUIServices.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/LocalAuthenticationPrivateUI.axbundle/LocalAuthenticationPrivateUI`](System__Library__AccessibilityBundles__LocalAuthenticationPrivateUI.axbundle__LocalAuthenticationPrivateUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ControlCenterUIKit.axbundle/ControlCenterUIKit`](System__Library__AccessibilityBundles__ControlCenterUIKit.axbundle__ControlCenterUIKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/BannerKit.axbundle/BannerKit`](System__Library__AccessibilityBundles__BannerKit.axbundle__BannerKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ShareSheet.axbundle/ShareSheet`](System__Library__AccessibilityBundles__ShareSheet.axbundle__ShareSheet.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AccessibilitySettingsLoader.bundle/AccessibilitySettingsLoader`](System__Library__AccessibilityBundles__AccessibilitySettingsLoader.bundle__AccessibilitySettingsLoader.md) | 3245.8.9.0.0 | light |
| [`/System/Library/AccessibilityBundles/UIKit.axbundle/UIKit`](System__Library__AccessibilityBundles__UIKit.axbundle__UIKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AVFoundation.axbundle/AVFoundation`](System__Library__AccessibilityBundles__AVFoundation.axbundle__AVFoundation.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PhotosUIFramework.axbundle/PhotosUIFramework`](System__Library__AccessibilityBundles__PhotosUIFramework.axbundle__PhotosUIFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) | 877.2.2.600.0 | full |
| [`/System/Library/PrivateFrameworks/Gestures.framework/Gestures`](System__Library__PrivateFrameworks__Gestures.framework__Gestures.md) | 9127.1.13.1.107 | light |
| [`/System/Library/PrivateFrameworks/TextInput.framework/TextInput`](System__Library__PrivateFrameworks__TextInput.framework__TextInput.md) | 3568.1.8.600.0 | light |
| [`/System/Library/PrivateFrameworks/AttributeGraph.framework/AttributeGraph`](System__Library__PrivateFrameworks__AttributeGraph.framework__AttributeGraph.md) | 8.1.3.0.0 | light |
| [`/System/Library/Frameworks/SwiftUI.framework/SwiftUI`](System__Library__Frameworks__SwiftUI.framework__SwiftUI.md) | 8.1.13.7.0 | light |
| [`/System/Library/Frameworks/WidgetKit.framework/WidgetKit`](System__Library__Frameworks__WidgetKit.framework__WidgetKit.md) | 7749.2.13.0.3 | light |
| [`/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils`](System__Library__PrivateFrameworks__CoreUtils.framework__CoreUtils.md) | 910.31.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices`](System__Library__PrivateFrameworks__ChronoServices.framework__ChronoServices.md) | 7749.2.13.0.3 | light |
| [`/System/Library/PrivateFrameworks/DesignLibrary.framework/DesignLibrary`](System__Library__PrivateFrameworks__DesignLibrary.framework__DesignLibrary.md) | 8.1.13.0.0 | light |
| [`/System/Library/AccessibilityBundles/TextInputUI.axbundle/TextInputUI`](System__Library__AccessibilityBundles__TextInputUI.axbundle__TextInputUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices`](System__Library__PrivateFrameworks__RunningBoardServices.framework__RunningBoardServices.md) | 1084.40.7.0.0 | light |
| [`/usr/lib/system/libsystem_platform.dylib`](usr__lib__system__libsystem_platform.dylib.md) | 402.40.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`](System__Library__PrivateFrameworks__AppleMediaServices.framework__AppleMediaServices.md) | 10.1.18.2.1 | light |
| [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) | 3896.200.61.0.0 | full |
| [`/System/Library/Frameworks/Intents.framework/Intents`](System__Library__Frameworks__Intents.framework__Intents.md) | 4016.1.16.0.0 | light |
| [`/System/Library/Frameworks/AppIntents.framework/AppIntents`](System__Library__Frameworks__AppIntents.framework__AppIntents.md) | 301.1.16.0.0 | light |
| [`/System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata`](System__Library__PrivateFrameworks__LinkMetadata.framework__LinkMetadata.md) | 301.1.16.0.0 | light |
| [`/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices`](System__Library__PrivateFrameworks__LinkServices.framework__LinkServices.md) | 301.1.16.0.0 | light |
| [`/usr/lib/swift/libswift_RegexParser.dylib`](usr__lib__swift__libswift_RegexParser.dylib.md) | 6.4.2.1.9 | light |
| [`/usr/lib/swift/libswift_StringProcessing.dylib`](usr__lib__swift__libswift_StringProcessing.dylib.md) | 6.4.2.1.9 | light |
| [`/System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary`](System__Library__PrivateFrameworks__BiomeLibrary.framework__BiomeLibrary.md) | 441.26.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/UserManagement.framework/UserManagement`](System__Library__PrivateFrameworks__UserManagement.framework__UserManagement.md) | 490.0.3.0.0 | light |
| [`/usr/lib/system/libsystem_trace.dylib`](usr__lib__system__libsystem_trace.dylib.md) | 1966.40.15.0.2 | light |
| [`/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`](System__Library__Frameworks__VideoToolbox.framework__VideoToolbox.md) | 3385.14.1.3.0 | full |
| [`/System/Library/Frameworks/CoreMedia.framework/CoreMedia`](System__Library__Frameworks__CoreMedia.framework__CoreMedia.md) | 3385.14.1.3.0 | light |
| [`/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`](System__Library__Frameworks__IOKit.framework__Versions__A__IOKit.md) | 100288.40.8.0.1 | full |
| [`/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight`](System__Library__Frameworks__CoreSpotlight.framework__CoreSpotlight.md) | 2465.1.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/Proximity.framework/Proximity`](System__Library__PrivateFrameworks__Proximity.framework__Proximity.md) | 576.0.1.0.0 | light |
| [`/System/Library/AccessibilityBundles/FMFindingUI.axbundle/FMFindingUI`](System__Library__AccessibilityBundles__FMFindingUI.axbundle__FMFindingUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ChatKitFramework.axbundle/ChatKitFramework`](System__Library__AccessibilityBundles__ChatKitFramework.axbundle__ChatKitFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit`](System__Library__PrivateFrameworks__ChatKit.framework__ChatKit.md) | 1491.200.101.21.5 | light |
| [`/usr/lib/objc/libobjcMsgSend1.dylib`](usr__lib__objc__libobjcMsgSend1.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/GeoServices.framework/GeoServices`](System__Library__PrivateFrameworks__GeoServices.framework__GeoServices.md) | 2076.31.9.18.106 | light |
| [`/System/Library/AccessibilityBundles/CommunicationDetails.axbundle/CommunicationDetails`](System__Library__AccessibilityBundles__CommunicationDetails.axbundle__CommunicationDetails.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/VoiceTriggerUI.axbundle/VoiceTriggerUI`](System__Library__AccessibilityBundles__VoiceTriggerUI.axbundle__VoiceTriggerUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal`](System__Library__PrivateFrameworks__CollectionsInternal.framework__CollectionsInternal.md) | 5027.1.6.0.0 | light |
| [`/usr/lib/libicucore.A.dylib`](usr__lib__libicucore.A.dylib.md) | 78138.0.0.0.0 | light |
| [`/usr/lib/swift/libswiftDispatch.dylib`](usr__lib__swift__libswiftDispatch.dylib.md) | 1605.40.4.0.0 | full |
| [`/usr/lib/libAccessibility.dylib`](usr__lib__libAccessibility.dylib.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime`](System__Library__PrivateFrameworks__AXRuntime.framework__AXRuntime.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard`](System__Library__PrivateFrameworks__BaseBoard.framework__BaseBoard.md) | 827.2.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/BoardServices.framework/BoardServices`](System__Library__PrivateFrameworks__BoardServices.framework__BoardServices.md) | 827.2.3.0.0 | light |
| [`/System/Library/AccessibilityBundles/WritingToolsUI.axbundle/WritingToolsUI`](System__Library__AccessibilityBundles__WritingToolsUI.axbundle__WritingToolsUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/WritingTools.framework/WritingTools`](System__Library__PrivateFrameworks__WritingTools.framework__WritingTools.md) | 151.1.11.100.0 | light |
| [`/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI`](System__Library__PrivateFrameworks__TextInputUI.framework__TextInputUI.md) | 9127.1.13.7.0 | light |
| [`/System/Library/AccessibilityBundles/AppleMediaServicesUI.axbundle/AppleMediaServicesUI`](System__Library__AccessibilityBundles__AppleMediaServicesUI.axbundle__AppleMediaServicesUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SearchUI.axbundle/SearchUI`](System__Library__AccessibilityBundles__SearchUI.axbundle__SearchUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SiriSharedUI.axbundle/SiriSharedUI`](System__Library__AccessibilityBundles__SiriSharedUI.axbundle__SiriSharedUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/HealthExperienceUI.axbundle/HealthExperienceUI`](System__Library__AccessibilityBundles__HealthExperienceUI.axbundle__HealthExperienceUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MedicalIDUI.axbundle/MedicalIDUI`](System__Library__AccessibilityBundles__MedicalIDUI.axbundle__MedicalIDUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/HealthUI.axbundle/HealthUI`](System__Library__AccessibilityBundles__HealthUI.axbundle__HealthUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessUI.framework/FitnessUI`](System__Library__PrivateFrameworks__FitnessUI.framework__FitnessUI.md) | 2027.1.27.0.0 | light |
| [`/System/Library/Frameworks/Combine.framework/Combine`](System__Library__Frameworks__Combine.framework__Combine.md) | 3023.0.0.0.0 | light |
| [`/System/Library/Frameworks/HealthKit.framework/HealthKit`](System__Library__Frameworks__HealthKit.framework__HealthKit.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry`](System__Library__PrivateFrameworks__PairedDeviceRegistry.framework__PairedDeviceRegistry.md) | 1075.16.0.0.0 | light |
| [`/usr/lib/swift/libswiftRegexBuilder.dylib`](usr__lib__swift__libswiftRegexBuilder.dylib.md) | 6.4.2.1.9 | light |
| [`/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration`](System__Library__PrivateFrameworks__ManagedConfiguration.framework__ManagedConfiguration.md) | 2483.40.19.0.0 | light |
| [`/usr/lib/swift/libswiftXPC.dylib`](usr__lib__swift__libswiftXPC.dylib.md) | 167.0.2.0.0 | light |
| [`/System/Library/AccessibilityBundles/PassKitUI.axbundle/PassKitUI`](System__Library__AccessibilityBundles__PassKitUI.axbundle__PassKitUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PassKitUIFoundation.axbundle/PassKitUIFoundation`](System__Library__AccessibilityBundles__PassKitUIFoundation.axbundle__PassKitUIFoundation.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation`](System__Library__PrivateFrameworks__UIFoundation.framework__UIFoundation.md) | 1057.3.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppSupport.framework/AppSupport`](System__Library__PrivateFrameworks__AppSupport.framework__AppSupport.md) | 2672.1.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) | 3605.3.2.0.0 | full |
| [`/System/Library/Frameworks/CoreML.framework/CoreML`](System__Library__Frameworks__CoreML.framework__CoreML.md) | 3600.25.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet`](System__Library__PrivateFrameworks__CoreDuet.framework__CoreDuet.md) | 1977.0.0.0.0 | light |
| [`/System/Library/Frameworks/Contacts.framework/Contacts`](System__Library__Frameworks__Contacts.framework__Contacts.md) | 3846.200.91.2.1 | light |
| [`/System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers`](System__Library__Frameworks__UniformTypeIdentifiers.framework__UniformTypeIdentifiers.md) | 919.1.13.6.0 | light |
| [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) | 2482.2.0.0.0 | full |
| [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) | 3385.14.1.3.0 | full |
| [`/usr/lib/libc++.1.dylib`](usr__lib__libc++.1.dylib.md) | 2200.32.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation`](System__Library__PrivateFrameworks__IDSFoundation.framework__IDSFoundation.md) | 2003.200.71.2.4 | light |
| [`/System/Library/PrivateFrameworks/IDS.framework/IDS`](System__Library__PrivateFrameworks__IDS.framework__IDS.md) | 2003.200.71.2.4 | light |
| [`/System/Library/Frameworks/CloudKit.framework/CloudKit`](System__Library__Frameworks__CloudKit.framework__CloudKit.md) | 2720.17.6.0.0 | light |
| [`/System/Library/Frameworks/MediaAccessibility.framework/MediaAccessibility`](System__Library__Frameworks__MediaAccessibility.framework__MediaAccessibility.md) | 241.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal`](System__Library__PrivateFrameworks__CoreServicesInternal.framework__CoreServicesInternal.md) | 609.1.7.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend2.dylib`](usr__lib__objc__libobjcMsgSend2.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary`](System__Library__PrivateFrameworks__IntelligencePlatformLibrary.framework__IntelligencePlatformLibrary.md) | 441.26.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices`](System__Library__PrivateFrameworks__AssistantServices.framework__AssistantServices.md) | 3605.31.1.11.2 | light |
| [`/System/Library/PrivateFrameworks/TipKitCore.framework/TipKitCore`](System__Library__PrivateFrameworks__TipKitCore.framework__TipKitCore.md) | 129.1.2.0.0 | light |
| [`/System/Library/Frameworks/SwiftData.framework/SwiftData`](System__Library__Frameworks__SwiftData.framework__SwiftData.md) | 187.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices`](System__Library__PrivateFrameworks__PhotoLibraryServices.framework__PhotoLibraryServices.md) | 916.62.154.0.0 | light |
| [`/System/Library/Frameworks/Photos.framework/Photos`](System__Library__Frameworks__Photos.framework__Photos.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) | 9127.1.13.13.0 | full |
| [`/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices`](System__Library__PrivateFrameworks__SpringBoardServices.framework__SpringBoardServices.md) | 4637.1.14.102.9 | light |
| [`/System/Library/Frameworks/CoreText.framework/CoreText`](System__Library__Frameworks__CoreText.framework__CoreText.md) | 910.0.0.0.0 | light |
| [`/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore`](System__Library__Frameworks__JavaScriptCore.framework__JavaScriptCore.md) | 625.2.8.21.2 | light |
| [`/System/Library/Frameworks/WebKit.framework/WebKit`](System__Library__Frameworks__WebKit.framework__WebKit.md) | 625.2.8.21.2 | light |
| [`/usr/lib/system/libsystem_info.dylib`](usr__lib__system__libsystem_info.dylib.md) | 603.40.2.0.0 | light |
| [`/usr/lib/libsqlite3.dylib`](usr__lib__libsqlite3.dylib.md) | 408.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/Dyld.framework/Dyld`](System__Library__PrivateFrameworks__Dyld.framework__Dyld.md) | 27104.0.0.0.0 | light |
| [`/usr/lib/system/libsystem_coreservices.dylib`](usr__lib__system__libsystem_coreservices.dylib.md) | 203.1.1.0.0 | light |
| [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) | 13499.0.0.0.0 | full |
| [`/System/Library/Frameworks/ActivityKit.framework/ActivityKit`](System__Library__Frameworks__ActivityKit.framework__ActivityKit.md) | 313.2.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) | 1628.200.81.21.4 | full |
| [`/System/Library/PrivateFrameworks/UIIntelligenceSupport.framework/UIIntelligenceSupport`](System__Library__PrivateFrameworks__UIIntelligenceSupport.framework__UIIntelligenceSupport.md) | 9127.1.13.0.0 | light |
| [`/usr/lib/swift/libswiftos.dylib`](usr__lib__swift__libswiftos.dylib.md) | 1090.40.3.0.0 | light |
| [`/System/Library/Frameworks/ColorSync.framework/ColorSync`](System__Library__Frameworks__ColorSync.framework__ColorSync.md) | 3929.1.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) | 1638.215.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`](System__Library__PrivateFrameworks__AudioSession.framework__AudioSession.md) | 449.207.0.0.0 | full |
| [`/System/Library/AccessibilityBundles/StickerKit.axbundle/StickerKit`](System__Library__AccessibilityBundles__StickerKit.axbundle__StickerKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/AnimationKit.framework/AnimationKit`](System__Library__PrivateFrameworks__AnimationKit.framework__AnimationKit.md) | 9127.1.13.13.0 | light |
| [`/System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices`](System__Library__PrivateFrameworks__ModelManagerServices.framework__ModelManagerServices.md) | 714.40.86.0.0 | light |
| [`/System/Library/PrivateFrameworks/SoftwareUpdateCoreConnect.framework/SoftwareUpdateCoreConnect`](System__Library__PrivateFrameworks__SoftwareUpdateCoreConnect.framework__SoftwareUpdateCoreConnect.md) | 2718.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation`](System__Library__PrivateFrameworks__ContactsFoundation.framework__ContactsFoundation.md) | 1430.200.41.0.0 | light |
| [`/System/Library/PrivateFrameworks/ContactsUICore.framework/ContactsUICore`](System__Library__PrivateFrameworks__ContactsUICore.framework__ContactsUICore.md) | 3723.200.91.2.1 | light |
| [`/System/Library/Frameworks/ContactsUI.framework/ContactsUI`](System__Library__Frameworks__ContactsUI.framework__ContactsUI.md) | 1463.200.91.2.1 | light |
| [`/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities`](System__Library__PrivateFrameworks__IMSharedUtilities.framework__IMSharedUtilities.md) | 1491.200.101.21.5 | light |
| [`/System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation`](System__Library__PrivateFrameworks__IMFoundation.framework__IMFoundation.md) | 1138.200.21.0.0 | light |
| [`/System/Library/Frameworks/Accounts.framework/Accounts`](System__Library__Frameworks__Accounts.framework__Accounts.md) | 1125.0.0.0.0 | light |
| [`/System/Library/Frameworks/CryptoKit.framework/CryptoKit`](System__Library__Frameworks__CryptoKit.framework__CryptoKit.md) | 383.40.14.0.0 | light |
| [`/System/Library/PrivateFrameworks/GeoAnalytics.framework/GeoAnalytics`](System__Library__PrivateFrameworks__GeoAnalytics.framework__GeoAnalytics.md) | 2076.31.9.18.106 | light |
| [`/System/Library/PrivateFrameworks/MallocStackLogging.framework/MallocStackLogging`](System__Library__PrivateFrameworks__MallocStackLogging.framework__MallocStackLogging.md) | 64578.132.1.0.0 | light |
| [`/usr/lib/libFDR.dylib`](usr__lib__libFDR.dylib.md) | 1636.40.11.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend3.dylib`](usr__lib__objc__libobjcMsgSend3.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/WebCore.framework/WebCore`](System__Library__PrivateFrameworks__WebCore.framework__WebCore.md) | 625.2.8.21.2 | light |
| [`/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore`](System__Library__PrivateFrameworks__PassKitCore.framework__PassKitCore.md) | 1696.2.9.2.0 | light |
| [`/System/Library/Frameworks/HomeKit.framework/HomeKit`](System__Library__Frameworks__HomeKit.framework__HomeKit.md) | 1520.2.7.1.3 | light |
| [`/System/Library/Frameworks/Metal.framework/Metal`](System__Library__Frameworks__Metal.framework__Metal.md) | 383.1.2.0.0 | full |
| [`/System/Library/Frameworks/CoreImage.framework/CoreImage`](System__Library__Frameworks__CoreImage.framework__CoreImage.md) | 1667.40.6.0.0 | light |
| [`/System/Library/Frameworks/Vision.framework/Vision`](System__Library__Frameworks__Vision.framework__Vision.md) | 10.1.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto`](System__Library__PrivateFrameworks__CMPhoto.framework__CMPhoto.md) | 488.40.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/JetEngine.framework/JetEngine`](System__Library__PrivateFrameworks__JetEngine.framework__JetEngine.md) | 10.1.11.0.0 | light |
| [`/System/Library/Frameworks/MediaPlayer.framework/MediaPlayer`](System__Library__Frameworks__MediaPlayer.framework__MediaPlayer.md) | 4026.210.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`](System__Library__PrivateFrameworks__MediaRemote.framework__MediaRemote.md) | 4026.210.4.0.0 | light |
| [`/System/Library/Frameworks/MapKit.framework/MapKit`](System__Library__Frameworks__MapKit.framework__MapKit.md) | 2552.31.6.17.115 | light |
| [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) | 3187.0.1.0.0 | full |
| [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) | 3187.0.1.0.0 | full |
| [`/usr/lib/libTelephonyUtilDynamic.dylib`](usr__lib__libTelephonyUtilDynamic.dylib.md) | 6575.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) | 1153.2.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices`](System__Library__PrivateFrameworks__SpringBoardUIServices.framework__SpringBoardUIServices.md) | 4637.1.14.102.9 | light |
| [`/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount`](System__Library__PrivateFrameworks__AppleAccount.framework__AppleAccount.md) | 1069.125.7.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend4.dylib`](usr__lib__objc__libobjcMsgSend4.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`](System__Library__PrivateFrameworks__AuthKit.framework__AuthKit.md) | 560.125.6.1.0 | light |
| [`/System/Library/PrivateFrameworks/RTCReporting.framework/RTCReporting`](System__Library__PrivateFrameworks__RTCReporting.framework__RTCReporting.md) | 190.11.0.0.0 | light |
| [`/System/Library/AccessibilityBundles/DisplayAndBrightnessSettings.axbundle/DisplayAndBrightnessSettings`](System__Library__AccessibilityBundles__DisplayAndBrightnessSettings.axbundle__DisplayAndBrightnessSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CameraUI.axbundle/CameraUI`](System__Library__AccessibilityBundles__CameraUI.axbundle__CameraUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate`](System__Library__PrivateFrameworks__PhotosUIPrivate.framework__PhotosUIPrivate.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit`](System__Library__PrivateFrameworks__PosterKit.framework__PosterKit.md) | 355.2.12.0.4 | light |
| [`/System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources`](System__Library__PrivateFrameworks__SpotlightResources.framework__SpotlightResources.md) | 2465.1.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs`](System__Library__PrivateFrameworks__CloudDocs.framework__CloudDocs.md) | 5168.40.162.0.0 | light |
| [`/System/Library/Frameworks/FileProvider.framework/FileProvider`](System__Library__Frameworks__FileProvider.framework__FileProvider.md) | 4838.42.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/PersonalizationPortrait.framework/PersonalizationPortrait`](System__Library__PrivateFrameworks__PersonalizationPortrait.framework__PersonalizationPortrait.md) | 1354.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/Montreal.framework/Montreal`](System__Library__PrivateFrameworks__Montreal.framework__Montreal.md) | 188.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech`](System__Library__PrivateFrameworks__TextToSpeech.framework__TextToSpeech.md) | 727.3.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext`](System__Library__PrivateFrameworks__CoreDuetContext.framework__CoreDuetContext.md) | 1977.0.0.0.0 | light |
| [`/usr/lib/libboringssl.dylib`](usr__lib__libboringssl.dylib.md) | 583.40.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy`](System__Library__PrivateFrameworks__NetworkServiceProxy.framework__NetworkServiceProxy.md) | 990.40.2.0.0 | light |
| [`/System/Library/Frameworks/_AppIntents_UIKit.framework/_AppIntents_UIKit`](System__Library__Frameworks___AppIntents_UIKit.framework___AppIntents_UIKit.md) | 301.1.16.0.0 | light |
| [`/System/Library/Frameworks/TipKit.framework/TipKit`](System__Library__Frameworks__TipKit.framework__TipKit.md) | 129.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/Sharing.framework/Sharing`](System__Library__PrivateFrameworks__Sharing.framework__Sharing.md) | 2131.21.31.21.8 | light |
| [`/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore`](System__Library__PrivateFrameworks__SafariCore.framework__SafariCore.md) | 625.2.8.21.5 | light |
| [`/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared`](System__Library__PrivateFrameworks__SafariShared.framework__SafariShared.md) | 625.2.8.21.5 | light |
| [`/System/Library/PrivateFrameworks/JetAsset.framework/JetAsset`](System__Library__PrivateFrameworks__JetAsset.framework__JetAsset.md) | 10.1.11.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleMediaServicesKitInternal.framework/AppleMediaServicesKitInternal`](System__Library__PrivateFrameworks__AppleMediaServicesKitInternal.framework__AppleMediaServicesKitInternal.md) | 2.1.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary`](System__Library__PrivateFrameworks__InstalledContentLibrary.framework__InstalledContentLibrary.md) | 1680.40.14.0.0 | light |
| [`/System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration`](System__Library__Frameworks__SystemConfiguration.framework__SystemConfiguration.md) | 1453.40.1.0.0 | light |
| [`/usr/lib/system/libsystem_networkextension.dylib`](usr__lib__system__libsystem_networkextension.dylib.md) | 2365.40.3.0.2 | light |
| [`/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension`](System__Library__Frameworks__NetworkExtension.framework__NetworkExtension.md) | 2365.40.3.0.2 | light |
| [`/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore`](System__Library__PrivateFrameworks__PhotoLibraryServicesCore.framework__PhotoLibraryServicesCore.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler`](System__Library__PrivateFrameworks__ANECompiler.framework__ANECompiler.md) | 10.205.4.0.0 | full |
| [`/System/Library/PrivateFrameworks/CoreSceneUnderstanding.framework/CoreSceneUnderstanding`](System__Library__PrivateFrameworks__CoreSceneUnderstanding.framework__CoreSceneUnderstanding.md) | 98.0.0.0.0 | light |
| [`/System/Library/Frameworks/LinkPresentation.framework/LinkPresentation`](System__Library__Frameworks__LinkPresentation.framework__LinkPresentation.md) | 317.0.0.0.0 | light |
| [`/System/Library/Frameworks/SensitiveContentAnalysis.framework/SensitiveContentAnalysis`](System__Library__Frameworks__SensitiveContentAnalysis.framework__SensitiveContentAnalysis.md) | 151.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) | 764.42.9.0.0 | full |
| [`/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks`](System__Library__PrivateFrameworks__BackgroundSystemTasks.framework__BackgroundSystemTasks.md) | 2467.52.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport`](System__Library__PrivateFrameworks__ProactiveSupport.framework__ProactiveSupport.md) | 425.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform`](System__Library__PrivateFrameworks__IntelligencePlatform.framework__IntelligencePlatform.md) | 194.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/GRDBInternal.framework/GRDBInternal`](System__Library__PrivateFrameworks__GRDBInternal.framework__GRDBInternal.md) | 19.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/Coherence.framework/Coherence`](System__Library__PrivateFrameworks__Coherence.framework__Coherence.md) | 241.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset`](System__Library__PrivateFrameworks__MobileAsset.framework__MobileAsset.md) | 2215.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag`](System__Library__PrivateFrameworks__MobileKeyBag.framework__MobileKeyBag.md) | 697.40.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities`](System__Library__PrivateFrameworks__DMCUtilities.framework__DMCUtilities.md) | 113.52.1.0.0 | light |
| [`/System/Library/Frameworks/SharedWithYou.framework/SharedWithYou`](System__Library__Frameworks__SharedWithYou.framework__SharedWithYou.md) | 217.200.51.0.0 | light |
| [`/System/Library/Frameworks/Accessibility.framework/Accessibility`](System__Library__Frameworks__Accessibility.framework__Accessibility.md) | 591.4.5.0.0 | light |
| [`/usr/lib/swift/libswiftObservation.dylib`](usr__lib__swift__libswiftObservation.dylib.md) | 6.4.2.1.9 | light |
| [`/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience`](System__Library__PrivateFrameworks__MediaExperience.framework__MediaExperience.md) | 385.10.1.0.0 | light |
| [`/usr/lib/system/libdispatch.dylib`](usr__lib__system__libdispatch.dylib.md) | 1605.40.4.0.0 | full |
| [`/System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit`](System__Library__Frameworks__BrowserEngineKit.framework__BrowserEngineKit.md) | 7625.2.1.1.0 | light |
| [`/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices`](System__Library__Frameworks__AuthenticationServices.framework__AuthenticationServices.md) | 625.2.8.21.5 | light |
| [`/System/Library/Frameworks/StoreKit.framework/StoreKit`](System__Library__Frameworks__StoreKit.framework__StoreKit.md) | 816.1.16.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI`](System__Library__PrivateFrameworks__AppleMediaServicesUI.framework__AppleMediaServicesUI.md) | 8.1.23.2.2 | light |
| [`/System/Library/Frameworks/AVKit.framework/AVKit`](System__Library__Frameworks__AVKit.framework__AVKit.md) | 1392.5.0.0.0 | light |
| [`/usr/lib/libxml2.2.dylib`](usr__lib__libxml2.2.dylib.md) | 40.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy`](System__Library__PrivateFrameworks__WebKitLegacy.framework__WebKitLegacy.md) | 625.2.8.21.2 | light |
| [`/System/Library/Frameworks/SafariServices.framework/SafariServices`](System__Library__Frameworks__SafariServices.framework__SafariServices.md) | 625.2.8.21.5 | light |
| [`/usr/lib/libMobileGestalt.dylib`](usr__lib__libMobileGestalt.dylib.md) | 1622.40.11.0.0 | full |
| [`/System/Library/PrivateFrameworks/QueryParser.framework/QueryParser`](System__Library__PrivateFrameworks__QueryParser.framework__QueryParser.md) | 3605.8.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/GenerativeFunctionsInstrumentation`](System__Library__PrivateFrameworks__GenerativeFunctionsInstrumentation.framework__GenerativeFunctionsInstrumentation.md) | 297.12.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/GenerativeModelsFoundation.framework/GenerativeModelsFoundation`](System__Library__PrivateFrameworks__GenerativeModelsFoundation.framework__GenerativeModelsFoundation.md) | 297.12.4.0.0 | light |
| [`/System/Library/Frameworks/CoreVideo.framework/CoreVideo`](System__Library__Frameworks__CoreVideo.framework__CoreVideo.md) | 776.2.0.0.0 | light |
| [`/System/Library/Frameworks/BackgroundTasks.framework/BackgroundTasks`](System__Library__Frameworks__BackgroundTasks.framework__BackgroundTasks.md) | 2467.52.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/UserActivity.framework/UserActivity`](System__Library__PrivateFrameworks__UserActivity.framework__UserActivity.md) | 630.1.1.0.0 | light |
| [`/System/Library/Frameworks/EventKit.framework/EventKit`](System__Library__Frameworks__EventKit.framework__EventKit.md) | 1976.2.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics`](System__Library__PrivateFrameworks__CoreAnalytics.framework__CoreAnalytics.md) | 577.40.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics`](System__Library__PrivateFrameworks__OSAnalytics.framework__OSAnalytics.md) | 1056.40.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf`](System__Library__PrivateFrameworks__InternalSwiftProtobuf.framework__InternalSwiftProtobuf.md) | 22.0.0.0.0 | light |
| [`/usr/lib/libnwswifttls.dylib`](usr__lib__libnwswifttls.dylib.md) | 171.40.10.0.0 | light |
| [`/System/Library/AccessibilityBundles/Moments.axbundle/Moments`](System__Library__AccessibilityBundles__Moments.axbundle__Moments.md) | 3050.3.8.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend5.dylib`](usr__lib__objc__libobjcMsgSend5.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) | 764.42.9.0.0 | full |
| [`/System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor`](System__Library__PrivateFrameworks__BlastDoor.framework__BlastDoor.md) | 331.200.71.0.0 | light |
| [`/System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials`](System__Library__Frameworks___LocationEssentials.framework___LocationEssentials.md) | 3187.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService`](System__Library__PrivateFrameworks__SiriTTSService.framework__SiriTTSService.md) | 3605.41.1.0.0 | light |
| [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) | 1638.215.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/VFX.framework/VFX`](System__Library__PrivateFrameworks__VFX.framework__VFX.md) | 233.40.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy`](System__Library__PrivateFrameworks__AddressBookLegacy.framework__AddressBookLegacy.md) | 12880.200.21.0.0 | light |
| [`/System/Library/PrivateFrameworks/RenderBox.framework/RenderBox`](System__Library__PrivateFrameworks__RenderBox.framework__RenderBox.md) | 8.1.13.0.0 | light |
| [`/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient`](System__Library__PrivateFrameworks__VoiceShortcutClient.framework__VoiceShortcutClient.md) | 5114.0.12.0.0 | light |
| [`/System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation`](System__Library__PrivateFrameworks__SearchFoundation.framework__SearchFoundation.md) | 3605.27.1.11.1 | light |
| [`/System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec`](System__Library__PrivateFrameworks__CoreParsec.framework__CoreParsec.md) | 3605.27.1.11.1 | light |
| [`/System/Library/PrivateFrameworks/CoreSuggestions.framework/CoreSuggestions`](System__Library__PrivateFrameworks__CoreSuggestions.framework__CoreSuggestions.md) | 1354.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreNLP.framework/CoreNLP`](System__Library__PrivateFrameworks__CoreNLP.framework__CoreNLP.md) | 371.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation`](System__Library__PrivateFrameworks__PosterUIFoundation.framework__PosterUIFoundation.md) | 355.2.12.0.4 | light |
| [`/System/Library/PrivateFrameworks/CoverSheetKit.framework/CoverSheetKit`](System__Library__PrivateFrameworks__CoverSheetKit.framework__CoverSheetKit.md) | 159.2.5.0.6 | light |
| [`/System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats`](System__Library__PrivateFrameworks__PhotosFormats.framework__PhotosFormats.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore`](System__Library__PrivateFrameworks__PhotosUICore.framework__PhotosUICore.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud`](System__Library__PrivateFrameworks__iTunesCloud.framework__iTunesCloud.md) | 4026.210.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/MediaServices.framework/MediaServices`](System__Library__PrivateFrameworks__MediaServices.framework__MediaServices.md) | 4026.200.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/VectorKit.framework/VectorKit`](System__Library__PrivateFrameworks__VectorKit.framework__VectorKit.md) | 2044.31.9.18.103 | light |
| [`/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet`](System__Library__PrivateFrameworks__ShareSheet.framework__ShareSheet.md) | 2131.21.31.21.8 | light |
| [`/System/Library/PrivateFrameworks/ManagedSettingsObjC.framework/ManagedSettingsObjC`](System__Library__PrivateFrameworks__ManagedSettingsObjC.framework__ManagedSettingsObjC.md) | 319.40.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit`](System__Library__PrivateFrameworks__PlugInKit.framework__PlugInKit.md) | 517.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ReplicatorServices.framework/ReplicatorServices`](System__Library__PrivateFrameworks__ReplicatorServices.framework__ReplicatorServices.md) | 176.2.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer`](System__Library__PrivateFrameworks__MobileTimer.framework__MobileTimer.md) | 2333.2.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory`](System__Library__PrivateFrameworks__CallHistory.framework__CallHistory.md) | 158.200.81.21.9 | light |
| [`/System/Library/PrivateFrameworks/AppIntentsLiveEntitySupport.framework/AppIntentsLiveEntitySupport`](System__Library__PrivateFrameworks__AppIntentsLiveEntitySupport.framework__AppIntentsLiveEntitySupport.md) | 301.1.16.0.0 | light |
| [`/System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService`](System__Library__PrivateFrameworks__ApplePushService.framework__ApplePushService.md) | 1168.200.51.0.0 | light |
| [`/System/Library/PrivateFrameworks/MessageDispatch.framework/MessageDispatch`](System__Library__PrivateFrameworks__MessageDispatch.framework__MessageDispatch.md) | 2027.1.4.0.0 | full |
| [`/System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib`](System__Library__PrivateFrameworks__FontServices.framework__libFontParser.dylib.md) | 463.1.0.1.0 | light |
| [`/System/Library/Frameworks/Charts.framework/Charts`](System__Library__Frameworks__Charts.framework__Charts.md) | 8.1.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities`](System__Library__PrivateFrameworks__MetadataUtilities.framework__MetadataUtilities.md) | 2465.1.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness`](System__Library__PrivateFrameworks__AttentionAwareness.framework__AttentionAwareness.md) | 265.40.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities`](System__Library__PrivateFrameworks__HearingUtilities.framework__HearingUtilities.md) | 543.2.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog`](System__Library__PrivateFrameworks__PowerLog.framework__PowerLog.md) | 3486.52.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`](System__Library__PrivateFrameworks__TelephonyUI.framework__TelephonyUI.md) | 158.200.81.21.9 | full |
| [`/System/Library/PrivateFrameworks/GeoServicesCore.framework/GeoServicesCore`](System__Library__PrivateFrameworks__GeoServicesCore.framework__GeoServicesCore.md) | 2076.31.9.18.106 | light |
| [`/System/Library/PrivateFrameworks/TCC.framework/TCC`](System__Library__PrivateFrameworks__TCC.framework__TCC.md) | 921.0.2.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend6.dylib`](usr__lib__objc__libobjcMsgSend6.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation`](System__Library__PrivateFrameworks__SiriInstrumentation.framework__SiriInstrumentation.md) | 3605.33.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog`](System__Library__PrivateFrameworks__ModelCatalog.framework__ModelCatalog.md) | 308.12.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/TokenGenerationCore.framework/TokenGenerationCore`](System__Library__PrivateFrameworks__TokenGenerationCore.framework__TokenGenerationCore.md) | 307.12.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/TextAnimationSupport.framework/TextAnimationSupport`](System__Library__PrivateFrameworks__TextAnimationSupport.framework__TextAnimationSupport.md) | 8.0.31.0.0 | light |
| [`/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester`](System__Library__PrivateFrameworks__PeopleSuggester.framework__PeopleSuggester.md) | 1977.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppProtection.framework/AppProtection`](System__Library__PrivateFrameworks__AppProtection.framework__AppProtection.md) | 55.1.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/Message.framework/Message`](System__Library__PrivateFrameworks__Message.framework__Message.md) | 3901.200.71.21.4 | light |
| [`/System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle`](System__Library__PrivateFrameworks__FamilyCircle.framework__FamilyCircle.md) | 291.125.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation`](System__Library__PrivateFrameworks__BiomeFoundation.framework__BiomeFoundation.md) | 259.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets`](System__Library__PrivateFrameworks__CascadeSets.framework__CascadeSets.md) | 259.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler`](System__Library__PrivateFrameworks__DuetActivityScheduler.framework__DuetActivityScheduler.md) | 2467.52.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/ContextKitExtraction.framework/ContextKitExtraction`](System__Library__PrivateFrameworks__ContextKitExtraction.framework__ContextKitExtraction.md) | 308.0.0.0.0 | light |
| [`/System/Library/Frameworks/Speech.framework/Speech`](System__Library__Frameworks__Speech.framework__Speech.md) | 3605.24.1.11.3 | light |
| [`/System/Library/PrivateFrameworks/AppleIntelligenceReporting.framework/AppleIntelligenceReporting`](System__Library__PrivateFrameworks__AppleIntelligenceReporting.framework__AppleIntelligenceReporting.md) | 232.40.17.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate`](System__Library__PrivateFrameworks__MobileSoftwareUpdate.framework__MobileSoftwareUpdate.md) | 2718.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) | 1011.4.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/BaseBoardUI.framework/BaseBoardUI`](System__Library__PrivateFrameworks__BaseBoardUI.framework__BaseBoardUI.md) | 827.2.3.0.0 | light |
| [`/System/Library/AccessibilityBundles/ToneKit.axbundle/ToneKit`](System__Library__AccessibilityBundles__ToneKit.axbundle__ToneKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreMaterial.framework/CoreMaterial`](System__Library__PrivateFrameworks__CoreMaterial.framework__CoreMaterial.md) | 226.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) | 4637.1.14.102.9 | full |
| [`/System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility`](System__Library__PrivateFrameworks__UIAccessibility.framework__UIAccessibility.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/SAObjects.framework/SAObjects`](System__Library__PrivateFrameworks__SAObjects.framework__SAObjects.md) | 3605.4.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/PegasusAPI.framework/PegasusAPI`](System__Library__PrivateFrameworks__PegasusAPI.framework__PegasusAPI.md) | 3605.27.1.11.1 | light |
| [`/System/Library/PrivateFrameworks/TokenGeneration.framework/TokenGeneration`](System__Library__PrivateFrameworks__TokenGeneration.framework__TokenGeneration.md) | 307.12.4.0.0 | light |
| [`/System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit`](System__Library__Frameworks__CryptoTokenKit.framework__CryptoTokenKit.md) | 878.40.5.0.0 | light |
| [`/System/Library/Frameworks/AudioToolbox.framework/AudioCodecs`](System__Library__Frameworks__AudioToolbox.framework__AudioCodecs.md) | 818.205.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) | 382.101.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls`](System__Library__PrivateFrameworks__MediaControls.framework__MediaControls.md) | 4026.210.4.0.0 | light |
| [`/System/Library/AccessibilityBundles/MediaControls.axbundle/MediaControls`](System__Library__AccessibilityBundles__MediaControls.axbundle__MediaControls.md) | 3050.3.8.0.0 | light |
| [`/usr/lib/swift/libswiftCoreFoundation.dylib`](usr__lib__swift__libswiftCoreFoundation.dylib.md) | 2412.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/IMCore.framework/IMCore`](System__Library__PrivateFrameworks__IMCore.framework__IMCore.md) | 1491.200.101.21.5 | light |
| [`/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`](System__Library__PrivateFrameworks__IMDPersistence.framework__IMDPersistence.md) | 1491.200.101.21.5 | light |
| [`/usr/lib/swift/libswiftUniformTypeIdentifiers.dylib`](usr__lib__swift__libswiftUniformTypeIdentifiers.dylib.md) | 919.1.13.6.0 | light |
| [`/System/Library/Frameworks/MessageUI.framework/MessageUI`](System__Library__Frameworks__MessageUI.framework__MessageUI.md) | 3901.200.71.21.4 | light |
| [`/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures`](System__Library__PrivateFrameworks__CloudSubscriptionFeatures.framework__CloudSubscriptionFeatures.md) | 301.24.1.8.0 | light |
| [`/System/Library/Frameworks/FinanceKit.framework/FinanceKit`](System__Library__Frameworks__FinanceKit.framework__FinanceKit.md) | 376.1.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) | 4178.40.10.0.0 | full |
| [`/System/Library/PrivateFrameworks/PhotosUIFoundation.framework/PhotosUIFoundation`](System__Library__PrivateFrameworks__PhotosUIFoundation.framework__PhotosUIFoundation.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/PhotoFoundation.framework/PhotoFoundation`](System__Library__PrivateFrameworks__PhotoFoundation.framework__PhotoFoundation.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore`](System__Library__PrivateFrameworks__NeutrinoCore.framework__NeutrinoCore.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/AAAFoundationSwift.framework/AAAFoundationSwift`](System__Library__PrivateFrameworks__AAAFoundationSwift.framework__AAAFoundationSwift.md) | 117.125.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/FindMyLocate.framework/FindMyLocate`](System__Library__PrivateFrameworks__FindMyLocate.framework__FindMyLocate.md) | 141.31.6.16.22 | light |
| [`/System/Library/PrivateFrameworks/CloudTelemetryShared.framework/CloudTelemetryShared`](System__Library__PrivateFrameworks__CloudTelemetryShared.framework__CloudTelemetryShared.md) | 2722.40.2.0.0 | light |
| [`/usr/lib/libnetworkextension.dylib`](usr__lib__libnetworkextension.dylib.md) | 2365.40.3.0.2 | full |
| [`/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication`](System__Library__PrivateFrameworks__Symbolication.framework__Symbolication.md) | 64578.132.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/Rapport.framework/Rapport`](System__Library__PrivateFrameworks__Rapport.framework__Rapport.md) | 751.200.101.0.0 | light |
| [`/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore`](System__Library__PrivateFrameworks__ScreenTimeCore.framework__ScreenTimeCore.md) | 655.1.14.1.0 | light |
| [`/System/Library/PrivateFrameworks/_JetEngine_SwiftUI.framework/_JetEngine_SwiftUI`](System__Library__PrivateFrameworks___JetEngine_SwiftUI.framework___JetEngine_SwiftUI.md) | 10.1.11.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreUtilsSwift.framework/CoreUtilsSwift`](System__Library__PrivateFrameworks__CoreUtilsSwift.framework__CoreUtilsSwift.md) | 910.31.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics`](System__Library__PrivateFrameworks__AppAnalytics.framework__AppAnalytics.md) | 573.0.0.0.0 | light |
| [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) | 794.210.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/ActivityUIServices.framework/ActivityUIServices`](System__Library__PrivateFrameworks__ActivityUIServices.framework__ActivityUIServices.md) | 313.2.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/Preferences.framework/Preferences`](System__Library__PrivateFrameworks__Preferences.framework__Preferences.md) | 5315.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/GenerativeSearch.framework/GenerativeSearch`](System__Library__PrivateFrameworks__GenerativeSearch.framework__GenerativeSearch.md) | 73.3.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport`](System__Library__PrivateFrameworks__SoftwareUpdateCoreSupport.framework__SoftwareUpdateCoreSupport.md) | 2718.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreEmoji.framework/CoreEmoji`](System__Library__PrivateFrameworks__CoreEmoji.framework__CoreEmoji.md) | 285.1.2.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend7.dylib`](usr__lib__objc__libobjcMsgSend7.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ToolKit.framework/ToolKit`](System__Library__PrivateFrameworks__ToolKit.framework__ToolKit.md) | 5114.0.12.0.0 | light |
| [`/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/MessagesBlastDoorSupport`](System__Library__PrivateFrameworks__MessagesBlastDoorSupport.framework__MessagesBlastDoorSupport.md) | 331.200.71.0.0 | light |
| [`/System/Library/PrivateFrameworks/CalendarFoundation.framework/CalendarFoundation`](System__Library__PrivateFrameworks__CalendarFoundation.framework__CalendarFoundation.md) | 1636.2.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/NotesSupport.framework/NotesSupport`](System__Library__PrivateFrameworks__NotesSupport.framework__NotesSupport.md) | 3001.42.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessIntelligence.framework/FitnessIntelligence`](System__Library__PrivateFrameworks__FitnessIntelligence.framework__FitnessIntelligence.md) | 2027.1.35.0.0 | light |
| [`/System/Library/Frameworks/UserNotifications.framework/UserNotifications`](System__Library__Frameworks__UserNotifications.framework__UserNotifications.md) | 720.2.7.0.0 | light |
| [`/System/Library/Frameworks/CallKit.framework/CallKit`](System__Library__Frameworks__CallKit.framework__CallKit.md) | 1406.200.101.21.1 | light |
| [`/System/Library/PrivateFrameworks/FTServices.framework/FTServices`](System__Library__PrivateFrameworks__FTServices.framework__FTServices.md) | 2003.200.71.2.4 | light |
| [`/System/Library/PrivateFrameworks/CommonUtilities.framework/CommonUtilities`](System__Library__PrivateFrameworks__CommonUtilities.framework__CommonUtilities.md) | 302.100.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) | 211.37.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/EmojiFoundation.framework/EmojiFoundation`](System__Library__PrivateFrameworks__EmojiFoundation.framework__EmojiFoundation.md) | 286.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ContactsAutocompleteUI.framework/ContactsAutocompleteUI`](System__Library__PrivateFrameworks__ContactsAutocompleteUI.framework__ContactsAutocompleteUI.md) | 841.200.31.0.0 | light |
| [`/System/Library/Frameworks/LightweightCodeRequirements.framework/LightweightCodeRequirements`](System__Library__Frameworks__LightweightCodeRequirements.framework__LightweightCodeRequirements.md) | 22.40.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/ReminderKit.framework/ReminderKit`](System__Library__PrivateFrameworks__ReminderKit.framework__ReminderKit.md) | 4080.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/IconServices.framework/IconServices`](System__Library__PrivateFrameworks__IconServices.framework__IconServices.md) | 793.1.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI`](System__Library__PrivateFrameworks__SafariSharedUI.framework__SafariSharedUI.md) | 625.2.8.21.5 | light |
| [`/System/Library/PrivateFrameworks/QuickLookUICore.framework/QuickLookUICore`](System__Library__PrivateFrameworks__QuickLookUICore.framework__QuickLookUICore.md) | 1034.1.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration`](System__Library__PrivateFrameworks__PegasusConfiguration.framework__PegasusConfiguration.md) | 3605.27.1.11.1 | light |
| [`/System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub`](System__Library__PrivateFrameworks__BiomePubSub.framework__BiomePubSub.md) | 259.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging`](System__Library__PrivateFrameworks__PhotoImaging.framework__PhotoImaging.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/SensitiveContentAnalysisUI.framework/SensitiveContentAnalysisUI`](System__Library__PrivateFrameworks__SensitiveContentAnalysisUI.framework__SensitiveContentAnalysisUI.md) | 151.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) | 4178.40.10.0.0 | full |
| [`/System/Library/PrivateFrameworks/CarKit.framework/CarKit`](System__Library__PrivateFrameworks__CarKit.framework__CarKit.md) | 807.4.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/ProactiveDaemonSupport`](System__Library__PrivateFrameworks__ProactiveDaemonSupport.framework__ProactiveDaemonSupport.md) | 3605.22.501.11.0 | light |
| [`/System/Library/PrivateFrameworks/OnDeviceStorageCore.framework/OnDeviceStorageCore`](System__Library__PrivateFrameworks__OnDeviceStorageCore.framework__OnDeviceStorageCore.md) | 3.1.15.0.0 | light |
| [`/System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination`](System__Library__PrivateFrameworks__InstallCoordination.framework__InstallCoordination.md) | 849.40.7.0.2 | light |
| [`/System/Library/PrivateFrameworks/SwiftSQLite.framework/SwiftSQLite`](System__Library__PrivateFrameworks__SwiftSQLite.framework__SwiftSQLite.md) | 106.31.6.16.7 | light |
| [`/System/Library/Frameworks/IOSurface.framework/IOSurface`](System__Library__Frameworks__IOSurface.framework__IOSurface.md) | 403.1.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport`](System__Library__PrivateFrameworks__LoggingSupport.framework__LoggingSupport.md) | 1966.40.15.0.2 | light |
| [`/System/Library/PrivateFrameworks/ServicesIntelligence.framework/ServicesIntelligence`](System__Library__PrivateFrameworks__ServicesIntelligence.framework__ServicesIntelligence.md) | 1.81.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/PromotedContentUI.framework/PromotedContentUI`](System__Library__PrivateFrameworks__PromotedContentUI.framework__PromotedContentUI.md) | 557.2.14.0.0 | light |
| [`/System/Library/PrivateFrameworks/ScreenTimeSettingsServices.framework/ScreenTimeSettingsServices`](System__Library__PrivateFrameworks__ScreenTimeSettingsServices.framework__ScreenTimeSettingsServices.md) | 97.1.14.0.0 | light |
| [`/System/Library/AccessibilityBundles/VideosUIFramework.axbundle/VideosUIFramework`](System__Library__AccessibilityBundles__VideosUIFramework.axbundle__VideosUIFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI`](System__Library__PrivateFrameworks__VideosUI.framework__VideosUI.md) | 1145.11.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/XPCDistributed.framework/XPCDistributed`](System__Library__PrivateFrameworks__XPCDistributed.framework__XPCDistributed.md) | 167.0.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/Pegasus.framework/Pegasus`](System__Library__PrivateFrameworks__Pegasus.framework__Pegasus.md) | 311.1.2.600.0 | light |
| [`/System/Library/Frameworks/AVRouting.framework/AVRouting`](System__Library__Frameworks__AVRouting.framework__AVRouting.md) | 385.10.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/TeaUI.framework/TeaUI`](System__Library__PrivateFrameworks__TeaUI.framework__TeaUI.md) | 1517.1.0.0.0 | light |
| [`/System/Library/Frameworks/PDFKit.framework/PDFKit`](System__Library__Frameworks__PDFKit.framework__PDFKit.md) | 1537.1.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreHandwriting.framework/CoreHandwriting`](System__Library__PrivateFrameworks__CoreHandwriting.framework__CoreHandwriting.md) | 587.2.104.0.0 | light |
| [`/System/Library/PrivateFrameworks/ChronoKit.framework/ChronoKit`](System__Library__PrivateFrameworks__ChronoKit.framework__ChronoKit.md) | 7749.2.13.0.3 | light |
| [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) | 1153.2.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome`](System__Library__PrivateFrameworks__SpringBoardHome.framework__SpringBoardHome.md) | 226.2.11.0.2 | light |
| [`/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient`](System__Library__PrivateFrameworks__AppPredictionClient.framework__AppPredictionClient.md) | 678.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/TemplateKit.framework/TemplateKit`](System__Library__PrivateFrameworks__TemplateKit.framework__TemplateKit.md) | 685.1.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppSupportUI.framework/AppSupportUI`](System__Library__PrivateFrameworks__AppSupportUI.framework__AppSupportUI.md) | 43.4.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation`](System__Library__PrivateFrameworks__PosterFoundation.framework__PosterFoundation.md) | 355.2.12.0.4 | light |
| [`/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices`](System__Library__PrivateFrameworks__PosterBoardServices.framework__PosterBoardServices.md) | 355.2.12.0.4 | light |
| [`/System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb`](System__Library__PrivateFrameworks__DoNotDisturb.framework__DoNotDisturb.md) | 511.2.7.0.1 | light |
| [`/System/Library/PrivateFrameworks/CommunicationsUI.framework/CommunicationsUI`](System__Library__PrivateFrameworks__CommunicationsUI.framework__CommunicationsUI.md) | 158.200.81.21.9 | light |
| [`/System/Library/PrivateFrameworks/ConversationKit.framework/ConversationKit`](System__Library__PrivateFrameworks__ConversationKit.framework__ConversationKit.md) | 627.200.81.21.4 | light |
| [`/System/Library/AccessibilityBundles/CommunicationsUI.axbundle/CommunicationsUI`](System__Library__AccessibilityBundles__CommunicationsUI.axbundle__CommunicationsUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ConversationKit.axbundle/ConversationKit`](System__Library__AccessibilityBundles__ConversationKit.axbundle__ConversationKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit`](System__Library__PrivateFrameworks__OnBoardingKit.framework__OnBoardingKit.md) | 3977.0.22.0.600 | light |
| [`/System/Library/PrivateFrameworks/SeymourCore.framework/SeymourCore`](System__Library__PrivateFrameworks__SeymourCore.framework__SeymourCore.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine`](System__Library__PrivateFrameworks__CoreRoutine.framework__CoreRoutine.md) | 1123.0.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreAutoLayout.framework/CoreAutoLayout`](System__Library__PrivateFrameworks__CoreAutoLayout.framework__CoreAutoLayout.md) | 35.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AsyncAlgorithmsInternal.framework/AsyncAlgorithmsInternal`](System__Library__PrivateFrameworks__AsyncAlgorithmsInternal.framework__AsyncAlgorithmsInternal.md) | 5027.1.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/DataDetectorsCore.framework/DataDetectorsCore`](System__Library__PrivateFrameworks__DataDetectorsCore.framework__DataDetectorsCore.md) | 852.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore`](System__Library__PrivateFrameworks__IntelligencePlatformCore.framework__IntelligencePlatformCore.md) | 194.0.0.0.0 | light |
| [`/System/Library/Frameworks/ClockKit.framework/ClockKit`](System__Library__Frameworks__ClockKit.framework__ClockKit.md) | 2483.561.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation`](System__Library__PrivateFrameworks__TeaFoundation.framework__TeaFoundation.md) | 1517.1.0.0.0 | light |
| [`/usr/lib/swift/libswiftCoreLocation.dylib`](usr__lib__swift__libswiftCoreLocation.dylib.md) | 57.0.0.0.0 | full |
| [`/System/Library/Frameworks/Symbols.framework/Symbols`](System__Library__Frameworks__Symbols.framework__Symbols.md) | 207.0.0.0.0 | light |
| [`/System/Library/AccessibilityBundles/PaperKit.axbundle/PaperKit`](System__Library__AccessibilityBundles__PaperKit.axbundle__PaperKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) | 2319.52.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/AudioAnalytics.framework/AudioAnalytics`](System__Library__PrivateFrameworks__AudioAnalytics.framework__AudioAnalytics.md) | 300.205.0.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend8.dylib`](usr__lib__objc__libobjcMsgSend8.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI`](System__Library__PrivateFrameworks__PassKitUI.framework__PassKitUI.md) | 1696.2.9.2.0 | light |
| [`/System/Library/PrivateFrameworks/MapsUI.framework/MapsUI`](System__Library__PrivateFrameworks__MapsUI.framework__MapsUI.md) | 287.31.9.18.102 | light |
| [`/System/Library/PrivateFrameworks/MapsSync.framework/MapsSync`](System__Library__PrivateFrameworks__MapsSync.framework__MapsSync.md) | 188.31.9.18.102 | light |
| [`/System/Library/PrivateFrameworks/SharingUI.framework/SharingUI`](System__Library__PrivateFrameworks__SharingUI.framework__SharingUI.md) | 2131.21.31.21.8 | light |
| [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](System__Library__Frameworks__PencilKit.framework__PencilKit.md) | 622.1.2.600.0 | full |
| [`/System/Library/PrivateFrameworks/WeatherCore.framework/WeatherCore`](System__Library__PrivateFrameworks__WeatherCore.framework__WeatherCore.md) | 1474.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/WeatherDaemon.framework/WeatherDaemon`](System__Library__PrivateFrameworks__WeatherDaemon.framework__WeatherDaemon.md) | 1474.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ktrace.framework/ktrace`](System__Library__PrivateFrameworks__ktrace.framework__ktrace.md) | 706.40.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage`](System__Library__PrivateFrameworks__ProtectedCloudStorage.framework__ProtectedCloudStorage.md) | 1303.40.11.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication`](System__Library__PrivateFrameworks__CoreSymbolication.framework__CoreSymbolication.md) | 64578.104.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ReplicatorEngine.framework/ReplicatorEngine`](System__Library__PrivateFrameworks__ReplicatorEngine.framework__ReplicatorEngine.md) | 176.2.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant`](System__Library__PrivateFrameworks__SetupAssistant.framework__SetupAssistant.md) | 5411.2.4.602.0 | light |
| [`/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore`](System__Library__PrivateFrameworks__TipsCore.framework__TipsCore.md) | 866.2.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationFeed.framework/SymptomPresentationFeed`](System__Library__PrivateFrameworks__Symptoms.framework__Frameworks__SymptomPresentationFeed.framework__SymptomPresentationFeed.md) | 2394.40.17.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriEntityMatcher.framework/SiriEntityMatcher`](System__Library__PrivateFrameworks__SiriEntityMatcher.framework__SiriEntityMatcher.md) | 3605.20.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/PegasusKit.framework/PegasusKit`](System__Library__PrivateFrameworks__PegasusKit.framework__PegasusKit.md) | 3605.27.1.11.1 | light |
| [`/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner`](System__Library__PrivateFrameworks__SPOwner.framework__SPOwner.md) | 449.31.6.16.29 | light |
| [`/System/Library/PrivateFrameworks/FMCoreLite.framework/FMCoreLite`](System__Library__PrivateFrameworks__FMCoreLite.framework__FMCoreLite.md) | 219.31.7.12.1 | light |
| [`/System/Library/PrivateFrameworks/Lexicon.framework/Lexicon`](System__Library__PrivateFrameworks__Lexicon.framework__Lexicon.md) | 219.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/VisualUnderstanding.framework/VisualUnderstanding`](System__Library__PrivateFrameworks__VisualUnderstanding.framework__VisualUnderstanding.md) | 80.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AccessibilityUIUtilities`](System__Library__PrivateFrameworks__AccessibilityUIUtilities.framework__AccessibilityUIUtilities.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/ClarityFoundation.framework/ClarityFoundation`](System__Library__PrivateFrameworks__ClarityFoundation.framework__ClarityFoundation.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/AccessibilitySharedSupport`](System__Library__PrivateFrameworks__AccessibilitySharedSupport.framework__AccessibilitySharedSupport.md) | 591.4.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppSSO.framework/AppSSO`](System__Library__PrivateFrameworks__AppSSO.framework__AppSSO.md) | 643.40.34.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppSSOCore.framework/AppSSOCore`](System__Library__PrivateFrameworks__AppSSOCore.framework__AppSSOCore.md) | 643.40.34.0.0 | light |
| [`/System/Library/PrivateFrameworks/PromotedContent.framework/PromotedContent`](System__Library__PrivateFrameworks__PromotedContent.framework__PromotedContent.md) | 557.2.14.0.0 | light |
| [`/System/Library/PrivateFrameworks/JetUI.framework/JetUI`](System__Library__PrivateFrameworks__JetUI.framework__JetUI.md) | 10.1.11.0.0 | light |
| [`/System/Library/PrivateFrameworks/AdPlatformsCommon.framework/AdPlatformsCommon`](System__Library__PrivateFrameworks__AdPlatformsCommon.framework__AdPlatformsCommon.md) | 557.2.14.0.0 | light |
| [`/System/Library/Frameworks/GroupActivities.framework/GroupActivities`](System__Library__Frameworks__GroupActivities.framework__GroupActivities.md) | 309.200.71.21.1 | light |
| [`/System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices`](System__Library__PrivateFrameworks__TVAppServices.framework__TVAppServices.md) | 207.10.21.0.0 | light |
| [`/System/Library/PrivateFrameworks/SportsKit.framework/SportsKit`](System__Library__PrivateFrameworks__SportsKit.framework__SportsKit.md) | 238.0.0.0.0 | light |
| [`/usr/lib/swift/libswiftAVFoundation.dylib`](usr__lib__swift__libswiftAVFoundation.dylib.md) | 2482.2.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AvatarKit.framework/AvatarKit`](System__Library__PrivateFrameworks__AvatarKit.framework__AvatarKit.md) | 368.101.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AvatarUI.framework/AvatarUI`](System__Library__PrivateFrameworks__AvatarUI.framework__AvatarUI.md) | 406.200.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/BatteryCenterUI.framework/BatteryCenterUI`](System__Library__PrivateFrameworks__BatteryCenterUI.framework__BatteryCenterUI.md) | 328.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/Calculate.framework/Calculate`](System__Library__PrivateFrameworks__Calculate.framework__Calculate.md) | 243.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CalendarLink.framework/CalendarLink`](System__Library__PrivateFrameworks__CalendarLink.framework__CalendarLink.md) | 1327.2.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/PhotosSwiftUICore.framework/PhotosSwiftUICore`](System__Library__PrivateFrameworks__PhotosSwiftUICore.framework__PhotosSwiftUICore.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/IconRendering.framework/IconRendering`](System__Library__PrivateFrameworks__IconRendering.framework__IconRendering.md) | 120.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriSharedUI.framework/SiriSharedUI`](System__Library__PrivateFrameworks__SiriSharedUI.framework__SiriSharedUI.md) | 3605.23.2.3.0 | light |
| [`/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation`](System__Library__PrivateFrameworks__SiriActivation.framework__SiriActivation.md) | 3605.23.2.3.0 | light |
| [`/System/Library/PrivateFrameworks/SiriUICore.framework/SiriUICore`](System__Library__PrivateFrameworks__SiriUICore.framework__SiriUICore.md) | 3600.9.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/CardKit.framework/CardKit`](System__Library__PrivateFrameworks__CardKit.framework__CardKit.md) | 3520.8.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI`](System__Library__PrivateFrameworks__SearchUI.framework__SearchUI.md) | 685.1.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents`](System__Library__PrivateFrameworks__AppStoreComponents.framework__AppStoreComponents.md) | 27.1.12.0.0 | light |
| [`/System/Library/PrivateFrameworks/HybridQueryProcessing.framework/HybridQueryProcessing`](System__Library__PrivateFrameworks__HybridQueryProcessing.framework__HybridQueryProcessing.md) | 73.3.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/GenerativeSearchResultRanker.framework/GenerativeSearchResultRanker`](System__Library__PrivateFrameworks__GenerativeSearchResultRanker.framework__GenerativeSearchResultRanker.md) | 73.3.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/GenerativeSearchAdapter.framework/GenerativeSearchAdapter`](System__Library__PrivateFrameworks__GenerativeSearchAdapter.framework__GenerativeSearchAdapter.md) | 73.3.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/AgentSessionKit.framework/AgentSessionKit`](System__Library__PrivateFrameworks__AgentSessionKit.framework__AgentSessionKit.md) | 297.12.4.0.0 | light |
| [`/System/Library/Frameworks/ManagedAppDistribution.framework/ManagedAppDistribution`](System__Library__Frameworks__ManagedAppDistribution.framework__ManagedAppDistribution.md) | 4.1.15.0.0 | light |
| [`/System/Library/Frameworks/Social.framework/Social`](System__Library__Frameworks__Social.framework__Social.md) | 774.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/PosterBoardUIServices.framework/PosterBoardUIServices`](System__Library__PrivateFrameworks__PosterBoardUIServices.framework__PosterBoardUIServices.md) | 355.2.12.0.4 | light |
| [`/usr/lib/libTelephonyCapabilities.dylib`](usr__lib__libTelephonyCapabilities.dylib.md) | 6575.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/Navigation.framework/Navigation`](System__Library__PrivateFrameworks__Navigation.framework__Navigation.md) | 2436.31.9.18.102 | light |
| [`/System/Library/AccessibilityBundles/VectorKit.axbundle/VectorKit`](System__Library__AccessibilityBundles__VectorKit.axbundle__VectorKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/DeviceConfiguration.framework/DeviceConfiguration`](System__Library__PrivateFrameworks__DeviceConfiguration.framework__DeviceConfiguration.md) | 39.52.1.0.0 | light |
| [`/System/Library/AccessibilityBundles/CallsDialer.axbundle/CallsDialer`](System__Library__AccessibilityBundles__CallsDialer.axbundle__CallsDialer.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CommunicationsSetupUI.axbundle/CommunicationsSetupUI`](System__Library__AccessibilityBundles__CommunicationsSetupUI.axbundle__CommunicationsSetupUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/HealthBalance.framework/HealthBalance`](System__Library__PrivateFrameworks__HealthBalance.framework__HealthBalance.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthBalanceUI.framework/HealthBalanceUI`](System__Library__PrivateFrameworks__HealthBalanceUI.framework__HealthBalanceUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/SeymourMetricsCore.framework/SeymourMetricsCore`](System__Library__PrivateFrameworks__SeymourMetricsCore.framework__SeymourMetricsCore.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/ActivitySharingClient.framework/ActivitySharingClient`](System__Library__PrivateFrameworks__ActivitySharingClient.framework__ActivitySharingClient.md) | 2027.1.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation`](System__Library__PrivateFrameworks__HMFoundation.framework__HMFoundation.md) | 1520.2.7.1.3 | light |
| [`/System/Library/PrivateFrameworks/MapsSupport.framework/MapsSupport`](System__Library__PrivateFrameworks__MapsSupport.framework__MapsSupport.md) | 2972.31.6.17.137 | light |
| [`/System/Library/PrivateFrameworks/BannerKit.framework/BannerKit`](System__Library__PrivateFrameworks__BannerKit.framework__BannerKit.md) | 169.2.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/PlatterKit.framework/PlatterKit`](System__Library__PrivateFrameworks__PlatterKit.framework__PlatterKit.md) | 391.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CallIntelligence.framework/CallIntelligence`](System__Library__PrivateFrameworks__CallIntelligence.framework__CallIntelligence.md) | 158.200.81.21.9 | light |
| [`/System/Library/AccessibilityBundles/MailUI.axbundle/MailUI`](System__Library__AccessibilityBundles__MailUI.axbundle__MailUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/EmailFoundation.framework/EmailFoundation`](System__Library__PrivateFrameworks__EmailFoundation.framework__EmailFoundation.md) | 3901.200.71.21.4 | light |
| [`/System/Library/AccessibilityBundles/SystemApertureUI.axbundle/SystemApertureUI`](System__Library__AccessibilityBundles__SystemApertureUI.axbundle__SystemApertureUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/UserNotificationsUIKit.axbundle/UserNotificationsUIKit`](System__Library__AccessibilityBundles__UserNotificationsUIKit.axbundle__UserNotificationsUIKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI`](System__Library__PrivateFrameworks__MediaCoreUI.framework__MediaCoreUI.md) | 4026.210.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore`](System__Library__PrivateFrameworks__MediaPlaybackCore.framework__MediaPlaybackCore.md) | 26210.26.40.301.0 | light |
| [`/System/Library/PrivateFrameworks/CalendarDaemon.framework/CalendarDaemon`](System__Library__PrivateFrameworks__CalendarDaemon.framework__CalendarDaemon.md) | 1246.2.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/Email.framework/Email`](System__Library__PrivateFrameworks__Email.framework__Email.md) | 3901.200.71.21.4 | light |
| [`/System/Library/PrivateFrameworks/TextUnderstanding.framework/TextUnderstanding`](System__Library__PrivateFrameworks__TextUnderstanding.framework__TextUnderstanding.md) | 192.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ProofReader.framework/ProofReader`](System__Library__PrivateFrameworks__ProofReader.framework__ProofReader.md) | 699.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CVNLP.framework/CVNLP`](System__Library__PrivateFrameworks__CVNLP.framework__CVNLP.md) | 131.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared`](System__Library__PrivateFrameworks__NotesShared.framework__NotesShared.md) | 3001.42.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AXMediaUtilities.framework/AXMediaUtilities`](System__Library__PrivateFrameworks__AXMediaUtilities.framework__AXMediaUtilities.md) | 187.2.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/VisionKitCore.framework/VisionKitCore`](System__Library__PrivateFrameworks__VisionKitCore.framework__VisionKitCore.md) | 347.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport`](System__Library__PrivateFrameworks__InternationalSupport.framework__InternationalSupport.md) | 125.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices`](System__Library__PrivateFrameworks__MediaAnalysisServices.framework__MediaAnalysisServices.md) | 460.14.1.2.0 | light |
| [`/System/Library/Frameworks/FoundationModels.framework/FoundationModels`](System__Library__Frameworks__FoundationModels.framework__FoundationModels.md) | 2.1.14.0.0 | light |
| [`/System/Library/PrivateFrameworks/StoreServices.framework/StoreServices`](System__Library__PrivateFrameworks__StoreServices.framework__StoreServices.md) | 1453.1.1.2.2 | light |
| [`/System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary`](System__Library__PrivateFrameworks__MusicLibrary.framework__MusicLibrary.md) | 4026.200.21.0.0 | light |
| [`/usr/lib/swift/libswiftSynchronization.dylib`](usr__lib__swift__libswiftSynchronization.dylib.md) | 6.4.2.1.9 | light |
| [`/System/Library/PrivateFrameworks/FontServices.framework/libGSFont.dylib`](System__Library__PrivateFrameworks__FontServices.framework__libGSFont.dylib.md) | 176.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary`](System__Library__PrivateFrameworks__ToneLibrary.framework__ToneLibrary.md) | 675.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HearingCore.framework/HearingCore`](System__Library__PrivateFrameworks__HearingCore.framework__HearingCore.md) | 543.2.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/SampleAnalysis.framework/Frameworks/SAHelper.framework/SAHelper`](System__Library__PrivateFrameworks__SampleAnalysis.framework__Frameworks__SAHelper.framework__SAHelper.md) | 441.0.0.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend9.dylib`](usr__lib__objc__libobjcMsgSend9.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal`](System__Library__PrivateFrameworks__MusicKitInternal.framework__MusicKitInternal.md) | 4026.210.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/ComputationalGraph.framework/ComputationalGraph`](System__Library__PrivateFrameworks__ComputationalGraph.framework__ComputationalGraph.md) | 136.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/TipsUI.framework/TipsUI`](System__Library__PrivateFrameworks__TipsUI.framework__TipsUI.md) | 866.2.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) | 578.40.7.0.0 | full |
| [`/System/Library/PrivateFrameworks/ClockFacePosters.framework/ClockFacePosters`](System__Library__PrivateFrameworks__ClockFacePosters.framework__ClockFacePosters.md) | 123.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/Stickers.framework/Stickers`](System__Library__PrivateFrameworks__Stickers.framework__Stickers.md) | 90.1.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleMediaServicesUIKitInternal.framework/AppleMediaServicesUIKitInternal`](System__Library__PrivateFrameworks__AppleMediaServicesUIKitInternal.framework__AppleMediaServicesUIKitInternal.md) | 2.1.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation`](System__Library__PrivateFrameworks__MobileInstallation.framework__MobileInstallation.md) | 1680.40.14.0.0 | light |
| [`/System/Library/PrivateFrameworks/FontServices.framework/FontServices`](System__Library__PrivateFrameworks__FontServices.framework__FontServices.md) | 176.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle`](System__Library__PrivateFrameworks__KeychainCircle.framework__KeychainCircle.md) | 62460.40.78.0.0 | full |
| [`/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation`](System__Library__PrivateFrameworks__AAAFoundation.framework__AAAFoundation.md) | 117.125.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary`](System__Library__PrivateFrameworks__CloudPhotoLibrary.framework__CloudPhotoLibrary.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriOntology.framework/SiriOntology`](System__Library__PrivateFrameworks__SiriOntology.framework__SiriOntology.md) | 3605.4.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation`](System__Library__PrivateFrameworks__CoreSpeechFoundation.framework__CoreSpeechFoundation.md) | 3605.32.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/EmbeddedAcousticRecognition`](System__Library__PrivateFrameworks__EmbeddedAcousticRecognition.framework__EmbeddedAcousticRecognition.md) | 3605.9.1.0.0 | light |
| [`/System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage`](System__Library__Frameworks__NaturalLanguage.framework__NaturalLanguage.md) | 185.0.0.0.0 | light |
| [`/usr/lib/system/libcorecrypto.dylib`](usr__lib__system__libcorecrypto.dylib.md) | 2109.40.22.0.0 | light |
| [`/System/Library/PrivateFrameworks/CloudCoreInternal.framework/CloudCoreInternal`](System__Library__PrivateFrameworks__CloudCoreInternal.framework__CloudCoreInternal.md) | 18.20.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/SyncedDefaults.framework/SyncedDefaults`](System__Library__PrivateFrameworks__SyncedDefaults.framework__SyncedDefaults.md) | 2720.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/FindMyBase.framework/FindMyBase`](System__Library__PrivateFrameworks__FindMyBase.framework__FindMyBase.md) | 106.31.6.16.7 | light |
| [`/System/Library/PrivateFrameworks/CoreKnowledge.framework/CoreKnowledge`](System__Library__PrivateFrameworks__CoreKnowledge.framework__CoreKnowledge.md) | 3600.13.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication`](System__Library__PrivateFrameworks__AppleIDSSOAuthentication.framework__AppleIDSSOAuthentication.md) | 118.125.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/PhotosPosterUI.framework/PhotosPosterUI`](System__Library__PrivateFrameworks__PhotosPosterUI.framework__PhotosPosterUI.md) | 916.62.154.0.0 | light |
| [`/System/Library/AccessibilityBundles/StoreDynamicUIPlugin.axbundle/StoreDynamicUIPlugin`](System__Library__AccessibilityBundles__StoreDynamicUIPlugin.axbundle__StoreDynamicUIPlugin.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon`](System__Library__PrivateFrameworks__AppStoreDaemon.framework__AppStoreDaemon.md) | 13.1.17.0.0 | light |
| [`/System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit`](System__Library__Frameworks__AdAttributionKit.framework__AdAttributionKit.md) | 4.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ContentKit.framework/ContentKit`](System__Library__PrivateFrameworks__ContentKit.framework__ContentKit.md) | 5114.0.12.0.0 | light |
| [`/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit`](System__Library__PrivateFrameworks__WorkflowKit.framework__WorkflowKit.md) | 5114.0.12.0.0 | light |
| [`/System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit`](System__Library__PrivateFrameworks__CalendarUIKit.framework__CalendarUIKit.md) | 1327.2.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging`](System__Library__PrivateFrameworks__CMImaging.framework__CMImaging.md) | 764.42.9.0.0 | light |
| [`/System/Library/Frameworks/Messages.framework/Messages`](System__Library__Frameworks__Messages.framework__Messages.md) | 1491.200.101.21.5 | light |
| [`/System/Library/PrivateFrameworks/AssistantIsland.framework/AssistantIsland`](System__Library__PrivateFrameworks__AssistantIsland.framework__AssistantIsland.md) | 3605.10.2.11.9 | light |
| [`/System/Library/PrivateFrameworks/SiriActivationFoundation.framework/SiriActivationFoundation`](System__Library__PrivateFrameworks__SiriActivationFoundation.framework__SiriActivationFoundation.md) | 3605.23.2.3.0 | light |
| [`/System/Library/PrivateFrameworks/WorkflowUIServices.framework/WorkflowUIServices`](System__Library__PrivateFrameworks__WorkflowUIServices.framework__WorkflowUIServices.md) | 5114.0.12.0.0 | light |
| [`/System/Library/Frameworks/_AppIntents_SwiftUI.framework/_AppIntents_SwiftUI`](System__Library__Frameworks___AppIntents_SwiftUI.framework___AppIntents_SwiftUI.md) | 301.1.16.0.0 | light |
| [`/System/Library/Frameworks/PhotosUI.framework/PhotosUI`](System__Library__Frameworks__PhotosUI.framework__PhotosUI.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/_IconServices_SwiftUI.framework/_IconServices_SwiftUI`](System__Library__PrivateFrameworks___IconServices_SwiftUI.framework___IconServices_SwiftUI.md) | 793.1.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/SpotlightUIInternal.framework/SpotlightUIInternal`](System__Library__PrivateFrameworks__SpotlightUIInternal.framework__SpotlightUIInternal.md) | 250.1.12.200.0 | light |
| [`/System/Library/PrivateFrameworks/SpotlightUIShared.framework/SpotlightUIShared`](System__Library__PrivateFrameworks__SpotlightUIShared.framework__SpotlightUIShared.md) | 250.1.12.200.0 | light |
| [`/System/Library/Frameworks/DataDetection.framework/DataDetection`](System__Library__Frameworks__DataDetection.framework__DataDetection.md) | 852.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/GenerativePartnerService.framework/GenerativePartnerService`](System__Library__PrivateFrameworks__GenerativePartnerService.framework__GenerativePartnerService.md) | 297.12.4.0.0 | light |
| [`/System/Library/Frameworks/IntentsUI.framework/IntentsUI`](System__Library__Frameworks__IntentsUI.framework__IntentsUI.md) | 4016.1.16.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileTimerSupport.framework/MobileTimerSupport`](System__Library__PrivateFrameworks__MobileTimerSupport.framework__MobileTimerSupport.md) | 2333.2.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/WallpaperKit.framework/WallpaperKit`](System__Library__PrivateFrameworks__WallpaperKit.framework__WallpaperKit.md) | 2144.1.1.0.2 | light |
| [`/usr/lib/libBasebandCommandDriversARI.dylib`](usr__lib__libBasebandCommandDriversARI.dylib.md) | 1594.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection`](System__Library__PrivateFrameworks__PersistentConnection.framework__PersistentConnection.md) | 562.200.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleCV3D.framework/AppleCV3D`](System__Library__PrivateFrameworks__AppleCV3D.framework__AppleCV3D.md) | 9.26.7.9.0 | light |
| [`/System/Library/PrivateFrameworks/ContextKit.framework/ContextKit`](System__Library__PrivateFrameworks__ContextKit.framework__ContextKit.md) | 308.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MLAssetIO.framework/MLAssetIO`](System__Library__PrivateFrameworks__MLAssetIO.framework__MLAssetIO.md) | 3600.25.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/SpotlightIndex.framework/SpotlightIndex`](System__Library__PrivateFrameworks__SpotlightIndex.framework__SpotlightIndex.md) | 2465.1.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon`](System__Library__PrivateFrameworks__FileProviderDaemon.framework__FileProviderDaemon.md) | 4838.42.2.0.0 | light |
| [`/System/Library/AccessibilityBundles/CallsSearch.axbundle/CallsSearch`](System__Library__AccessibilityBundles__CallsSearch.axbundle__CallsSearch.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CallsAppUI.axbundle/CallsAppUI`](System__Library__AccessibilityBundles__CallsAppUI.axbundle__CallsAppUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground`](System__Library__PrivateFrameworks__LighthouseBackground.framework__LighthouseBackground.md) | 3.7.24.0.0 | light |
| [`/System/Library/PrivateFrameworks/SeymourClientServices.framework/SeymourClientServices`](System__Library__PrivateFrameworks__SeymourClientServices.framework__SeymourClientServices.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/ActivityRingsUI.framework/ActivityRingsUI`](System__Library__PrivateFrameworks__ActivityRingsUI.framework__ActivityRingsUI.md) | 2027.1.2.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend10.dylib`](usr__lib__objc__libobjcMsgSend10.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreNavigation.framework/CoreNavigation`](System__Library__PrivateFrameworks__CoreNavigation.framework__CoreNavigation.md) | 427.0.2.0.0 | light |
| [`/System/Library/Frameworks/WorkoutKit.framework/WorkoutKit`](System__Library__Frameworks__WorkoutKit.framework__WorkoutKit.md) | 2027.1.63.0.0 | light |
| [`/System/Library/AccessibilityBundles/HeadphoneCommonUIKit.axbundle/HeadphoneCommonUIKit`](System__Library__AccessibilityBundles__HeadphoneCommonUIKit.axbundle__HeadphoneCommonUIKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/HeadphoneCommonUIKit.framework/HeadphoneCommonUIKit`](System__Library__PrivateFrameworks__HeadphoneCommonUIKit.framework__HeadphoneCommonUIKit.md) | 41.7.0.0.0 | light |
| [`/System/Library/AccessibilityBundles/HearingModeUI.axbundle/HearingModeUI`](System__Library__AccessibilityBundles__HearingModeUI.axbundle__HearingModeUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/HealthExperienceUI.framework/HealthExperienceUI`](System__Library__PrivateFrameworks__HealthExperienceUI.framework__HealthExperienceUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthPlatform.framework/HealthPlatform`](System__Library__PrivateFrameworks__HealthPlatform.framework__HealthPlatform.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/FeedItemPlugins/MenstrualCyclesAppPlugin.healthplugin/MenstrualCyclesAppPlugin`](System__Library__Health__FeedItemPlugins__MenstrualCyclesAppPlugin.healthplugin__MenstrualCyclesAppPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/UserDomainConceptsSupport.framework/UserDomainConceptsSupport`](System__Library__PrivateFrameworks__UserDomainConceptsSupport.framework__UserDomainConceptsSupport.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthVisualization.framework/HealthVisualization`](System__Library__PrivateFrameworks__HealthVisualization.framework__HealthVisualization.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthRecordsUI.framework/HealthRecordsUI`](System__Library__PrivateFrameworks__HealthRecordsUI.framework__HealthRecordsUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI`](System__Library__PrivateFrameworks__HealthUI.framework__HealthUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/FeedItemPlugins/Summaries.healthplugin/Summaries`](System__Library__Health__FeedItemPlugins__Summaries.healthplugin__Summaries.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthPluginHost.framework/HealthPluginHost`](System__Library__PrivateFrameworks__HealthPluginHost.framework__HealthPluginHost.md) | 7027.1.56.6.5 | light |
| [`/System/Library/AccessibilityBundles/DMCEnrollmentProvider.axbundle/DMCEnrollmentProvider`](System__Library__AccessibilityBundles__DMCEnrollmentProvider.axbundle__DMCEnrollmentProvider.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/HomeDataModel.framework/HomeDataModel`](System__Library__PrivateFrameworks__HomeDataModel.framework__HomeDataModel.md) | 1269.2.5.6.6 | light |
| [`/System/Library/PrivateFrameworks/HomeServices.framework/HomeServices`](System__Library__PrivateFrameworks__HomeServices.framework__HomeServices.md) | 510.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/SymptomNetworkDiagnostics.framework/SymptomNetworkDiagnostics`](System__Library__PrivateFrameworks__SymptomNetworkDiagnostics.framework__SymptomNetworkDiagnostics.md) | 2394.40.17.0.0 | light |
| [`/System/Library/PrivateFrameworks/SymptomNetworkDiagnosticsCommon.framework/SymptomNetworkDiagnosticsCommon`](System__Library__PrivateFrameworks__SymptomNetworkDiagnosticsCommon.framework__SymptomNetworkDiagnosticsCommon.md) | 2394.40.17.0.0 | light |
| [`/System/Library/PrivateFrameworks/CopresenceCore.framework/CopresenceCore`](System__Library__PrivateFrameworks__CopresenceCore.framework__CopresenceCore.md) | 309.200.71.21.1 | light |
| [`/System/Library/Frameworks/GameController.framework/GameController`](System__Library__Frameworks__GameController.framework__GameController.md) | 14.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation`](System__Library__PrivateFrameworks__GameControllerFoundation.framework__GameControllerFoundation.md) | 14.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/AutoFillUI.framework/AutoFillUI`](System__Library__PrivateFrameworks__AutoFillUI.framework__AutoFillUI.md) | 114.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/RemoteTextInput.framework/RemoteTextInput`](System__Library__PrivateFrameworks__RemoteTextInput.framework__RemoteTextInput.md) | 180.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/VectorSearch.framework/VectorSearch`](System__Library__PrivateFrameworks__VectorSearch.framework__VectorSearch.md) | 53.0.0.0.0 | light |
| [`/System/Library/Frameworks/ManagedSettings.framework/ManagedSettings`](System__Library__Frameworks__ManagedSettings.framework__ManagedSettings.md) | 319.40.1.0.0 | light |
| [`/System/Library/Frameworks/EventKitUI.framework/EventKitUI`](System__Library__Frameworks__EventKitUI.framework__EventKitUI.md) | 1573.2.2.0.0 | light |
| [`/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI`](System__Library__Frameworks___MapKit_SwiftUI.framework___MapKit_SwiftUI.md) | 2552.31.6.17.115 | light |
| [`/System/Library/PrivateFrameworks/APFoundation.framework/APFoundation`](System__Library__PrivateFrameworks__APFoundation.framework__APFoundation.md) | 557.2.14.0.0 | light |
| [`/System/Library/AccessibilityBundles/CoverSheet.axbundle/CoverSheet`](System__Library__AccessibilityBundles__CoverSheet.axbundle__CoverSheet.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/EmojiKit.framework/EmojiKit`](System__Library__PrivateFrameworks__EmojiKit.framework__EmojiKit.md) | 44.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ManagedBackgroundAssetsXPC.framework/ManagedBackgroundAssetsXPC`](System__Library__PrivateFrameworks__ManagedBackgroundAssetsXPC.framework__ManagedBackgroundAssetsXPC.md) | 2.1.9.0.0 | light |
| [`/usr/lib/libMobileGestaltExtensions.dylib`](usr__lib__libMobileGestaltExtensions.dylib.md) | 1622.40.11.0.0 | full |
| [`/System/Library/PrivateFrameworks/MailSupport.framework/MailSupport`](System__Library__PrivateFrameworks__MailSupport.framework__MailSupport.md) | 3901.200.71.21.4 | light |
| [`/System/Library/PrivateFrameworks/EmailCore.framework/EmailCore`](System__Library__PrivateFrameworks__EmailCore.framework__EmailCore.md) | 3901.200.71.21.4 | light |
| [`/System/Library/PrivateFrameworks/MIME.framework/MIME`](System__Library__PrivateFrameworks__MIME.framework__MIME.md) | 3901.200.71.21.4 | light |
| [`/System/Library/PrivateFrameworks/MessageSupport.framework/MessageSupport`](System__Library__PrivateFrameworks__MessageSupport.framework__MessageSupport.md) | 3901.200.71.21.4 | light |
| [`/System/Library/Frameworks/PaperKit.framework/PaperKit`](System__Library__Frameworks__PaperKit.framework__PaperKit.md) | 384.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI`](System__Library__PrivateFrameworks__NotesUI.framework__NotesUI.md) | 3001.42.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/TextRecognition.framework/TextRecognition`](System__Library__PrivateFrameworks__TextRecognition.framework__TextRecognition.md) | 446.15.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/SonicKit.framework/SonicKit`](System__Library__PrivateFrameworks__SonicKit.framework__SonicKit.md) | 26210.26.40.301.0 | light |
| [`/System/Library/Frameworks/_GroupActivities_UIKit.framework/_GroupActivities_UIKit`](System__Library__Frameworks___GroupActivities_UIKit.framework___GroupActivities_UIKit.md) | 309.200.71.21.1 | light |
| [`/System/Library/Frameworks/MusicKit.framework/MusicKit`](System__Library__Frameworks__MusicKit.framework__MusicKit.md) | 4026.210.2.0.0 | light |
| [`/usr/lib/swift/libswiftAccelerate.dylib`](usr__lib__swift__libswiftAccelerate.dylib.md) | 82.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/TeaBreeze.framework/TeaBreeze`](System__Library__PrivateFrameworks__TeaBreeze.framework__TeaBreeze.md) | 1517.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NewsArticles.framework/NewsArticles`](System__Library__PrivateFrameworks__NewsArticles.framework__NewsArticles.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NewsFeed.framework/NewsFeed`](System__Library__PrivateFrameworks__NewsFeed.framework__NewsFeed.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NewsAds.framework/NewsAds`](System__Library__PrivateFrameworks__NewsAds.framework__NewsAds.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/SocialLayer.framework/SocialLayer`](System__Library__PrivateFrameworks__SocialLayer.framework__SocialLayer.md) | 217.200.51.0.0 | light |
| [`/System/Library/PrivateFrameworks/PoirotSQLite.framework/PoirotSQLite`](System__Library__PrivateFrameworks__PoirotSQLite.framework__PoirotSQLite.md) | 3605.11.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/PoirotUDFs.framework/PoirotUDFs`](System__Library__PrivateFrameworks__PoirotUDFs.framework__PoirotUDFs.md) | 3605.11.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AtomicsInternal.framework/AtomicsInternal`](System__Library__PrivateFrameworks__AtomicsInternal.framework__AtomicsInternal.md) | 5027.1.6.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend11.dylib`](usr__lib__objc__libobjcMsgSend11.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore`](System__Library__PrivateFrameworks__NewsCore.framework__NewsCore.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NewsSubscription.framework/NewsSubscription`](System__Library__PrivateFrameworks__NewsSubscription.framework__NewsSubscription.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/GameServices.framework/GameServices`](System__Library__PrivateFrameworks__GameServices.framework__GameServices.md) | 821.1.16.2.1 | light |
| [`/System/Library/PrivateFrameworks/NewsLiveActivitiesCore.framework/NewsLiveActivitiesCore`](System__Library__PrivateFrameworks__NewsLiveActivitiesCore.framework__NewsLiveActivitiesCore.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NewsPersonalization.framework/NewsPersonalization`](System__Library__PrivateFrameworks__NewsPersonalization.framework__NewsPersonalization.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AIMLInstrumentationStreams.framework/AIMLInstrumentationStreams`](System__Library__PrivateFrameworks__AIMLInstrumentationStreams.framework__AIMLInstrumentationStreams.md) | 3605.2.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/SiriPrivateLearningAnalytics`](System__Library__PrivateFrameworks__SiriPrivateLearningAnalytics.framework__SiriPrivateLearningAnalytics.md) | 3600.5.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowResponsiveness`](System__Library__PrivateFrameworks__WorkflowResponsiveness.framework__WorkflowResponsiveness.md) | 453.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence`](System__Library__PrivateFrameworks__PhotosIntelligence.framework__PhotosIntelligence.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/Leo.framework/Leo`](System__Library__PrivateFrameworks__Leo.framework__Leo.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/PodcastsFoundation.framework/PodcastsFoundation`](System__Library__PrivateFrameworks__PodcastsFoundation.framework__PodcastsFoundation.md) | 4027.210.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ChronoUIServices.framework/ChronoUIServices`](System__Library__PrivateFrameworks__ChronoUIServices.framework__ChronoUIServices.md) | 7749.2.13.0.3 | light |
| [`/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI`](System__Library__PrivateFrameworks__PaperBoardUI.framework__PaperBoardUI.md) | 355.2.12.0.4 | light |
| [`/System/Library/PrivateFrameworks/HeadphoneManager.framework/HeadphoneManager`](System__Library__PrivateFrameworks__HeadphoneManager.framework__HeadphoneManager.md) | 41.7.0.0.0 | light |
| [`/System/Library/Frameworks/AppManagedFeatures.framework/AppManagedFeatures`](System__Library__Frameworks__AppManagedFeatures.framework__AppManagedFeatures.md) | 58.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp`](System__Library__PrivateFrameworks__CoreFollowUp.framework__CoreFollowUp.md) | 2027.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/PromotedContentJetClient.framework/PromotedContentJetClient`](System__Library__PrivateFrameworks__PromotedContentJetClient.framework__PromotedContentJetClient.md) | 557.2.14.0.0 | light |
| [`/System/Library/PrivateFrameworks/ReminderKitInternal.framework/ReminderKitInternal`](System__Library__PrivateFrameworks__ReminderKitInternal.framework__ReminderKitInternal.md) | 4080.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics`](System__Library__PrivateFrameworks__SiriAnalytics.framework__SiriAnalytics.md) | 3605.33.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/FileProviderResolver.framework/FileProviderResolver`](System__Library__PrivateFrameworks__FileProviderResolver.framework__FileProviderResolver.md) | 4838.42.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth`](System__Library__PrivateFrameworks__MobileBluetooth.framework__MobileBluetooth.md) | 2701.7.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/SiriUI.framework/SiriUI`](System__Library__PrivateFrameworks__SiriUI.framework__SiriUI.md) | 3605.23.2.3.0 | light |
| [`/System/Library/PrivateFrameworks/AssistantUI.framework/AssistantUI`](System__Library__PrivateFrameworks__AssistantUI.framework__AssistantUI.md) | 3605.23.2.3.0 | light |
| [`/System/Library/PrivateFrameworks/ScreenshotServices.framework/ScreenshotServices`](System__Library__PrivateFrameworks__ScreenshotServices.framework__ScreenshotServices.md) | 452.1.3.100.0 | light |
| [`/System/Library/PrivateFrameworks/AXGuestPassServices.framework/AXGuestPassServices`](System__Library__PrivateFrameworks__AXGuestPassServices.framework__AXGuestPassServices.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer`](System__Library__PrivateFrameworks__HangTracer.framework__HangTracer.md) | 430.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) | 3600.26.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration`](System__Library__PrivateFrameworks__SiriCrossDeviceArbitration.framework__SiriCrossDeviceArbitration.md) | 3605.25.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ProactiveSummarizationClient.framework/ProactiveSummarizationClient`](System__Library__PrivateFrameworks__ProactiveSummarizationClient.framework__ProactiveSummarizationClient.md) | 1354.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus`](System__Library__PrivateFrameworks__SystemStatus.framework__SystemStatus.md) | 288.1.6.0.2 | light |
| [`/System/Library/PrivateFrameworks/MediaControl.framework/MediaControl`](System__Library__PrivateFrameworks__MediaControl.framework__MediaControl.md) | 4026.210.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntlPreferences.framework/IntlPreferences`](System__Library__PrivateFrameworks__IntlPreferences.framework__IntlPreferences.md) | 500.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore`](System__Library__PrivateFrameworks__UserNotificationsCore.framework__UserNotificationsCore.md) | 720.2.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/LocalStatusKit.framework/LocalStatusKit`](System__Library__PrivateFrameworks__LocalStatusKit.framework__LocalStatusKit.md) | 154.200.31.0.0 | light |
| [`/System/Library/PrivateFrameworks/StocksCore.framework/StocksCore`](System__Library__PrivateFrameworks__StocksCore.framework__StocksCore.md) | 2063.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) | 1072.4.0.0.0 | full |
| [`/usr/lib/swift/libswiftSystem.dylib`](usr__lib__swift__libswiftSystem.dylib.md) | 5027.0.67.0.0 | light |
| [`/System/Library/PrivateFrameworks/SwiftCRLite.framework/SwiftCRLite`](System__Library__PrivateFrameworks__SwiftCRLite.framework__SwiftCRLite.md) | 134.40.15.0.0 | light |
| [`/System/Library/PrivateFrameworks/WeatherAppSupport.framework/WeatherAppSupport`](System__Library__PrivateFrameworks__WeatherAppSupport.framework__WeatherAppSupport.md) | 1474.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/WeatherUI.framework/WeatherUI`](System__Library__PrivateFrameworks__WeatherUI.framework__WeatherUI.md) | 1474.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/WidgetRenderer.framework/WidgetRenderer`](System__Library__PrivateFrameworks__WidgetRenderer.framework__WidgetRenderer.md) | 7749.2.13.0.3 | light |
| [`/System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories`](System__Library__PrivateFrameworks__CoreAccessories.framework__CoreAccessories.md) | 1219.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/DataAccessExpress.framework/DataAccessExpress`](System__Library__PrivateFrameworks__DataAccessExpress.framework__DataAccessExpress.md) | 2708.2.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/CalendarDatabase.framework/CalendarDatabase`](System__Library__PrivateFrameworks__CalendarDatabase.framework__CalendarDatabase.md) | 1291.2.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate`](System__Library__PrivateFrameworks__CryptoKitPrivate.framework__CryptoKitPrivate.md) | 383.40.14.0.0 | light |
| [`/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`](System__Library__PrivateFrameworks__UnifiedAssetFramework.framework__UnifiedAssetFramework.md) | 3605.17.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine`](System__Library__PrivateFrameworks__DialogEngine.framework__DialogEngine.md) | 3605.10.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriKitRuntime.framework/SiriKitRuntime`](System__Library__PrivateFrameworks__SiriKitRuntime.framework__SiriKitRuntime.md) | 3605.22.1.11.1 | light |
| [`/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech`](System__Library__PrivateFrameworks__CoreSpeech.framework__CoreSpeech.md) | 3605.32.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities`](System__Library__PrivateFrameworks__SiriUtilities.framework__SiriUtilities.md) | 3600.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation`](System__Library__PrivateFrameworks__CDMFoundation.framework__CDMFoundation.md) | 3605.19.1.11.1 | light |
| [`/System/Library/PrivateFrameworks/AIMLExperimentationAnalytics.framework/AIMLExperimentationAnalytics`](System__Library__PrivateFrameworks__AIMLExperimentationAnalytics.framework__AIMLExperimentationAnalytics.md) | 3400.7.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) | 3605.32.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/FeatureStore.framework/FeatureStore`](System__Library__PrivateFrameworks__FeatureStore.framework__FeatureStore.md) | 3605.12.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/HAENotifications.framework/HAENotifications`](System__Library__PrivateFrameworks__HAENotifications.framework__HAENotifications.md) | 881.210.0.0.0 | light |
| [`/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib`](System__Library__Frameworks__AudioToolbox.framework__libAudioDSP.dylib.md) | 881.210.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AudioDSPGraph.framework/AudioDSPGraph`](System__Library__PrivateFrameworks__AudioDSPGraph.framework__AudioDSPGraph.md) | 73.201.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AVConference.framework/AVConference`](System__Library__PrivateFrameworks__AVConference.framework__AVConference.md) | 2263.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) | 2319.52.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage`](System__Library__PrivateFrameworks__BiomeStorage.framework__BiomeStorage.md) | 259.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ProactiveSuggestionClientModel.framework/ProactiveSuggestionClientModel`](System__Library__PrivateFrameworks__ProactiveSuggestionClientModel.framework__ProactiveSuggestionClientModel.md) | 678.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport`](System__Library__PrivateFrameworks__CrashReporterSupport.framework__CrashReporterSupport.md) | 14281.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreServicesStore.framework/CoreServicesStore`](System__Library__PrivateFrameworks__CoreServicesStore.framework__CoreServicesStore.md) | 1517.1.12.0.0 | light |
| [`/System/Library/PrivateFrameworks/WebPrivacy.framework/WebPrivacy`](System__Library__PrivateFrameworks__WebPrivacy.framework__WebPrivacy.md) | 61.0.0.0.0 | light |
| [`/System/Library/AccessibilityBundles/WebProcessLoader.axbundle/WebProcessLoader`](System__Library__AccessibilityBundles__WebProcessLoader.axbundle__WebProcessLoader.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`](System__Library__PrivateFrameworks__EmailDaemon.framework__EmailDaemon.md) | 3901.200.71.21.4 | light |
| [`/System/Library/PrivateFrameworks/PrivacyAccounting.framework/PrivacyAccounting`](System__Library__PrivateFrameworks__PrivacyAccounting.framework__PrivacyAccounting.md) | 150.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon`](System__Library__PrivateFrameworks__ContainerManagerCommon.framework__ContainerManagerCommon.md) | 833.40.18.0.1 | light |
| [`/usr/lib/system/libsystem_containermanager.dylib`](usr__lib__system__libsystem_containermanager.dylib.md) | 833.40.18.0.1 | light |
| [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) | 2701.7.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/CoreIDVShared.framework/CoreIDVShared`](System__Library__PrivateFrameworks__CoreIDVShared.framework__CoreIDVShared.md) | 9.108.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete`](System__Library__PrivateFrameworks__CacheDelete.framework__CacheDelete.md) | 904.40.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice`](System__Library__PrivateFrameworks__FindMyDevice.framework__FindMyDevice.md) | 482.31.6.16.21 | light |
| [`/System/Library/PrivateFrameworks/FindMyBluetooth.framework/FindMyBluetooth`](System__Library__PrivateFrameworks__FindMyBluetooth.framework__FindMyBluetooth.md) | 106.31.6.16.7 | full |
| [`/System/Library/PrivateFrameworks/FindMyServerInteraction.framework/FindMyServerInteraction`](System__Library__PrivateFrameworks__FindMyServerInteraction.framework__FindMyServerInteraction.md) | 106.31.6.16.7 | light |
| [`/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis`](System__Library__PrivateFrameworks__SampleAnalysis.framework__SampleAnalysis.md) | 441.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/SleepHealth.framework/SleepHealth`](System__Library__PrivateFrameworks__SleepHealth.framework__SleepHealth.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthOrchestration.framework/HealthOrchestration`](System__Library__PrivateFrameworks__HealthOrchestration.framework__HealthOrchestration.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/VisualGeneration.framework/VisualGeneration`](System__Library__PrivateFrameworks__VisualGeneration.framework__VisualGeneration.md) | 144.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics`](System__Library__PrivateFrameworks__InputAnalytics.framework__InputAnalytics.md) | 154.1.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/DataDeliveryServices.framework/DataDeliveryServices`](System__Library__PrivateFrameworks__DataDeliveryServices.framework__DataDeliveryServices.md) | 117.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CompanionSync.framework/CompanionSync`](System__Library__PrivateFrameworks__CompanionSync.framework__CompanionSync.md) | 279.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer`](System__Library__PrivateFrameworks__ProtocolBuffer.framework__ProtocolBuffer.md) | 326.31.9.18.102 | light |
| [`/usr/lib/system/libsystem_asl.dylib`](usr__lib__system__libsystem_asl.dylib.md) | 409.40.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/StreamingZip.framework/StreamingZip`](System__Library__PrivateFrameworks__StreamingZip.framework__StreamingZip.md) | 260.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ServiceDiscovery.framework/ServiceDiscovery`](System__Library__PrivateFrameworks__ServiceDiscovery.framework__ServiceDiscovery.md) | 751.200.101.0.0 | light |
| [`/System/Library/PrivateFrameworks/SpotlightKnowledge.framework/SpotlightKnowledge`](System__Library__PrivateFrameworks__SpotlightKnowledge.framework__SpotlightKnowledge.md) | 2465.1.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/Transparency.framework/Transparency`](System__Library__PrivateFrameworks__Transparency.framework__Transparency.md) | 1766.40.58.0.0 | light |
| [`/System/Library/PrivateFrameworks/SymptomNetworkDiagnosticsCore.framework/SymptomNetworkDiagnosticsCore`](System__Library__PrivateFrameworks__SymptomNetworkDiagnosticsCore.framework__SymptomNetworkDiagnosticsCore.md) | 2394.40.17.0.0 | light |
| [`/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomAnalytics.framework/SymptomAnalytics`](System__Library__PrivateFrameworks__Symptoms.framework__Frameworks__SymptomAnalytics.framework__SymptomAnalytics.md) | 2394.40.17.0.0 | light |
| [`/System/Library/PrivateFrameworks/Archetype.framework/Archetype`](System__Library__PrivateFrameworks__Archetype.framework__Archetype.md) | 41.14.0.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend12.dylib`](usr__lib__objc__libobjcMsgSend12.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligenceFlowProto.framework/IntelligenceFlowProto`](System__Library__PrivateFrameworks__IntelligenceFlowProto.framework__IntelligenceFlowProto.md) | 3605.22.501.11.0 | light |
| [`/System/Library/PrivateFrameworks/SpotlightKnowledgeDaemon.framework/SpotlightKnowledgeDaemon`](System__Library__PrivateFrameworks__SpotlightKnowledgeDaemon.framework__SpotlightKnowledgeDaemon.md) | 2465.1.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/AppleMediaDiscovery`](System__Library__PrivateFrameworks__AppleMediaDiscovery.framework__AppleMediaDiscovery.md) | 1.5.7.0.0 | light |
| [`/System/Library/Frameworks/RealityKit.framework/RealityKit`](System__Library__Frameworks__RealityKit.framework__RealityKit.md) | 453.42.1.0.1 | light |
| [`/System/Library/Frameworks/RealityFoundation.framework/RealityFoundation`](System__Library__Frameworks__RealityFoundation.framework__RealityFoundation.md) | 453.42.1.0.1 | light |
| [`/System/Library/PrivateFrameworks/AppStoreKit.framework/AppStoreKit`](System__Library__PrivateFrameworks__AppStoreKit.framework__AppStoreKit.md) | 27.1.24.1.0 | light |
| [`/System/Library/PrivateFrameworks/CoreRE.framework/CoreRE`](System__Library__PrivateFrameworks__CoreRE.framework__CoreRE.md) | 453.42.1.0.1 | light |
| [`/System/Library/AccessibilityBundles/AppStore.axbundle/AppStore`](System__Library__AccessibilityBundles__AppStore.axbundle__AppStore.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) | 162.16.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/GameCenterUI.framework/GameCenterUI`](System__Library__PrivateFrameworks__GameCenterUI.framework__GameCenterUI.md) | 821.1.16.2.1 | light |
| [`/System/Library/Frameworks/PHASE.framework/PHASE`](System__Library__Frameworks__PHASE.framework__PHASE.md) | 400.101.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ITMLKit.framework/ITMLKit`](System__Library__PrivateFrameworks__ITMLKit.framework__ITMLKit.md) | 651.10.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/MetricsFramework.framework/MetricsFramework`](System__Library__PrivateFrameworks__MetricsFramework.framework__MetricsFramework.md) | 3605.17.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ActionKit.framework/ActionKit`](System__Library__PrivateFrameworks__ActionKit.framework__ActionKit.md) | 5114.0.12.0.0 | light |
| [`/System/Library/PrivateFrameworks/FlowToolsRegistry.framework/FlowToolsRegistry`](System__Library__PrivateFrameworks__FlowToolsRegistry.framework__FlowToolsRegistry.md) | 3605.31.1.11.2 | light |
| [`/System/Library/PrivateFrameworks/BookFoundation.framework/BookFoundation`](System__Library__PrivateFrameworks__BookFoundation.framework__BookFoundation.md) | 2354.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/BookDataStore.framework/BookDataStore`](System__Library__PrivateFrameworks__BookDataStore.framework__BookDataStore.md) | 2354.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CalculateUI.framework/CalculateUI`](System__Library__PrivateFrameworks__CalculateUI.framework__CalculateUI.md) | 243.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CalendarPoster.framework/CalendarPoster`](System__Library__PrivateFrameworks__CalendarPoster.framework__CalendarPoster.md) | 415.2.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/CalendarWidget.framework/CalendarWidget`](System__Library__PrivateFrameworks__CalendarWidget.framework__CalendarWidget.md) | 415.2.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices`](System__Library__PrivateFrameworks__SpotlightServices.framework__SpotlightServices.md) | 2465.1.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/DictionaryServices.framework/DictionaryServices`](System__Library__PrivateFrameworks__DictionaryServices.framework__DictionaryServices.md) | 383.8.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AssistantIslandClient.framework/AssistantIslandClient`](System__Library__PrivateFrameworks__AssistantIslandClient.framework__AssistantIslandClient.md) | 3605.10.2.11.9 | light |
| [`/System/Library/PrivateFrameworks/AssistantActionSuggestionSupport.framework/AssistantActionSuggestionSupport`](System__Library__PrivateFrameworks__AssistantActionSuggestionSupport.framework__AssistantActionSuggestionSupport.md) | 678.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/Spotlight.framework/Spotlight`](System__Library__PrivateFrameworks__Spotlight.framework__Spotlight.md) | 2465.1.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/CampoUIInternal.framework/CampoUIInternal`](System__Library__PrivateFrameworks__CampoUIInternal.framework__CampoUIInternal.md) | 3605.10.2.11.9 | light |
| [`/System/Library/PrivateFrameworks/AgentCanvasUICore.framework/AgentCanvasUICore`](System__Library__PrivateFrameworks__AgentCanvasUICore.framework__AgentCanvasUICore.md) | 3605.10.2.11.9 | light |
| [`/System/Library/PrivateFrameworks/SpotlightUIServices.framework/SpotlightUIServices`](System__Library__PrivateFrameworks__SpotlightUIServices.framework__SpotlightUIServices.md) | 250.1.12.200.0 | light |
| [`/System/Library/Frameworks/CoreTransferable.framework/CoreTransferable`](System__Library__Frameworks__CoreTransferable.framework__CoreTransferable.md) | 8.0.39.0.0 | light |
| [`/System/Library/PrivateFrameworks/CampoServices.framework/CampoServices`](System__Library__PrivateFrameworks__CampoServices.framework__CampoServices.md) | 3605.10.2.11.9 | full |
| [`/System/Library/PrivateFrameworks/AssistantUICore.framework/AssistantUICore`](System__Library__PrivateFrameworks__AssistantUICore.framework__AssistantUICore.md) | 3605.10.2.11.9 | light |
| [`/System/Library/PrivateFrameworks/AgentCanvasFoundation.framework/AgentCanvasFoundation`](System__Library__PrivateFrameworks__AgentCanvasFoundation.framework__AgentCanvasFoundation.md) | 3605.10.2.11.9 | light |
| [`/System/Library/PrivateFrameworks/AgentCanvasUI.framework/AgentCanvasUI`](System__Library__PrivateFrameworks__AgentCanvasUI.framework__AgentCanvasUI.md) | 3605.10.2.11.9 | light |
| [`/System/Library/PrivateFrameworks/AgentCanvasPersistence.framework/AgentCanvasPersistence`](System__Library__PrivateFrameworks__AgentCanvasPersistence.framework__AgentCanvasPersistence.md) | 3605.10.2.11.9 | light |
| [`/System/Library/PrivateFrameworks/CampoMarkdown.framework/CampoMarkdown`](System__Library__PrivateFrameworks__CampoMarkdown.framework__CampoMarkdown.md) | 3605.10.2.11.9 | light |
| [`/System/Library/PrivateFrameworks/AgentCanvasKit.framework/AgentCanvasKit`](System__Library__PrivateFrameworks__AgentCanvasKit.framework__AgentCanvasKit.md) | 3605.10.2.11.9 | light |
| [`/System/Library/PrivateFrameworks/BubbleKit.framework/BubbleKit`](System__Library__PrivateFrameworks__BubbleKit.framework__BubbleKit.md) | 1491.200.101.21.5 | light |
| [`/System/Library/AccessibilityBundles/ClockPoster.axbundle/ClockPoster`](System__Library__AccessibilityBundles__ClockPoster.axbundle__ClockPoster.md) | 3050.3.8.0.0 | light |
| [`/usr/lib/libBasebandManagerICE.dylib`](usr__lib__libBasebandManagerICE.dylib.md) | 1594.0.0.0.0 | full |
| [`/usr/lib/libBBUpdaterDynamic.dylib`](usr__lib__libBBUpdaterDynamic.dylib.md) | 1594.0.0.0.0 | light |
| [`/usr/lib/libKTLDynamic.dylib`](usr__lib__libKTLDynamic.dylib.md) | 1594.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`](System__Library__PrivateFrameworks__IPTelephony.framework__Support__libIPTelephony.dylib.md) | 2774.0.0.0.0 | full |
| [`/System/Library/Frameworks/ExtensionKit.framework/ExtensionKit`](System__Library__Frameworks__ExtensionKit.framework__ExtensionKit.md) | 290.1.3.0.0 | light |
| [`/System/Library/Frameworks/ImagePlayground.framework/ImagePlayground`](System__Library__Frameworks__ImagePlayground.framework__ImagePlayground.md) | 198.2.12.600.0 | light |
| [`/System/Library/PrivateFrameworks/NeuralNetworks.framework/NeuralNetworks`](System__Library__PrivateFrameworks__NeuralNetworks.framework__NeuralNetworks.md) | 150.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/PredictedContextAlgorithms.framework/PredictedContextAlgorithms`](System__Library__PrivateFrameworks__PredictedContextAlgorithms.framework__PredictedContextAlgorithms.md) | 52.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust`](System__Library__PrivateFrameworks__OctagonTrust.framework__OctagonTrust.md) | 62460.40.78.0.0 | light |
| [`/System/Library/AccessibilityBundles/FaceTime.axbundle/FaceTime`](System__Library__AccessibilityBundles__FaceTime.axbundle__FaceTime.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/FedStatsPluginCore`](System__Library__PrivateFrameworks__FedStatsPluginCore.framework__FedStatsPluginCore.md) | 85.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesPriv`](System__Library__PrivateFrameworks__DesktopServicesPriv.framework__DesktopServicesPriv.md) | 1857.1.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/Fitness.framework/Fitness`](System__Library__PrivateFrameworks__Fitness.framework__Fitness.md) | 2027.1.27.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessBrowsing.framework/FitnessBrowsing`](System__Library__PrivateFrameworks__FitnessBrowsing.framework__FitnessBrowsing.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/WorkoutSeymourBridge.framework/WorkoutSeymourBridge`](System__Library__PrivateFrameworks__WorkoutSeymourBridge.framework__WorkoutSeymourBridge.md) | 2027.1.63.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessAppRoot.framework/FitnessAppRoot`](System__Library__PrivateFrameworks__FitnessAppRoot.framework__FitnessAppRoot.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessWorkoutPlan.framework/FitnessWorkoutPlan`](System__Library__PrivateFrameworks__FitnessWorkoutPlan.framework__FitnessWorkoutPlan.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessSchedule.framework/FitnessSchedule`](System__Library__PrivateFrameworks__FitnessSchedule.framework__FitnessSchedule.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessCoreUI.framework/FitnessCoreUI`](System__Library__PrivateFrameworks__FitnessCoreUI.framework__FitnessCoreUI.md) | 2027.1.69.0.0 | full |
| [`/System/Library/PrivateFrameworks/FitnessSearch.framework/FitnessSearch`](System__Library__PrivateFrameworks__FitnessSearch.framework__FitnessSearch.md) | 2027.1.69.0.0 | light |
| [`/System/Library/AccessibilityBundles/SeymourUI.axbundle/SeymourUI`](System__Library__AccessibilityBundles__SeymourUI.axbundle__SeymourUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessAsset.framework/FitnessAsset`](System__Library__PrivateFrameworks__FitnessAsset.framework__FitnessAsset.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/ActivityUI.framework/ActivityUI`](System__Library__PrivateFrameworks__ActivityUI.framework__ActivityUI.md) | 2027.1.27.0.0 | light |
| [`/System/Library/PrivateFrameworks/ActivityAchievementsUI.framework/ActivityAchievementsUI`](System__Library__PrivateFrameworks__ActivityAchievementsUI.framework__ActivityAchievementsUI.md) | 2027.1.4.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend13.dylib`](usr__lib__objc__libobjcMsgSend13.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/WorkoutUI.framework/WorkoutUI`](System__Library__PrivateFrameworks__WorkoutUI.framework__WorkoutUI.md) | 2027.1.63.0.0 | light |
| [`/System/Library/PrivateFrameworks/WorkoutCore.framework/WorkoutCore`](System__Library__PrivateFrameworks__WorkoutCore.framework__WorkoutCore.md) | 2027.1.63.0.0 | light |
| [`/System/Library/PrivateFrameworks/Blackbeard.framework/Blackbeard`](System__Library__PrivateFrameworks__Blackbeard.framework__Blackbeard.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessForYou.framework/FitnessForYou`](System__Library__PrivateFrameworks__FitnessForYou.framework__FitnessForYou.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/SeymourUI.framework/SeymourUI`](System__Library__PrivateFrameworks__SeymourUI.framework__SeymourUI.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/SeymourClient.framework/SeymourClient`](System__Library__PrivateFrameworks__SeymourClient.framework__SeymourClient.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/SeymourMedia.framework/SeymourMedia`](System__Library__PrivateFrameworks__SeymourMedia.framework__SeymourMedia.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/SafetyMonitorUI`](System__Library__PrivateFrameworks__SafetyMonitorUI.framework__SafetyMonitorUI.md) | 1123.0.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessActions.framework/FitnessActions`](System__Library__PrivateFrameworks__FitnessActions.framework__FitnessActions.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessSummary.framework/FitnessSummary`](System__Library__PrivateFrameworks__FitnessSummary.framework__FitnessSummary.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessCanvasUI.framework/FitnessCanvasUI`](System__Library__PrivateFrameworks__FitnessCanvasUI.framework__FitnessCanvasUI.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessSampleContent.framework/FitnessSampleContent`](System__Library__PrivateFrameworks__FitnessSampleContent.framework__FitnessSampleContent.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessLibrary.framework/FitnessLibrary`](System__Library__PrivateFrameworks__FitnessLibrary.framework__FitnessLibrary.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessCanvas.framework/FitnessCanvas`](System__Library__PrivateFrameworks__FitnessCanvas.framework__FitnessCanvas.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessMarketing.framework/FitnessMarketing`](System__Library__PrivateFrameworks__FitnessMarketing.framework__FitnessMarketing.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessIntelligenceDaemonCore.framework/FitnessIntelligenceDaemonCore`](System__Library__PrivateFrameworks__FitnessIntelligenceDaemonCore.framework__FitnessIntelligenceDaemonCore.md) | 2027.1.35.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessIntelligenceSnapshotting.framework/FitnessIntelligenceSnapshotting`](System__Library__PrivateFrameworks__FitnessIntelligenceSnapshotting.framework__FitnessIntelligenceSnapshotting.md) | 2027.1.35.0.0 | light |
| [`/System/Library/Frameworks/HealthKitUI.framework/HealthKitUI`](System__Library__Frameworks__HealthKitUI.framework__HealthKitUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthReportUI.framework/HealthReportUI`](System__Library__PrivateFrameworks__HealthReportUI.framework__HealthReportUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/AccessibilityBundles/HealthMedicationsUI.axbundle/HealthMedicationsUI`](System__Library__AccessibilityBundles__HealthMedicationsUI.axbundle__HealthMedicationsUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SleepHealthAppPlugin.axbundle/SleepHealthAppPlugin`](System__Library__AccessibilityBundles__SleepHealthAppPlugin.axbundle__SleepHealthAppPlugin.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/HealthToolbox.framework/HealthToolbox`](System__Library__PrivateFrameworks__HealthToolbox.framework__HealthToolbox.md) | 7027.1.56.6.5 | light |
| [`/System/Library/AccessibilityBundles/HearingTestUI.axbundle/HearingTestUI`](System__Library__AccessibilityBundles__HearingTestUI.axbundle__HearingTestUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MenstrualCyclesAppPlugin.axbundle/MenstrualCyclesAppPlugin`](System__Library__AccessibilityBundles__MenstrualCyclesAppPlugin.axbundle__MenstrualCyclesAppPlugin.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Home.axbundle/Home`](System__Library__AccessibilityBundles__Home.axbundle__Home.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/HomeUI2.framework/HomeUI2`](System__Library__PrivateFrameworks__HomeUI2.framework__HomeUI2.md) | 1269.2.5.6.6 | light |
| [`/System/Library/PrivateFrameworks/HomeEnergyUI.framework/HomeEnergyUI`](System__Library__PrivateFrameworks__HomeEnergyUI.framework__HomeEnergyUI.md) | 510.0.0.0.0 | light |
| [`/System/Library/Frameworks/EnergyKit.framework/EnergyKit`](System__Library__Frameworks__EnergyKit.framework__EnergyKit.md) | 510.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/EnergyKitFoundation.framework/EnergyKitFoundation`](System__Library__PrivateFrameworks__EnergyKitFoundation.framework__EnergyKitFoundation.md) | 510.0.0.0.0 | light |
| [`/System/Library/Frameworks/HomeExtensions.framework/HomeExtensions`](System__Library__Frameworks__HomeExtensions.framework__HomeExtensions.md) | 1269.2.5.6.6 | light |
| [`/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI`](System__Library__PrivateFrameworks__HomeUI.framework__HomeUI.md) | 1269.2.5.6.6 | light |
| [`/System/Library/PrivateFrameworks/EnergyKitInternal.framework/EnergyKitInternal`](System__Library__PrivateFrameworks__EnergyKitInternal.framework__EnergyKitInternal.md) | 510.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HomeUICommon.framework/HomeUICommon`](System__Library__PrivateFrameworks__HomeUICommon.framework__HomeUICommon.md) | 1269.2.5.6.6 | light |
| [`/System/Library/Frameworks/QuickLookThumbnailing.framework/QuickLookThumbnailing`](System__Library__Frameworks__QuickLookThumbnailing.framework__QuickLookThumbnailing.md) | 218.1.3.200.0 | light |
| [`/System/Library/PrivateFrameworks/CommunicationsUICore.framework/CommunicationsUICore`](System__Library__PrivateFrameworks__CommunicationsUICore.framework__CommunicationsUICore.md) | 158.200.81.21.9 | light |
| [`/System/Library/AccessibilityBundles/InCallService.axbundle/InCallService`](System__Library__AccessibilityBundles__InCallService.axbundle__InCallService.md) | 3050.3.8.0.0 | light |
| [`/System/Library/Frameworks/SharedWithYouCore.framework/SharedWithYouCore`](System__Library__Frameworks__SharedWithYouCore.framework__SharedWithYouCore.md) | 217.200.51.0.0 | light |
| [`/System/Library/PrivateFrameworks/ManagedBackgroundAssetsHelper.framework/ManagedBackgroundAssetsHelper`](System__Library__PrivateFrameworks__ManagedBackgroundAssetsHelper.framework__ManagedBackgroundAssetsHelper.md) | 2.1.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/MapsDesign.framework/MapsDesign`](System__Library__PrivateFrameworks__MapsDesign.framework__MapsDesign.md) | 82.31.6.17.14 | light |
| [`/System/Library/PrivateFrameworks/SearchAds.framework/SearchAds`](System__Library__PrivateFrameworks__SearchAds.framework__SearchAds.md) | 557.2.14.0.0 | light |
| [`/System/Library/PrivateFrameworks/APConfigurationSystem.framework/APConfigurationSystem`](System__Library__PrivateFrameworks__APConfigurationSystem.framework__APConfigurationSystem.md) | 557.2.14.0.0 | light |
| [`/System/Library/AccessibilityBundles/MapsUI.axbundle/MapsUI`](System__Library__AccessibilityBundles__MapsUI.axbundle__MapsUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Maps.axbundle/Maps`](System__Library__AccessibilityBundles__Maps.axbundle__Maps.md) | 3050.3.8.0.0 | light |
| [`/System/Library/Frameworks/NotificationCenter.framework/NotificationCenter`](System__Library__Frameworks__NotificationCenter.framework__NotificationCenter.md) | 308.0.0.0.0 | light |
| [`/System/Library/AccessibilityBundles/MobileCal.axbundle/MobileCal`](System__Library__AccessibilityBundles__MobileCal.axbundle__MobileCal.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/icloudMCCKit.framework/icloudMCCKit`](System__Library__PrivateFrameworks__icloudMCCKit.framework__icloudMCCKit.md) | 2027.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreSuggestionsUI.framework/CoreSuggestionsUI`](System__Library__PrivateFrameworks__CoreSuggestionsUI.framework__CoreSuggestionsUI.md) | 18.1.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/iCloudMailAssistant.framework/iCloudMailAssistant`](System__Library__PrivateFrameworks__iCloudMailAssistant.framework__iCloudMailAssistant.md) | 2027.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/MailUI.framework/MailUI`](System__Library__PrivateFrameworks__MailUI.framework__MailUI.md) | 3901.200.71.21.4 | light |
| [`/System/Library/AccessibilityBundles/MobileMail.axbundle/MobileMail`](System__Library__AccessibilityBundles__MobileMail.axbundle__MobileMail.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/NotesEditor.framework/NotesEditor`](System__Library__PrivateFrameworks__NotesEditor.framework__NotesEditor.md) | 3001.42.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/NotesUIServices.framework/NotesUIServices`](System__Library__PrivateFrameworks__NotesUIServices.framework__NotesUIServices.md) | 3001.42.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CallsAppServices.framework/CallsAppServices`](System__Library__PrivateFrameworks__CallsAppServices.framework__CallsAppServices.md) | 158.200.81.21.9 | light |
| [`/System/Library/PrivateFrameworks/CallsAppUI.framework/CallsAppUI`](System__Library__PrivateFrameworks__CallsAppUI.framework__CallsAppUI.md) | 158.200.81.21.9 | light |
| [`/System/Library/PrivateFrameworks/CallsSearch.framework/CallsSearch`](System__Library__PrivateFrameworks__CallsSearch.framework__CallsSearch.md) | 158.200.81.21.9 | light |
| [`/System/Library/AccessibilityBundles/MobilePhone.axbundle/MobilePhone`](System__Library__AccessibilityBundles__MobilePhone.axbundle__MobilePhone.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/CallsDialer.framework/CallsDialer`](System__Library__PrivateFrameworks__CallsDialer.framework__CallsDialer.md) | 158.200.81.21.9 | light |
| [`/System/Library/PrivateFrameworks/WebUI.framework/WebUI`](System__Library__PrivateFrameworks__WebUI.framework__WebUI.md) | 625.2.8.21.5 | light |
| [`/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI`](System__Library__PrivateFrameworks__MobileSafariUI.framework__MobileSafariUI.md) | 625.2.8.21.5 | light |
| [`/System/Library/PrivateFrameworks/SearchAssets.framework/SearchAssets`](System__Library__PrivateFrameworks__SearchAssets.framework__SearchAssets.md) | 3605.27.1.11.1 | light |
| [`/System/Library/AccessibilityBundles/MobileTimer.axbundle/MobileTimer`](System__Library__AccessibilityBundles__MobileTimer.axbundle__MobileTimer.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/MomentsUI.framework/MomentsUI`](System__Library__PrivateFrameworks__MomentsUI.framework__MomentsUI.md) | 502.0.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/MonogramPoster.framework/MonogramPoster`](System__Library__PrivateFrameworks__MonogramPoster.framework__MonogramPoster.md) | 1463.200.91.2.1 | light |
| [`/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/AppleMediaServicesUIDynamic`](System__Library__PrivateFrameworks__AppleMediaServicesUIDynamic.framework__AppleMediaServicesUIDynamic.md) | 8.1.23.2.2 | light |
| [`/System/Library/AccessibilityBundles/Music.axbundle/Music`](System__Library__AccessibilityBundles__Music.axbundle__Music.md) | 3050.3.8.0.0 | light |
| [`/System/Library/Frameworks/_MusicKit_SwiftUI.framework/_MusicKit_SwiftUI`](System__Library__Frameworks___MusicKit_SwiftUI.framework___MusicKit_SwiftUI.md) | 4026.210.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/MusicUI.framework/MusicUI`](System__Library__PrivateFrameworks__MusicUI.framework__MusicUI.md) | 4026.210.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/_MusicKitInternal_AppIntents.framework/_MusicKitInternal_AppIntents`](System__Library__PrivateFrameworks___MusicKitInternal_AppIntents.framework___MusicKitInternal_AppIntents.md) | 4026.210.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/_MusicKitInternal_SwiftUI`](System__Library__PrivateFrameworks___MusicKitInternal_SwiftUI.framework___MusicKitInternal_SwiftUI.md) | 4026.210.2.0.0 | light |
| [`/usr/lib/swift/libswiftObjectiveC.dylib`](usr__lib__swift__libswiftObjectiveC.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/SwiftMedia.framework/SwiftMedia`](System__Library__PrivateFrameworks__SwiftMedia.framework__SwiftMedia.md) | 70.10.1.1.0 | light |
| [`/System/Library/PrivateFrameworks/TeaDB.framework/TeaDB`](System__Library__PrivateFrameworks__TeaDB.framework__TeaDB.md) | 1517.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/RemoteConfiguration.framework/RemoteConfiguration`](System__Library__PrivateFrameworks__RemoteConfiguration.framework__RemoteConfiguration.md) | 424.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CookingSupport.framework/CookingSupport`](System__Library__PrivateFrameworks__CookingSupport.framework__CookingSupport.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ODDIFramework.framework/ODDIFramework`](System__Library__PrivateFrameworks__ODDIFramework.framework__ODDIFramework.md) | 3605.17.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/PaymentUIBase.framework/PaymentUIBase`](System__Library__PrivateFrameworks__PaymentUIBase.framework__PaymentUIBase.md) | 1696.2.9.2.0 | light |
| [`/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI`](System__Library__PrivateFrameworks__LocalAuthenticationPrivateUI.framework__LocalAuthenticationPrivateUI.md) | 2319.52.2.0.0 | full |
| [`/usr/lib/objc/libobjcMsgSend14.dylib`](usr__lib__objc__libobjcMsgSend14.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/libLLVM.dylib`](System__Library__PrivateFrameworks__GPUCompiler.framework__Versions__32023__Libraries__libLLVM.dylib.md) | 32023.922.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/CookingKit.framework/CookingKit`](System__Library__PrivateFrameworks__CookingKit.framework__CookingKit.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NewsAnalytics.framework/NewsAnalytics`](System__Library__PrivateFrameworks__NewsAnalytics.framework__NewsAnalytics.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleMediaServicesUIPaymentSheets.framework/AppleMediaServicesUIPaymentSheets`](System__Library__PrivateFrameworks__AppleMediaServicesUIPaymentSheets.framework__AppleMediaServicesUIPaymentSheets.md) | 8.1.23.2.2 | light |
| [`/System/Library/PrivateFrameworks/PassKitUIFoundation.framework/PassKitUIFoundation`](System__Library__PrivateFrameworks__PassKitUIFoundation.framework__PassKitUIFoundation.md) | 1696.2.9.2.0 | light |
| [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) | 3486.52.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport`](System__Library__PrivateFrameworks__SignpostSupport.framework__SignpostSupport.md) | 205.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/PhotosUIEdit.framework/PhotosUIEdit`](System__Library__PrivateFrameworks__PhotosUIEdit.framework__PhotosUIEdit.md) | 916.62.154.0.0 | light |
| [`/System/Library/AccessibilityBundles/PhotosFramework.axbundle/PhotosFramework`](System__Library__AccessibilityBundles__PhotosFramework.axbundle__PhotosFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/PhotoLibrary.framework/PhotoLibrary`](System__Library__PrivateFrameworks__PhotoLibrary.framework__PhotoLibrary.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/Tungsten.framework/Tungsten`](System__Library__PrivateFrameworks__Tungsten.framework__Tungsten.md) | 916.62.154.0.0 | light |
| [`/System/Library/AccessibilityBundles/VisionKitCore.axbundle/VisionKitCore`](System__Library__AccessibilityBundles__VisionKitCore.axbundle__VisionKitCore.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CameraEditKitFramework.axbundle/CameraEditKitFramework`](System__Library__AccessibilityBundles__CameraEditKitFramework.axbundle__CameraEditKitFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/PhotosPlayer.framework/PhotosPlayer`](System__Library__PrivateFrameworks__PhotosPlayer.framework__PhotosPlayer.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/GridZero.framework/GridZero`](System__Library__PrivateFrameworks__GridZero.framework__GridZero.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/PhotosGenerativeServices.framework/PhotosGenerativeServices`](System__Library__PrivateFrameworks__PhotosGenerativeServices.framework__PhotosGenerativeServices.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/PodcastsUI.framework/PodcastsUI`](System__Library__PrivateFrameworks__PodcastsUI.framework__PodcastsUI.md) | 4027.210.1.0.0 | light |
| [`/System/Library/AccessibilityBundles/PosterBoardFramework.axbundle/PosterBoardFramework`](System__Library__AccessibilityBundles__PosterBoardFramework.axbundle__PosterBoardFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard`](System__Library__PrivateFrameworks__PosterBoard.framework__PosterBoard.md) | 355.2.12.0.4 | light |
| [`/System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities`](System__Library__PrivateFrameworks__NetAppsUtilities.framework__NetAppsUtilities.md) | 108.0.0.0.0 | light |
| [`/System/Library/AccessibilityBundles/SIMSetupSupport.axbundle/SIMSetupSupport`](System__Library__AccessibilityBundles__SIMSetupSupport.axbundle__SIMSetupSupport.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit`](System__Library__PrivateFrameworks__UserNotificationsKit.framework__UserNotificationsKit.md) | 1077.2.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/Settings.framework/Settings`](System__Library__PrivateFrameworks__Settings.framework__Settings.md) | 2027.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/RemoteUI.framework/RemoteUI`](System__Library__PrivateFrameworks__RemoteUI.framework__RemoteUI.md) | 640.125.11.1.0 | light |
| [`/System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit`](System__Library__Frameworks__MarketplaceKit.framework__MarketplaceKit.md) | 4.1.15.0.0 | light |
| [`/System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings`](System__Library__PrivateFrameworks__Settings__SoundsAndHapticsSettings.framework__SoundsAndHapticsSettings.md) | 2027.0.3.600.0 | full |
| [`/System/Library/AccessibilityBundles/HeadphoneSettingsUI.axbundle/HeadphoneSettingsUI`](System__Library__AccessibilityBundles__HeadphoneSettingsUI.axbundle__HeadphoneSettingsUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/PreferencesExtended.framework/PreferencesExtended`](System__Library__PrivateFrameworks__PreferencesExtended.framework__PreferencesExtended.md) | 2027.0.1.0.0 | light |
| [`/System/Library/Frameworks/AccessoryNotifications.framework/AccessoryNotifications`](System__Library__Frameworks__AccessoryNotifications.framework__AccessoryNotifications.md) | 720.2.7.0.0 | full |
| [`/System/Library/PrivateFrameworks/AccountsUI.framework/AccountsUI`](System__Library__PrivateFrameworks__AccountsUI.framework__AccountsUI.md) | 370.0.0.0.0 | light |
| [`/System/Library/AccessibilityBundles/AppleAccountSettings.axbundle/AppleAccountSettings`](System__Library__AccessibilityBundles__AppleAccountSettings.axbundle__AppleAccountSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/ToneKit.framework/ToneKit`](System__Library__PrivateFrameworks__ToneKit.framework__ToneKit.md) | 675.0.0.0.0 | light |
| [`/System/Library/AccessibilityBundles/BatteryUsageUI.axbundle/BatteryUsageUI`](System__Library__AccessibilityBundles__BatteryUsageUI.axbundle__BatteryUsageUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/iCloudSettings.axbundle/iCloudSettings`](System__Library__AccessibilityBundles__iCloudSettings.axbundle__iCloudSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/Settings/GeneralSettingsUI.framework/GeneralSettingsUI`](System__Library__PrivateFrameworks__Settings__GeneralSettingsUI.framework__GeneralSettingsUI.md) | 2027.1.1.101.0 | light |
| [`/System/Library/PrivateFrameworks/SettingsHostUI.framework/SettingsHostUI`](System__Library__PrivateFrameworks__SettingsHostUI.framework__SettingsHostUI.md) | 2027.1.6.0.0 | light |
| [`/System/Library/AccessibilityBundles/HeadphoneConfigs.axbundle/HeadphoneConfigs`](System__Library__AccessibilityBundles__HeadphoneConfigs.axbundle__HeadphoneConfigs.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MobileMailSettings.axbundle/MobileMailSettings`](System__Library__AccessibilityBundles__MobileMailSettings.axbundle__MobileMailSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/BiometricKitUI.axbundle/BiometricKitUI`](System__Library__AccessibilityBundles__BiometricKitUI.axbundle__BiometricKitUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/DriverManagement.framework/DriverManagement`](System__Library__PrivateFrameworks__DriverManagement.framework__DriverManagement.md) | 514.40.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MailAccountSettings.axbundle/MailAccountSettings`](System__Library__AccessibilityBundles__MailAccountSettings.axbundle__MailAccountSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/DiagnosticsReporterServices.framework/DiagnosticsReporterServices`](System__Library__PrivateFrameworks__DiagnosticsReporterServices.framework__DiagnosticsReporterServices.md) | 1056.40.8.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend15.dylib`](usr__lib__objc__libobjcMsgSend15.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NewsUI2.framework/NewsUI2`](System__Library__PrivateFrameworks__NewsUI2.framework__NewsUI2.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HeadphoneSettingsUI.framework/HeadphoneSettingsUI`](System__Library__PrivateFrameworks__HeadphoneSettingsUI.framework__HeadphoneSettingsUI.md) | 41.7.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`](System__Library__PrivateFrameworks__SIMSetupSupport.framework__SIMSetupSupport.md) | 982.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/FamilyCircleUI.framework/FamilyCircleUI`](System__Library__PrivateFrameworks__FamilyCircleUI.framework__FamilyCircleUI.md) | 291.125.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/SettingsHost.framework/SettingsHost`](System__Library__PrivateFrameworks__SettingsHost.framework__SettingsHost.md) | 2027.1.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/PrivateMLClientInferenceProvider.framework/PrivateMLClientInferenceProvider`](System__Library__PrivateFrameworks__PrivateMLClientInferenceProvider.framework__PrivateMLClientInferenceProvider.md) | 218.9.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/PrivateMLClient.framework/PrivateMLClient`](System__Library__PrivateFrameworks__PrivateMLClient.framework__PrivateMLClient.md) | 218.9.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/PromotedContentJetSupport.framework/PromotedContentJetSupport`](System__Library__PrivateFrameworks__PromotedContentJetSupport.framework__PromotedContentJetSupport.md) | 557.2.14.0.0 | light |
| [`/System/Library/PrivateFrameworks/RemindersUICore.framework/RemindersUICore`](System__Library__PrivateFrameworks__RemindersUICore.framework__RemindersUICore.md) | 4080.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices`](System__Library__PrivateFrameworks__AppIntentsServices.framework__AppIntentsServices.md) | 41.1.16.1.103 | light |
| [`/System/Library/PrivateFrameworks/RemindersAppIntents.framework/RemindersAppIntents`](System__Library__PrivateFrameworks__RemindersAppIntents.framework__RemindersAppIntents.md) | 4080.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics`](System__Library__PrivateFrameworks__CoreDiagnostics.framework__CoreDiagnostics.md) | 83.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ScreenTimeSwift.framework/ScreenTimeSwift`](System__Library__PrivateFrameworks__ScreenTimeSwift.framework__ScreenTimeSwift.md) | 655.1.14.1.0 | light |
| [`/System/Library/PrivateFrameworks/ScreenTimeSettingsFoundation.framework/ScreenTimeSettingsFoundation`](System__Library__PrivateFrameworks__ScreenTimeSettingsFoundation.framework__ScreenTimeSettingsFoundation.md) | 97.1.14.0.0 | light |
| [`/System/Library/PrivateFrameworks/PoirotBlocks.framework/PoirotBlocks`](System__Library__PrivateFrameworks__PoirotBlocks.framework__PoirotBlocks.md) | 3605.11.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/PoirotSchematizer.framework/PoirotSchematizer`](System__Library__PrivateFrameworks__PoirotSchematizer.framework__PoirotSchematizer.md) | 3605.11.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/SearchOnDeviceAnalytics.framework/SearchOnDeviceAnalytics`](System__Library__PrivateFrameworks__SearchOnDeviceAnalytics.framework__SearchOnDeviceAnalytics.md) | 3605.27.1.11.1 | light |
| [`/System/Library/PrivateFrameworks/SeymourAsset.framework/SeymourAsset`](System__Library__PrivateFrameworks__SeymourAsset.framework__SeymourAsset.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/SeymourMetrics.framework/SeymourMetrics`](System__Library__PrivateFrameworks__SeymourMetrics.framework__SeymourMetrics.md) | 2027.1.69.0.0 | light |
| [`/System/Library/AccessibilityBundles/Siri.axbundle/Siri`](System__Library__AccessibilityBundles__Siri.axbundle__Siri.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriTurnRestatement.framework/SiriTurnRestatement`](System__Library__PrivateFrameworks__SiriTurnRestatement.framework__SiriTurnRestatement.md) | 3605.17.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/DeepThoughtBiomeFoundation.framework/DeepThoughtBiomeFoundation`](System__Library__PrivateFrameworks__DeepThoughtBiomeFoundation.framework__DeepThoughtBiomeFoundation.md) | 6.1.3.0.0 | light |
| [`/usr/lib/libmis.dylib`](usr__lib__libmis.dylib.md) | 487.0.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/SpringBoardUI.framework/SpringBoardUI`](System__Library__PrivateFrameworks__SpringBoardUI.framework__SpringBoardUI.md) | 4637.1.14.102.9 | light |
| [`/System/Library/AccessibilityBundles/ControlCenterUI.axbundle/ControlCenterUI`](System__Library__AccessibilityBundles__ControlCenterUI.axbundle__ControlCenterUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ReplayKitModule.axbundle/ReplayKitModule`](System__Library__AccessibilityBundles__ReplayKitModule.axbundle__ReplayKitModule.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriUIActivation.framework/SiriUIActivation`](System__Library__PrivateFrameworks__SiriUIActivation.framework__SiriUIActivation.md) | 3605.23.2.3.0 | light |
| [`/System/Library/PrivateFrameworks/VoiceServices.framework/VoiceServices`](System__Library__PrivateFrameworks__VoiceServices.framework__VoiceServices.md) | 3600.12.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/MaterialKit.framework/MaterialKit`](System__Library__PrivateFrameworks__MaterialKit.framework__MaterialKit.md) | 226.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/GamePolicy.framework/GamePolicy`](System__Library__PrivateFrameworks__GamePolicy.framework__GamePolicy.md) | 4.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit`](System__Library__PrivateFrameworks__UserNotificationsUIKit.framework__UserNotificationsUIKit.md) | 1077.2.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/SystemStatusUI.framework/SystemStatusUI`](System__Library__PrivateFrameworks__SystemStatusUI.framework__SystemStatusUI.md) | 288.1.6.0.2 | light |
| [`/System/Library/AccessibilityBundles/ConnectivityModule.axbundle/ConnectivityModule`](System__Library__AccessibilityBundles__ConnectivityModule.axbundle__ConnectivityModule.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/PrototypeTools.framework/PrototypeTools`](System__Library__PrivateFrameworks__PrototypeTools.framework__PrototypeTools.md) | 165.1.2.0.0 | light |
| [`/System/Library/Frameworks/AudioToolbox.framework/libEmbeddedSystemAUs.dylib`](System__Library__Frameworks__AudioToolbox.framework__libEmbeddedSystemAUs.dylib.md) | 1638.215.0.0.0 | full |
| [`/System/Library/AccessibilityBundles/SystemUIWindowingKit.axbundle/SystemUIWindowingKit`](System__Library__AccessibilityBundles__SystemUIWindowingKit.axbundle__SystemUIWindowingKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/KeyboardArbiter.framework/KeyboardArbiter`](System__Library__PrivateFrameworks__KeyboardArbiter.framework__KeyboardArbiter.md) | 9127.1.13.13.0 | light |
| [`/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI`](System__Library__PrivateFrameworks__ControlCenterUI.framework__ControlCenterUI.md) | 704.2.4.0.3 | light |
| [`/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet`](System__Library__PrivateFrameworks__CoverSheet.framework__CoverSheet.md) | 159.2.5.0.6 | light |
| [`/System/Library/PrivateFrameworks/ShellSceneKit.framework/ShellSceneKit`](System__Library__PrivateFrameworks__ShellSceneKit.framework__ShellSceneKit.md) | 54.1.4.200.0 | light |
| [`/System/Library/AccessibilityBundles/SpringBoard.axbundle/SpringBoard`](System__Library__AccessibilityBundles__SpringBoard.axbundle__SpringBoard.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/SystemUIDisplayUtilities.framework/SystemUIDisplayUtilities`](System__Library__PrivateFrameworks__SystemUIDisplayUtilities.framework__SystemUIDisplayUtilities.md) | 104.100.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/ControlCenterUIServices.framework/ControlCenterUIServices`](System__Library__PrivateFrameworks__ControlCenterUIServices.framework__ControlCenterUIServices.md) | 704.2.4.0.3 | light |
| [`/System/Library/PrivateFrameworks/UserNotificationsServices.framework/UserNotificationsServices`](System__Library__PrivateFrameworks__UserNotificationsServices.framework__UserNotificationsServices.md) | 720.2.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) | 4637.1.14.102.9 | full |
| [`/System/Library/AccessibilityBundles/AudioConferenceControlCenterModule.axbundle/AudioConferenceControlCenterModule`](System__Library__AccessibilityBundles__AudioConferenceControlCenterModule.axbundle__AudioConferenceControlCenterModule.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/SpringBoardDisplay.framework/SpringBoardDisplay`](System__Library__PrivateFrameworks__SpringBoardDisplay.framework__SpringBoardDisplay.md) | 41.100.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AXSpringBoardServerInstance.framework/AXSpringBoardServerInstance`](System__Library__PrivateFrameworks__AXSpringBoardServerInstance.framework__AXSpringBoardServerInstance.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) | 6.1.6.0.0 | full |
| [`/System/Library/PrivateFrameworks/AppRestrictionsCore.framework/AppRestrictionsCore`](System__Library__PrivateFrameworks__AppRestrictionsCore.framework__AppRestrictionsCore.md) | 22.2.2.100.0 | light |
| [`/System/Library/PrivateFrameworks/AppRestrictions.framework/AppRestrictions`](System__Library__PrivateFrameworks__AppRestrictions.framework__AppRestrictions.md) | 22.2.2.100.0 | light |
| [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) | 6.1.6.0.0 | full |
| [`/System/Library/PrivateFrameworks/PointerUIServices.framework/PointerUIServices`](System__Library__PrivateFrameworks__PointerUIServices.framework__PointerUIServices.md) | 172.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ControlCenterUIKit.framework/ControlCenterUIKit`](System__Library__PrivateFrameworks__ControlCenterUIKit.framework__ControlCenterUIKit.md) | 704.2.4.0.3 | light |
| [`/System/Library/PrivateFrameworks/NearField.framework/NearField`](System__Library__PrivateFrameworks__NearField.framework__NearField.md) | 371.8.0.0.0 | light |
| [`/usr/lib/libapp_launch_measurement.dylib`](usr__lib__libapp_launch_measurement.dylib.md) | 32.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer`](System__Library__PrivateFrameworks__UserNotificationsServer.framework__UserNotificationsServer.md) | 720.2.7.0.0 | light |
| [`/System/Library/AccessibilityBundles/VideoConferenceControlCenterModule.axbundle/VideoConferenceControlCenterModule`](System__Library__AccessibilityBundles__VideoConferenceControlCenterModule.axbundle__VideoConferenceControlCenterModule.md) | 3050.3.8.0.0 | light |
| [`/usr/lib/swift/libswiftDistributed.dylib`](usr__lib__swift__libswiftDistributed.dylib.md) | 6.4.2.1.9 | light |
| [`/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore`](System__Library__PrivateFrameworks__StatusKitAgentCore.framework__StatusKitAgentCore.md) | 154.200.31.0.0 | light |
| [`/System/Library/AccessibilityBundles/StickersUI.axbundle/StickersUI`](System__Library__AccessibilityBundles__StickersUI.axbundle__StickersUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/Frameworks/StickerKit.framework/StickerKit`](System__Library__Frameworks__StickerKit.framework__StickerKit.md) | 152.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/TeaCharts.framework/TeaCharts`](System__Library__PrivateFrameworks__TeaCharts.framework__TeaCharts.md) | 1517.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/StocksUI.framework/StocksUI`](System__Library__PrivateFrameworks__StocksUI.framework__StocksUI.md) | 2063.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/StocksPersonalization.framework/StocksPersonalization`](System__Library__PrivateFrameworks__StocksPersonalization.framework__StocksPersonalization.md) | 2063.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/StocksAnalytics.framework/StocksAnalytics`](System__Library__PrivateFrameworks__StocksAnalytics.framework__StocksAnalytics.md) | 2063.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/UnilogTelemetry.framework/UnilogTelemetry`](System__Library__PrivateFrameworks__UnilogTelemetry.framework__UnilogTelemetry.md) | 3600.14.2.0.0 | light |
| [`/usr/lib/system/libsystem_dnssd.dylib`](usr__lib__system__libsystem_dnssd.dylib.md) | 3111.40.45.0.0 | light |
| [`/System/Library/PrivateFrameworks/WeatherMaps.framework/WeatherMaps`](System__Library__PrivateFrameworks__WeatherMaps.framework__WeatherMaps.md) | 1474.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/WeatherAnalytics.framework/WeatherAnalytics`](System__Library__PrivateFrameworks__WeatherAnalytics.framework__WeatherAnalytics.md) | 1474.0.0.0.0 | light |
| [`/System/Library/Frameworks/_PhotosUI_WidgetKit.framework/_PhotosUI_WidgetKit`](System__Library__Frameworks___PhotosUI_WidgetKit.framework___PhotosUI_WidgetKit.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccessoryAssistiveTouch.framework/AccessoryAssistiveTouch`](System__Library__PrivateFrameworks__AccessoryAssistiveTouch.framework__AccessoryAssistiveTouch.md) | 1219.52.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/AccessoryBLEPairing.framework/AccessoryBLEPairing`](System__Library__PrivateFrameworks__AccessoryBLEPairing.framework__AccessoryBLEPairing.md) | 1219.52.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/AccessoryNavigation.framework/AccessoryNavigation`](System__Library__PrivateFrameworks__AccessoryNavigation.framework__AccessoryNavigation.md) | 1219.52.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/AccessoryCommunications.framework/AccessoryCommunications`](System__Library__PrivateFrameworks__AccessoryCommunications.framework__AccessoryCommunications.md) | 1219.52.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/AccessoryNowPlaying.framework/AccessoryNowPlaying`](System__Library__PrivateFrameworks__AccessoryNowPlaying.framework__AccessoryNowPlaying.md) | 1219.52.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/AccessoryOOBBTPairing.framework/AccessoryOOBBTPairing`](System__Library__PrivateFrameworks__AccessoryOOBBTPairing.framework__AccessoryOOBBTPairing.md) | 1219.52.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/AccessoryHID.framework/AccessoryHID`](System__Library__PrivateFrameworks__AccessoryHID.framework__AccessoryHID.md) | 1219.52.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/AccessoryMediaLibrary.framework/AccessoryMediaLibrary`](System__Library__PrivateFrameworks__AccessoryMediaLibrary.framework__AccessoryMediaLibrary.md) | 1219.52.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/ActivitySharingServices.framework/ActivitySharingServices`](System__Library__PrivateFrameworks__ActivitySharingServices.framework__ActivitySharingServices.md) | 2027.1.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/AgentSessionKitRuntime.framework/AgentSessionKitRuntime`](System__Library__PrivateFrameworks__AgentSessionKitRuntime.framework__AgentSessionKitRuntime.md) | 297.12.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport`](System__Library__PrivateFrameworks__AirPlaySupport.framework__AirPlaySupport.md) | 1005.13.1.1.0 | light |
| [`/System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI`](System__Library__PrivateFrameworks__AuthKitUI.framework__AuthKitUI.md) | 560.125.6.1.0 | light |
| [`/System/Library/PrivateFrameworks/ServicesAnalyticsDaemon.framework/ServicesAnalyticsDaemon`](System__Library__PrivateFrameworks__ServicesAnalyticsDaemon.framework__ServicesAnalyticsDaemon.md) | 3.1.15.0.0 | light |
| [`/System/Library/PrivateFrameworks/OnDeviceStorageDaemon.framework/OnDeviceStorageDaemon`](System__Library__PrivateFrameworks__OnDeviceStorageDaemon.framework__OnDeviceStorageDaemon.md) | 3.1.15.0.0 | light |
| [`/System/Library/PrivateFrameworks/AnnounceDaemon.framework/AnnounceDaemon`](System__Library__PrivateFrameworks__AnnounceDaemon.framework__AnnounceDaemon.md) | 340.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/VisualLocalization.framework/VisualLocalization`](System__Library__PrivateFrameworks__VisualLocalization.framework__VisualLocalization.md) | 105.31.9.20.102 | light |
| [`/System/Library/PrivateFrameworks/ALUtil.framework/ALUtil.dylib`](System__Library__PrivateFrameworks__ALUtil.framework__ALUtil.dylib.md) | 131.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppPlaceholderSync.framework/AppPlaceholderSync`](System__Library__PrivateFrameworks__AppPlaceholderSync.framework__AppPlaceholderSync.md) | 54.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/DMCApps.framework/DMCApps`](System__Library__PrivateFrameworks__DMCApps.framework__DMCApps.md) | 113.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppState.framework/AppState`](System__Library__PrivateFrameworks__AppState.framework__AppState.md) | 4.0.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppStoreComponentsDaemonKit.framework/AppStoreComponentsDaemonKit`](System__Library__PrivateFrameworks__AppStoreComponentsDaemonKit.framework__AppStoreComponentsDaemonKit.md) | 27.1.12.0.0 | light |
| [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) | 341.40.12.0.0 | full |
| [`/System/Library/PrivateFrameworks/MediaConversionService.framework/MediaConversionService`](System__Library__PrivateFrameworks__MediaConversionService.framework__MediaConversionService.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/PhotosIntelligenceCore.framework/PhotosIntelligenceCore`](System__Library__PrivateFrameworks__PhotosIntelligenceCore.framework__PhotosIntelligenceCore.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/Marrs.framework/Marrs`](System__Library__PrivateFrameworks__Marrs.framework__Marrs.md) | 3605.2.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriSuggestionsAPI.framework/SiriSuggestionsAPI`](System__Library__PrivateFrameworks__SiriSuggestionsAPI.framework__SiriSuggestionsAPI.md) | 3605.7.1.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend16.dylib`](usr__lib__objc__libobjcMsgSend16.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreODIEssentials.framework/CoreODIEssentials`](System__Library__PrivateFrameworks__CoreODIEssentials.framework__CoreODIEssentials.md) | 27.2.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriNaturalLanguageParsing.framework/SiriNaturalLanguageParsing`](System__Library__PrivateFrameworks__SiriNaturalLanguageParsing.framework__SiriNaturalLanguageParsing.md) | 3605.12.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriDialogEngine.framework/SiriDialogEngine`](System__Library__PrivateFrameworks__SiriDialogEngine.framework__SiriDialogEngine.md) | 3605.4.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriPrivateLearningInference.framework/SiriPrivateLearningInference`](System__Library__PrivateFrameworks__SiriPrivateLearningInference.framework__SiriPrivateLearningInference.md) | 3600.5.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriReferenceResolution.framework/SiriReferenceResolution`](System__Library__PrivateFrameworks__SiriReferenceResolution.framework__SiriReferenceResolution.md) | 3500.13.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriInformationSearch.framework/SiriInformationSearch`](System__Library__PrivateFrameworks__SiriInformationSearch.framework__SiriInformationSearch.md) | 3605.24.1.11.2 | light |
| [`/System/Library/PrivateFrameworks/SiriKitFlow.framework/SiriKitFlow`](System__Library__PrivateFrameworks__SiriKitFlow.framework__SiriKitFlow.md) | 3605.22.1.11.1 | light |
| [`/System/Library/PrivateFrameworks/SiriRequestDispatcher.framework/SiriRequestDispatcher`](System__Library__PrivateFrameworks__SiriRequestDispatcher.framework__SiriRequestDispatcher.md) | 3605.26.1.11.1 | full |
| [`/System/Library/PrivateFrameworks/SiriAnnouncePlatformOpportuneSpeaking.framework/SiriAnnouncePlatformOpportuneSpeaking`](System__Library__PrivateFrameworks__SiriAnnouncePlatformOpportuneSpeaking.framework__SiriAnnouncePlatformOpportuneSpeaking.md) | 3600.26.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriMessageBus.framework/SiriMessageBus`](System__Library__PrivateFrameworks__SiriMessageBus.framework__SiriMessageBus.md) | 3605.26.1.11.1 | light |
| [`/System/Library/PrivateFrameworks/GenerativeAssistantSettings.framework/GenerativeAssistantSettings`](System__Library__PrivateFrameworks__GenerativeAssistantSettings.framework__GenerativeAssistantSettings.md) | 3605.4.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriInCall.framework/SiriInCall`](System__Library__PrivateFrameworks__SiriInCall.framework__SiriInCall.md) | 3400.14.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriObservation.framework/SiriObservation`](System__Library__PrivateFrameworks__SiriObservation.framework__SiriObservation.md) | 3605.31.1.11.2 | light |
| [`/System/Library/PrivateFrameworks/MorphunAssets.framework/MorphunAssets`](System__Library__PrivateFrameworks__MorphunAssets.framework__MorphunAssets.md) | 3600.36.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/RequestDispatcherBridges.framework/RequestDispatcherBridges`](System__Library__PrivateFrameworks__RequestDispatcherBridges.framework__RequestDispatcherBridges.md) | 3605.26.1.11.1 | full |
| [`/System/Library/PrivateFrameworks/SiriMessageTypes.framework/SiriMessageTypes`](System__Library__PrivateFrameworks__SiriMessageTypes.framework__SiriMessageTypes.md) | 3605.7.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriTurnTakingManager.framework/SiriTurnTakingManager`](System__Library__PrivateFrameworks__SiriTurnTakingManager.framework__SiriTurnTakingManager.md) | 3605.4.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriCore.framework/SiriCore`](System__Library__PrivateFrameworks__SiriCore.framework__SiriCore.md) | 3500.6.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriCrossDeviceArbitrationFeedback.framework/SiriCrossDeviceArbitrationFeedback`](System__Library__PrivateFrameworks__SiriCrossDeviceArbitrationFeedback.framework__SiriCrossDeviceArbitrationFeedback.md) | 3605.25.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ATFoundation.framework/ATFoundation`](System__Library__PrivateFrameworks__ATFoundation.framework__ATFoundation.md) | 4026.200.21.0.0 | light |
| [`/System/Library/PrivateFrameworks/AirTrafficDevice.framework/AirTrafficDevice`](System__Library__PrivateFrameworks__AirTrafficDevice.framework__AirTrafficDevice.md) | 4026.200.21.0.0 | light |
| [`/System/Library/PrivateFrameworks/AudioAnalyticsExternal.framework/AudioAnalyticsExternal`](System__Library__PrivateFrameworks__AudioAnalyticsExternal.framework__AudioAnalyticsExternal.md) | 300.205.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/AudioAnalyticsBase`](System__Library__PrivateFrameworks__AudioAnalyticsBase.framework__AudioAnalyticsBase.md) | 300.205.0.0.0 | light |
| [`/System/Library/Frameworks/CoreAudio.framework/CoreAudio`](System__Library__Frameworks__CoreAudio.framework__CoreAudio.md) | 482.208.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/VoiceProcessor.framework/VoiceProcessor`](System__Library__PrivateFrameworks__VoiceProcessor.framework__VoiceProcessor.md) | 85.107.0.0.0 | light |
| [`/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`](System__Library__Frameworks__CoreHaptics.framework__CoreHaptics.md) | 293.200.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AudioDSPManager.framework/AudioDSPManager`](System__Library__PrivateFrameworks__AudioDSPManager.framework__AudioDSPManager.md) | 241.206.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AudioSession.framework/libSessionUtility.dylib`](System__Library__PrivateFrameworks__AudioSession.framework__libSessionUtility.dylib.md) | 449.207.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/TimeSync.framework/TimeSync`](System__Library__PrivateFrameworks__TimeSync.framework__TimeSync.md) | 1510.9.0.0.0 | light |
| [`/System/Library/VideoDecoders/AVD.videodecoder`](System__Library__VideoDecoders__AVD.videodecoder.md) | 995.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace`](System__Library__PrivateFrameworks__AVConference.framework__Frameworks__ViceroyTrace.framework__ViceroyTrace.md) | 2263.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/VideoProcessing.framework/VideoProcessing`](System__Library__PrivateFrameworks__VideoProcessing.framework__VideoProcessing.md) | 1415.6.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/TextToSpeechVoiceBankingSupport`](System__Library__PrivateFrameworks__TextToSpeechVoiceBankingSupport.framework__TextToSpeechVoiceBankingSupport.md) | 727.3.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/AXAssetLoader.framework/AXAssetLoader`](System__Library__PrivateFrameworks__AXAssetLoader.framework__AXAssetLoader.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) | 2300.52.5.0.0 | full |
| [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) | 877.2.2.600.0 | full |
| [`/System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer`](System__Library__PrivateFrameworks__IOMobileFramebuffer.framework__IOMobileFramebuffer.md) | 700.50.112.6.0 | full |
| [`/System/Library/AccessibilityBundles/BackBoard.axbundle/BackBoard`](System__Library__AccessibilityBundles__BackBoard.axbundle__BackBoard.md) | 3050.3.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) | 877.2.2.600.0 | full |
| [`/System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices`](System__Library__PrivateFrameworks__GraphicsServices.framework__GraphicsServices.md) | 9127.0.78.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup`](System__Library__PrivateFrameworks__MobileBackup.framework__MobileBackup.md) | 3039.42.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/BiomeDSL.framework/BiomeDSL`](System__Library__PrivateFrameworks__BiomeDSL.framework__BiomeDSL.md) | 259.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CloudKitDistributedSync.framework/CloudKitDistributedSync`](System__Library__PrivateFrameworks__CloudKitDistributedSync.framework__CloudKitDistributedSync.md) | 2720.17.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/CalendarIntegrationSupport.framework/CalendarIntegrationSupport`](System__Library__PrivateFrameworks__CalendarIntegrationSupport.framework__CalendarIntegrationSupport.md) | 1246.2.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/PhoneAppIntents.framework/PhoneAppIntents`](System__Library__PrivateFrameworks__PhoneAppIntents.framework__PhoneAppIntents.md) | 1628.200.81.21.4 | light |
| [`/System/Library/PrivateFrameworks/Portrait.framework/Portrait`](System__Library__PrivateFrameworks__Portrait.framework__Portrait.md) | 560.40.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/CarKitNavigation.framework/CarKitNavigation`](System__Library__PrivateFrameworks__CarKitNavigation.framework__CarKitNavigation.md) | 807.4.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP`](System__Library__PrivateFrameworks__CoreCDP.framework__CoreCDP.md) | 448.125.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/ChronoCore.framework/ChronoCore`](System__Library__PrivateFrameworks__ChronoCore.framework__ChronoCore.md) | 7749.2.13.0.3 | light |
| [`/System/Library/PrivateFrameworks/CipherML.framework/CipherML`](System__Library__PrivateFrameworks__CipherML.framework__CipherML.md) | 383.40.16.0.0 | light |
| [`/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon`](System__Library__PrivateFrameworks__CloudKitDaemon.framework__CloudKitDaemon.md) | 2720.17.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreSVG.framework/CoreSVG`](System__Library__PrivateFrameworks__CoreSVG.framework__CoreSVG.md) | 362.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/WebGPU.framework/WebGPU`](System__Library__PrivateFrameworks__WebGPU.framework__WebGPU.md) | 625.2.8.21.2 | light |
| [`/System/Library/PrivateFrameworks/QuickLookSupport.framework/QuickLookSupport`](System__Library__PrivateFrameworks__QuickLookSupport.framework__QuickLookSupport.md) | 218.1.3.200.0 | light |
| [`/System/Library/PrivateFrameworks/ContactsDonation.framework/ContactsDonation`](System__Library__PrivateFrameworks__ContactsDonation.framework__ContactsDonation.md) | 1130.200.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/Synapse.framework/Synapse`](System__Library__PrivateFrameworks__Synapse.framework__Synapse.md) | 149.0.0.0.0 | light |
| [`/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils`](System__Library__Frameworks__LocalAuthentication.framework__Support__SharedUtils.framework__SharedUtils.md) | 2319.52.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition`](System__Library__PrivateFrameworks__CoreEmbeddedSpeechRecognition.framework__CoreEmbeddedSpeechRecognition.md) | 3605.14.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/MapsSuggestions.framework/MapsSuggestions`](System__Library__PrivateFrameworks__MapsSuggestions.framework__MapsSuggestions.md) | 2972.31.6.17.137 | light |
| [`/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity`](System__Library__PrivateFrameworks__DeviceIdentity.framework__DeviceIdentity.md) | 1145.40.5.0.4 | full |
| [`/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal`](System__Library__PrivateFrameworks__AppAttestInternal.framework__AppAttestInternal.md) | 158.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DeviceSharing.framework/DeviceSharing`](System__Library__PrivateFrameworks__DeviceSharing.framework__DeviceSharing.md) | 40.0.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement`](System__Library__PrivateFrameworks__DeviceManagement.framework__DeviceManagement.md) | 267.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy`](System__Library__PrivateFrameworks__DifferentialPrivacy.framework__DifferentialPrivacy.md) | 800.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/SmartStackReplication.framework/SmartStackReplication`](System__Library__PrivateFrameworks__SmartStackReplication.framework__SmartStackReplication.md) | 350.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppPredictionFoundation.framework/AppPredictionFoundation`](System__Library__PrivateFrameworks__AppPredictionFoundation.framework__AppPredictionFoundation.md) | 678.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ActionPredictionHeuristicsInternal.framework/ActionPredictionHeuristicsInternal`](System__Library__PrivateFrameworks__ActionPredictionHeuristicsInternal.framework__ActionPredictionHeuristicsInternal.md) | 678.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal`](System__Library__PrivateFrameworks__AppPredictionInternal.framework__AppPredictionInternal.md) | 678.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AssistantActionSuggestionCore.framework/AssistantActionSuggestionCore`](System__Library__PrivateFrameworks__AssistantActionSuggestionCore.framework__AssistantActionSuggestionCore.md) | 678.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/FaceTimeMessageStore`](System__Library__PrivateFrameworks__FaceTimeMessageStore.framework__FaceTimeMessageStore.md) | 1628.200.81.21.4 | light |
| [`/System/Library/PrivateFrameworks/FileIndexerDaemon.framework/FileIndexerDaemon`](System__Library__PrivateFrameworks__FileIndexerDaemon.framework__FileIndexerDaemon.md) | 4838.42.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/FinanceDaemon.framework/FinanceDaemon`](System__Library__PrivateFrameworks__FinanceDaemon.framework__FinanceDaemon.md) | 376.1.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/FindMyDaemonSupport.framework/FindMyDaemonSupport`](System__Library__PrivateFrameworks__FindMyDaemonSupport.framework__FindMyDaemonSupport.md) | 106.31.6.16.7 | light |
| [`/System/Library/PrivateFrameworks/SeymourServices.framework/SeymourServices`](System__Library__PrivateFrameworks__SeymourServices.framework__SeymourServices.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/SeymourServicesCore.framework/SeymourServicesCore`](System__Library__PrivateFrameworks__SeymourServicesCore.framework__SeymourServicesCore.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/SeymourSessionServices.framework/SeymourSessionServices`](System__Library__PrivateFrameworks__SeymourSessionServices.framework__SeymourSessionServices.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/GameServicesCore.framework/GameServicesCore`](System__Library__PrivateFrameworks__GameServicesCore.framework__GameServicesCore.md) | 821.1.16.2.1 | light |
| [`/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation`](System__Library__PrivateFrameworks__GameCenterFoundation.framework__GameCenterFoundation.md) | 821.1.16.2.1 | light |
| [`/System/Library/PrivateFrameworks/RapidResourceDelivery.framework/RapidResourceDelivery`](System__Library__PrivateFrameworks__RapidResourceDelivery.framework__RapidResourceDelivery.md) | 3605.5.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/GenerativeExperiencesRuntime`](System__Library__PrivateFrameworks__GenerativeExperiencesRuntime.framework__GenerativeExperiencesRuntime.md) | 297.12.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/HealthPlatformFoundation.framework/HealthPlatformFoundation`](System__Library__PrivateFrameworks__HealthPlatformFoundation.framework__HealthPlatformFoundation.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthBalanceAppPlugin.framework/HealthBalanceAppPlugin`](System__Library__PrivateFrameworks__HealthBalanceAppPlugin.framework__HealthBalanceAppPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthAppHealthDaemonSupport.framework/HealthAppHealthDaemonSupport`](System__Library__PrivateFrameworks__HealthAppHealthDaemonSupport.framework__HealthAppHealthDaemonSupport.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/FeedItemPlugins/Safety.healthplugin/Safety`](System__Library__Health__FeedItemPlugins__Safety.healthplugin__Safety.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/FeedItemPlugins/SleepHealthAppPlugin.healthplugin/SleepHealthAppPlugin`](System__Library__Health__FeedItemPlugins__SleepHealthAppPlugin.healthplugin__SleepHealthAppPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/FeedItemPlugins/HearingAppPlugin.healthplugin/HearingAppPlugin`](System__Library__Health__FeedItemPlugins__HearingAppPlugin.healthplugin__HearingAppPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/MedicationsHealthAppPlugin.framework/MedicationsHealthAppPlugin`](System__Library__PrivateFrameworks__MedicationsHealthAppPlugin.framework__MedicationsHealthAppPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/FeedItemPlugins/HealthRecords.healthplugin/HealthRecords`](System__Library__Health__FeedItemPlugins__HealthRecords.healthplugin__HealthRecords.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HighlightAlerts.framework/HighlightAlerts`](System__Library__PrivateFrameworks__HighlightAlerts.framework__HighlightAlerts.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/HealthMedicationsUI`](System__Library__PrivateFrameworks__HealthMedicationsUI.framework__HealthMedicationsUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthPlatformCore.framework/HealthPlatformCore`](System__Library__PrivateFrameworks__HealthPlatformCore.framework__HealthPlatformCore.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthMedicationsExperience.framework/HealthMedicationsExperience`](System__Library__PrivateFrameworks__HealthMedicationsExperience.framework__HealthMedicationsExperience.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/Sleep.framework/Sleep`](System__Library__PrivateFrameworks__Sleep.framework__Sleep.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthContentDaemon.framework/HealthContentDaemon`](System__Library__PrivateFrameworks__HealthContentDaemon.framework__HealthContentDaemon.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthTopicsDaemonPlugin.framework/HealthTopicsDaemonPlugin`](System__Library__PrivateFrameworks__HealthTopicsDaemonPlugin.framework__HealthTopicsDaemonPlugin.md) | 7027.1.56.6.5 | light |
| [`/usr/lib/objc/libobjcMsgSend17.dylib`](usr__lib__objc__libobjcMsgSend17.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/Health/FeedItemPlugins/Heart.healthplugin/Heart`](System__Library__Health__FeedItemPlugins__Heart.healthplugin__Heart.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthDomains.framework/HealthDomains`](System__Library__PrivateFrameworks__HealthDomains.framework__HealthDomains.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthTopicsDaemon.framework/HealthTopicsDaemon`](System__Library__PrivateFrameworks__HealthTopicsDaemon.framework__HealthTopicsDaemon.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/SleepHealthDaemon.framework/SleepHealthDaemon`](System__Library__PrivateFrameworks__SleepHealthDaemon.framework__SleepHealthDaemon.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthReportHealthDaemon.framework/HealthReportHealthDaemon`](System__Library__PrivateFrameworks__HealthReportHealthDaemon.framework__HealthReportHealthDaemon.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/SurveyKitDaemon.framework/SurveyKitDaemon`](System__Library__PrivateFrameworks__SurveyKitDaemon.framework__SurveyKitDaemon.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthBalanceDaemon.framework/HealthBalanceDaemon`](System__Library__PrivateFrameworks__HealthBalanceDaemon.framework__HealthBalanceDaemon.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthAppHealthDaemon.framework/HealthAppHealthDaemon`](System__Library__PrivateFrameworks__HealthAppHealthDaemon.framework__HealthAppHealthDaemon.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthRecordsPlugin.framework/HealthRecordsPlugin`](System__Library__PrivateFrameworks__HealthRecordsPlugin.framework__HealthRecordsPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthDaemonFeatures.framework/HealthDaemonFeatures`](System__Library__PrivateFrameworks__HealthDaemonFeatures.framework__HealthDaemonFeatures.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon`](System__Library__PrivateFrameworks__HealthDaemon.framework__HealthDaemon.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon`](System__Library__PrivateFrameworks__HealthMenstrualCyclesDaemon.framework__HealthMenstrualCyclesDaemon.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthOntologyDaemonPlugin.framework/HealthOntologyDaemonPlugin`](System__Library__PrivateFrameworks__HealthOntologyDaemonPlugin.framework__HealthOntologyDaemonPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation`](System__Library__PrivateFrameworks__HealthDaemonFoundation.framework__HealthDaemonFoundation.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthHistoryDaemon.framework/HealthHistoryDaemon`](System__Library__PrivateFrameworks__HealthHistoryDaemon.framework__HealthHistoryDaemon.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthOntologyKit.framework/HealthOntologyKit`](System__Library__PrivateFrameworks__HealthOntologyKit.framework__HealthOntologyKit.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthRecordsDaemon.framework/HealthRecordsDaemon`](System__Library__PrivateFrameworks__HealthRecordsDaemon.framework__HealthRecordsDaemon.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/LiveTranscription.framework/LiveTranscription`](System__Library__PrivateFrameworks__LiveTranscription.framework__LiveTranscription.md) | 591.4.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/HomeKitBackingStore.framework/HomeKitBackingStore`](System__Library__PrivateFrameworks__HomeKitBackingStore.framework__HomeKitBackingStore.md) | 1520.2.7.1.3 | light |
| [`/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter`](System__Library__PrivateFrameworks__HomeKitMatter.framework__HomeKitMatter.md) | 1520.2.7.1.3 | light |
| [`/System/Library/PrivateFrameworks/HomeKitFeatures.framework/HomeKitFeatures`](System__Library__PrivateFrameworks__HomeKitFeatures.framework__HomeKitFeatures.md) | 1520.2.7.1.3 | light |
| [`/System/Library/PrivateFrameworks/HomeKitMetrics.framework/HomeKitMetrics`](System__Library__PrivateFrameworks__HomeKitMetrics.framework__HomeKitMetrics.md) | 1520.2.7.1.3 | light |
| [`/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon`](System__Library__PrivateFrameworks__HomeKitDaemon.framework__HomeKitDaemon.md) | 1520.2.7.1.3 | light |
| [`/System/Library/PrivateFrameworks/HomeKitEventRouter.framework/HomeKitEventRouter`](System__Library__PrivateFrameworks__HomeKitEventRouter.framework__HomeKitEventRouter.md) | 1520.2.7.1.3 | light |
| [`/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP`](System__Library__PrivateFrameworks__CoreHAP.framework__CoreHAP.md) | 1520.2.7.1.3 | light |
| [`/System/Library/PrivateFrameworks/HomeKitEvents.framework/HomeKitEvents`](System__Library__PrivateFrameworks__HomeKitEvents.framework__HomeKitEvents.md) | 1520.2.7.1.3 | light |
| [`/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/HomeEnergyDaemon`](System__Library__PrivateFrameworks__HomeEnergyDaemon.framework__HomeEnergyDaemon.md) | 510.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HybridSearchRuntime.framework/HybridSearchRuntime`](System__Library__PrivateFrameworks__HybridSearchRuntime.framework__HybridSearchRuntime.md) | 73.3.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/HybridDatabase.framework/HybridDatabase`](System__Library__PrivateFrameworks__HybridDatabase.framework__HybridDatabase.md) | 60.3.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerDaemon.framework/iCloudSubscriptionOptimizerDaemon`](System__Library__PrivateFrameworks__iCloudSubscriptionOptimizerDaemon.framework__iCloudSubscriptionOptimizerDaemon.md) | 74.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation`](System__Library__PrivateFrameworks__IconFoundation.framework__IconFoundation.md) | 793.1.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/MessagesSecurityPolicy.framework/MessagesSecurityPolicy`](System__Library__PrivateFrameworks__MessagesSecurityPolicy.framework__MessagesSecurityPolicy.md) | 1491.200.101.21.5 | light |
| [`/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore`](System__Library__PrivateFrameworks__IMDaemonCore.framework__IMDaemonCore.md) | 1491.200.101.21.5 | light |
| [`/System/Library/PrivateFrameworks/TrustKit.framework/TrustKit`](System__Library__PrivateFrameworks__TrustKit.framework__TrustKit.md) | 106.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/PairedSync.framework/PairedSync`](System__Library__PrivateFrameworks__PairedSync.framework__PairedSync.md) | 197.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ImageGenerationServices.framework/ImageGenerationServices`](System__Library__PrivateFrameworks__ImageGenerationServices.framework__ImageGenerationServices.md) | 198.2.12.600.0 | light |
| [`/System/Library/PrivateFrameworks/SuggestedImage.framework/SuggestedImage`](System__Library__PrivateFrameworks__SuggestedImage.framework__SuggestedImage.md) | 198.2.12.600.0 | light |
| [`/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer`](System__Library__PrivateFrameworks__InputAnalyticsServer.framework__InputAnalyticsServer.md) | 154.1.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/IntelligenceFlowContextRuntime`](System__Library__PrivateFrameworks__IntelligenceFlowContextRuntime.framework__IntelligenceFlowContextRuntime.md) | 3605.22.501.11.0 | light |
| [`/System/Library/PrivateFrameworks/UIIntelligenceSupportAgent.framework/UIIntelligenceSupportAgent`](System__Library__PrivateFrameworks__UIIntelligenceSupportAgent.framework__UIIntelligenceSupportAgent.md) | 9127.1.13.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/IntelligenceFlowPlannerSupport`](System__Library__PrivateFrameworks__IntelligenceFlowPlannerSupport.framework__IntelligenceFlowPlannerSupport.md) | 3605.22.501.11.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligenceFlowShared.framework/IntelligenceFlowShared`](System__Library__PrivateFrameworks__IntelligenceFlowShared.framework__IntelligenceFlowShared.md) | 3605.22.501.11.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligenceFlow.framework/IntelligenceFlow`](System__Library__PrivateFrameworks__IntelligenceFlow.framework__IntelligenceFlow.md) | 3605.22.501.11.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligenceTasksEngine.framework/IntelligenceTasksEngine`](System__Library__PrivateFrameworks__IntelligenceTasksEngine.framework__IntelligenceTasksEngine.md) | 259.0.0.0.0 | light |
| [`/usr/lib/system/libsystem_darwin.dylib`](usr__lib__system__libsystem_darwin.dylib.md) | 1786.40.6.0.0 | light |
| [`/usr/lib/system/libsystem_kernel.dylib`](usr__lib__system__libsystem_kernel.dylib.md) | 13432.52.2.0.0 | light |
| [`/usr/lib/system/libsystem_featureflags.dylib`](usr__lib__system__libsystem_featureflags.dylib.md) | 111.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/SessionFoundation.framework/SessionFoundation`](System__Library__PrivateFrameworks__SessionFoundation.framework__SessionFoundation.md) | 313.2.9.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend18.dylib`](usr__lib__objc__libobjcMsgSend18.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/IntelligenceFlowPlannerRuntime`](System__Library__PrivateFrameworks__IntelligenceFlowPlannerRuntime.framework__IntelligenceFlowPlannerRuntime.md) | 3605.22.501.11.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/IntelligenceFlowRuntime`](System__Library__PrivateFrameworks__IntelligenceFlowRuntime.framework__IntelligenceFlowRuntime.md) | 3605.22.501.11.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligentRoutingDaemon.framework/IntelligentRoutingDaemon`](System__Library__PrivateFrameworks__IntelligentRoutingDaemon.framework__IntelligentRoutingDaemon.md) | 125.1.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/JetCore.framework/JetCore`](System__Library__PrivateFrameworks__JetCore.framework__JetCore.md) | 10.1.11.0.0 | light |
| [`/System/Library/PrivateFrameworks/LanguageModeling.framework/LanguageModeling`](System__Library__PrivateFrameworks__LanguageModeling.framework__LanguageModeling.md) | 449.3.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore`](System__Library__PrivateFrameworks__TextInputCore.framework__TextInputCore.md) | 3568.1.8.600.0 | light |
| [`/System/Library/PrivateFrameworks/GRDBv7Internal.framework/GRDBv7Internal`](System__Library__PrivateFrameworks__GRDBv7Internal.framework__GRDBv7Internal.md) | 19.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppIntentsIndex.framework/AppIntentsIndex`](System__Library__PrivateFrameworks__AppIntentsIndex.framework__AppIntentsIndex.md) | 301.1.16.0.0 | light |
| [`/System/Library/PrivateFrameworks/SessionCore.framework/SessionCore`](System__Library__PrivateFrameworks__SessionCore.framework__SessionCore.md) | 313.2.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/CarouselPreferenceServices.framework/CarouselPreferenceServices`](System__Library__PrivateFrameworks__CarouselPreferenceServices.framework__CarouselPreferenceServices.md) | 1115.1.11.0.0 | light |
| [`/System/Library/PrivateFrameworks/SessionPushNotifications.framework/SessionPushNotifications`](System__Library__PrivateFrameworks__SessionPushNotifications.framework__SessionPushNotifications.md) | 313.2.9.0.0 | light |
| [`/System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory`](System__Library__Frameworks__ExternalAccessory.framework__ExternalAccessory.md) | 462.40.2.0.0 | full |
| [`/usr/lib/libARI.dylib`](usr__lib__libARI.dylib.md) | 1640.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) | 107.0.26.0.0 | full |
| [`/System/Library/PrivateFrameworks/CoreGPS.framework/CoreGPS.dylib`](System__Library__PrivateFrameworks__CoreGPS.framework__CoreGPS.dylib.md) | 367.0.2.0.0 | full |
| [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](System__Library__Frameworks__SensorKit.framework__SensorKit.md) | 1039.0.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/IAP.framework/IAP`](System__Library__PrivateFrameworks__IAP.framework__IAP.md) | 2186.40.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/LocationAuthorizationFramework.framework/LocationAuthorizationFramework`](System__Library__PrivateFrameworks__LocationAuthorizationFramework.framework__LocationAuthorizationFramework.md) | 3187.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AONSense.framework/AONSense.dylib`](System__Library__PrivateFrameworks__AONSense.framework__AONSense.dylib.md) | 131.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) | 33.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/LocationSupport.framework/LocationSupport`](System__Library__PrivateFrameworks__LocationSupport.framework__LocationSupport.md) | 3187.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain`](System__Library__PrivateFrameworks__RegulatoryDomain.framework__RegulatoryDomain.md) | 74.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreTime.framework/CoreTime`](System__Library__PrivateFrameworks__CoreTime.framework__CoreTime.md) | 340.0.14.0.0 | light |
| [`/System/Library/PrivateFrameworks/LockdownMode.framework/LockdownMode`](System__Library__PrivateFrameworks__LockdownMode.framework__LockdownMode.md) | 128.40.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/StatusKit.framework/StatusKit`](System__Library__PrivateFrameworks__StatusKit.framework__StatusKit.md) | 154.200.31.0.0 | light |
| [`/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis`](System__Library__PrivateFrameworks__MediaAnalysis.framework__MediaAnalysis.md) | 460.14.1.2.0 | light |
| [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray`](System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNDArray.framework__MPSNDArray.md) | 130.1.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/VisionCore.framework/VisionCore`](System__Library__PrivateFrameworks__VisionCore.framework__VisionCore.md) | 10.1.7.0.0 | light |
| [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) | 7.1.5.0.0 | full |
| [`/System/Library/PrivateFrameworks/VisualLookUp.framework/VisualLookUp`](System__Library__PrivateFrameworks__VisualLookUp.framework__VisualLookUp.md) | 6.0.13.0.0 | light |
| [`/usr/lib/system/libsystem_symptoms.dylib`](usr__lib__system__libsystem_symptoms.dylib.md) | 2394.40.17.0.0 | light |
| [`/usr/lib/libusrtcp.dylib`](usr__lib__libusrtcp.dylib.md) | 6681.52.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreMediaSwiftUpwardLinkingTrampoline.framework/CoreMediaSwiftUpwardLinkingTrampoline`](System__Library__PrivateFrameworks__CoreMediaSwiftUpwardLinkingTrampoline.framework__CoreMediaSwiftUpwardLinkingTrampoline.md) | 3385.14.1.3.0 | light |
| [`/System/Library/PrivateFrameworks/NearbySessions.framework/NearbySessions`](System__Library__PrivateFrameworks__NearbySessions.framework__NearbySessions.md) | 309.200.71.21.1 | full |
| [`/System/Library/PrivateFrameworks/IntelligentRoutingMediaBundles.framework/IntelligentRoutingMediaBundles`](System__Library__PrivateFrameworks__IntelligentRoutingMediaBundles.framework__IntelligentRoutingMediaBundles.md) | 125.1.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/ProximityReaderDaemon.framework/ProximityReaderDaemon`](System__Library__PrivateFrameworks__ProximityReaderDaemon.framework__ProximityReaderDaemon.md) | 151.6.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileAssetDaemon.framework/MobileAssetDaemon`](System__Library__PrivateFrameworks__MobileAssetDaemon.framework__MobileAssetDaemon.md) | 2215.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`](System__Library__PrivateFrameworks__CoreRepairCore.framework__CoreRepairCore.md) | 1307.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/ModelCatalogRuntime`](System__Library__PrivateFrameworks__ModelCatalogRuntime.framework__ModelCatalogRuntime.md) | 308.12.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MediaStream.framework/MediaStream`](System__Library__PrivateFrameworks__MediaStream.framework__MediaStream.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync`](System__Library__PrivateFrameworks__NanoPreferencesSync.framework__NanoPreferencesSync.md) | 334.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry`](System__Library__PrivateFrameworks__NanoRegistry.framework__NanoRegistry.md) | 1075.16.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoTimeKit.framework/NanoTimeKit`](System__Library__PrivateFrameworks__NanoTimeKit.framework__NanoTimeKit.md) | 2483.561.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/NDOAPI.framework/NDOAPI`](System__Library__PrivateFrameworks__NDOAPI.framework__NDOAPI.md) | 624.40.22.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppletTranslationFramework.framework/AppletTranslationFramework`](System__Library__PrivateFrameworks__AppletTranslationFramework.framework__AppletTranslationFramework.md) | 71.5.0.0.0 | light |
| [`/usr/lib/libnfshared.dylib`](usr__lib__libnfshared.dylib.md) | 371.8.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/StreamingExtractor.framework/StreamingExtractor`](System__Library__PrivateFrameworks__StreamingExtractor.framework__StreamingExtractor.md) | 55.40.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/People.framework/People`](System__Library__PrivateFrameworks__People.framework__People.md) | 148.125.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis`](System__Library__PrivateFrameworks__PhotoAnalysis.framework__PhotoAnalysis.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/PhotosGraph.framework/PhotosGraph`](System__Library__PrivateFrameworks__PhotosGraph.framework__PhotosGraph.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/PhotosFace.framework/PhotosFace`](System__Library__PrivateFrameworks__PhotosFace.framework__PhotosFace.md) | 98.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ComputeSafeguards.framework/ComputeSafeguards`](System__Library__PrivateFrameworks__ComputeSafeguards.framework__ComputeSafeguards.md) | 177.40.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/CloudAttestation.framework/CloudAttestation`](System__Library__PrivateFrameworks__CloudAttestation.framework__CloudAttestation.md) | 323.40.16.0.0 | light |
| [`/System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary`](System__Library__PrivateFrameworks__MDMClientLibrary.framework__MDMClientLibrary.md) | 113.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreRecents.framework/CoreRecents`](System__Library__PrivateFrameworks__CoreRecents.framework__CoreRecents.md) | 1237.200.31.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreRoutineDiagnostics.framework/CoreRoutineDiagnostics`](System__Library__PrivateFrameworks__CoreRoutineDiagnostics.framework__CoreRoutineDiagnostics.md) | 1123.0.3.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend19.dylib`](usr__lib__objc__libobjcMsgSend19.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) | 3486.52.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/PrivateCloudComputeDaemon.framework/PrivateCloudComputeDaemon`](System__Library__PrivateFrameworks__PrivateCloudComputeDaemon.framework__PrivateCloudComputeDaemon.md) | 2570.40.41.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore`](System__Library__PrivateFrameworks__AppleKeyStore.framework__AppleKeyStore.md) | 2383.40.18.0.0 | light |
| [`/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagement`](System__Library__PrivateFrameworks__RemoteManagement.framework__RemoteManagement.md) | 624.52.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/Mercury.framework/Mercury`](System__Library__PrivateFrameworks__Mercury.framework__Mercury.md) | 79.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/RemotePairingDevice.framework/RemotePairingDevice`](System__Library__PrivateFrameworks__RemotePairingDevice.framework__RemotePairingDevice.md) | 280.40.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/ReplicatorCore.framework/ReplicatorCore`](System__Library__PrivateFrameworks__ReplicatorCore.framework__ReplicatorCore.md) | 176.2.6.0.0 | light |
| [`/usr/lib/libcoreroutine.dylib`](usr__lib__libcoreroutine.dylib.md) | 1123.0.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/RunningBoard.framework/RunningBoard`](System__Library__PrivateFrameworks__RunningBoard.framework__RunningBoard.md) | 1084.40.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/DynamicPrefetching.framework/DynamicPrefetching`](System__Library__PrivateFrameworks__DynamicPrefetching.framework__DynamicPrefetching.md) | 4.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`](System__Library__PrivateFrameworks__SpotlightDaemon.framework__SpotlightDaemon.md) | 2465.1.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/FindMyCloudKit.framework/FindMyCloudKit`](System__Library__PrivateFrameworks__FindMyCloudKit.framework__FindMyCloudKit.md) | 106.31.6.16.7 | light |
| [`/System/Library/PrivateFrameworks/SPFinder.framework/SPFinder`](System__Library__PrivateFrameworks__SPFinder.framework__SPFinder.md) | 449.31.6.16.29 | light |
| [`/System/Library/PrivateFrameworks/FMNetworking.framework/FMNetworking`](System__Library__PrivateFrameworks__FMNetworking.framework__FMNetworking.md) | 449.31.6.16.29 | light |
| [`/System/Library/PrivateFrameworks/DigitalAccess.framework/DigitalAccess`](System__Library__PrivateFrameworks__DigitalAccess.framework__DigitalAccess.md) | 71.9.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/SEService.framework/SEService`](System__Library__PrivateFrameworks__SEService.framework__SEService.md) | 71.9.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/SharingCore.framework/SharingCore`](System__Library__PrivateFrameworks__SharingCore.framework__SharingCore.md) | 2131.21.31.21.8 | light |
| [`/System/Library/PrivateFrameworks/ShazamEvents.framework/ShazamEvents`](System__Library__PrivateFrameworks__ShazamEvents.framework__ShazamEvents.md) | 427.2.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts`](System__Library__PrivateFrameworks__VoiceShortcuts.framework__VoiceShortcuts.md) | 5114.0.12.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriInference.framework/SiriInference`](System__Library__PrivateFrameworks__SiriInference.framework__SiriInference.md) | 3605.20.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriRemembers.framework/SiriRemembers`](System__Library__PrivateFrameworks__SiriRemembers.framework__SiriRemembers.md) | 3605.20.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/SiriSuggestionsKit`](System__Library__PrivateFrameworks__SiriSuggestionsKit.framework__SiriSuggestionsKit.md) | 3605.7.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/Koa.framework/Koa`](System__Library__PrivateFrameworks__Koa.framework__Koa.md) | 3600.13.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriTTS.framework/SiriTTS`](System__Library__PrivateFrameworks__SiriTTS.framework__SiriTTS.md) | 3605.29.1.11.1 | light |
| [`/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`](System__Library__PrivateFrameworks__SoftwareUpdateServices.framework__SoftwareUpdateServices.md) | 1114.40.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/FileDerivatives.framework/FileDerivatives`](System__Library__PrivateFrameworks__FileDerivatives.framework__FileDerivatives.md) | 63.40.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreSuggestionsInternals.framework/CoreSuggestionsInternals`](System__Library__PrivateFrameworks__CoreSuggestionsInternals.framework__CoreSuggestionsInternals.md) | 1354.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/PersonalizationPortraitInternals.framework/PersonalizationPortraitInternals`](System__Library__PrivateFrameworks__PersonalizationPortraitInternals.framework__PersonalizationPortraitInternals.md) | 1354.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator`](System__Library__PrivateFrameworks__Symptoms.framework__Frameworks__SymptomEvaluator.framework__SymptomEvaluator.md) | 2394.40.17.0.0 | light |
| [`/System/Library/PrivateFrameworks/SymptomShared.framework/SymptomShared`](System__Library__PrivateFrameworks__SymptomShared.framework__SymptomShared.md) | 2394.40.17.0.0 | light |
| [`/System/Library/PrivateFrameworks/SymptomDistribution.framework/SymptomDistribution`](System__Library__PrivateFrameworks__SymptomDistribution.framework__SymptomDistribution.md) | 2394.40.17.0.0 | light |
| [`/System/Library/PrivateFrameworks/OSAServicesClient.framework/OSAServicesClient`](System__Library__PrivateFrameworks__OSAServicesClient.framework__OSAServicesClient.md) | 1056.40.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/ArchetypeEngine.framework/ArchetypeEngine`](System__Library__PrivateFrameworks__ArchetypeEngine.framework__ArchetypeEngine.md) | 41.14.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/TextUnderstandingRuntime.framework/TextUnderstandingRuntime`](System__Library__PrivateFrameworks__TextUnderstandingRuntime.framework__TextUnderstandingRuntime.md) | 192.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/SpotlightReceiver.framework/SpotlightReceiver`](System__Library__PrivateFrameworks__SpotlightReceiver.framework__SpotlightReceiver.md) | 2465.1.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/TipsDaemon.framework/TipsDaemon`](System__Library__PrivateFrameworks__TipsDaemon.framework__TipsDaemon.md) | 866.2.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/SupportFlowCore.framework/SupportFlowCore`](System__Library__PrivateFrameworks__SupportFlowCore.framework__SupportFlowCore.md) | 37.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/TranslationInference.framework/TranslationInference`](System__Library__PrivateFrameworks__TranslationInference.framework__TranslationInference.md) | 396.2.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon`](System__Library__PrivateFrameworks__TranslationDaemon.framework__TranslationDaemon.md) | 396.2.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CloudTelemetry.framework/CloudTelemetry`](System__Library__PrivateFrameworks__CloudTelemetry.framework__CloudTelemetry.md) | 2722.40.2.0.0 | light |
| [`/System/Library/VideoCodecs/H264SW.videocodec`](System__Library__VideoCodecs__H264SW.videocodec.md) | 912.1.0.0.0 | light |
| [`/System/Library/VideoCodecs/VCPHEVC.videocodec`](System__Library__VideoCodecs__VCPHEVC.videocodec.md) | 390.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/UnblockService.framework/UnblockService`](System__Library__PrivateFrameworks__UnblockService.framework__UnblockService.md) | 18.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) | 1032.9.0.0.0 | full |
| [`/usr/lib/libprotobuf-lite.dylib`](usr__lib__libprotobuf-lite.dylib.md) | 7019.0.0.0.0 | light |
| [`/System/Library/AccessibilityBundles/ARKit.axbundle/ARKit`](System__Library__AccessibilityBundles__ARKit.axbundle__ARKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ARTraceModule.axbundle/ARTraceModule`](System__Library__AccessibilityBundles__ARTraceModule.axbundle__ARTraceModule.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ASMessagesProvider.axbundle/ASMessagesProvider`](System__Library__AccessibilityBundles__ASMessagesProvider.axbundle__ASMessagesProvider.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AXActionSheetUIServer.axuiservice/AXActionSheetUIServer`](System__Library__AccessibilityBundles__AXActionSheetUIServer.axuiservice__AXActionSheetUIServer.md) | 3245.8.9.0.0 | light |
| [`/System/Library/AccessibilityBundles/AccessibilitySettings.axbundle/AccessibilitySettings`](System__Library__AccessibilityBundles__AccessibilitySettings.axbundle__AccessibilitySettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AccountsUI.axbundle/AccountsUI`](System__Library__AccessibilityBundles__AccountsUI.axbundle__AccountsUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AcousticId-Assistant.axbundle/AcousticId-Assistant`](System__Library__AccessibilityBundles__AcousticId-Assistant.axbundle__AcousticId-Assistant.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ActionButtonConfigurationUI.axbundle/ActionButtonConfigurationUI`](System__Library__AccessibilityBundles__ActionButtonConfigurationUI.axbundle__ActionButtonConfigurationUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ActionButtonSelector.axbundle/ActionButtonSelector`](System__Library__AccessibilityBundles__ActionButtonSelector.axbundle__ActionButtonSelector.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ActiveSyncSettings.axbundle/ActiveSyncSettings`](System__Library__AccessibilityBundles__ActiveSyncSettings.axbundle__ActiveSyncSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ActivityUIServices.axbundle/ActivityUIServices`](System__Library__AccessibilityBundles__ActivityUIServices.axbundle__ActivityUIServices.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AddressBook-Assistant.axbundle/AddressBook-Assistant`](System__Library__AccessibilityBundles__AddressBook-Assistant.axbundle__AddressBook-Assistant.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AddressBookUIFramework.axbundle/AddressBookUIFramework`](System__Library__AccessibilityBundles__AddressBookUIFramework.axbundle__AddressBookUIFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AirDrop.axbundle/AirDrop`](System__Library__AccessibilityBundles__AirDrop.axbundle__AirDrop.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AirDropUI.axbundle/AirDropUI`](System__Library__AccessibilityBundles__AirDropUI.axbundle__AirDropUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AirPlayMirroringModule.axbundle/AirPlayMirroringModule`](System__Library__AccessibilityBundles__AirPlayMirroringModule.axbundle__AirPlayMirroringModule.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AirPortSettings.axbundle/AirPortSettings`](System__Library__AccessibilityBundles__AirPortSettings.axbundle__AirPortSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AirTrafficSettings.axbundle/AirTrafficSettings`](System__Library__AccessibilityBundles__AirTrafficSettings.axbundle__AirTrafficSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AmbientUI.axbundle/AmbientUI`](System__Library__AccessibilityBundles__AmbientUI.axbundle__AmbientUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Animoji.axbundle/Animoji`](System__Library__AccessibilityBundles__Animoji.axbundle__Animoji.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AnnotationKit.axbundle/AnnotationKit`](System__Library__AccessibilityBundles__AnnotationKit.axbundle__AnnotationKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AppInstallExtension.axbundle/AppInstallExtension`](System__Library__AccessibilityBundles__AppInstallExtension.axbundle__AppInstallExtension.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AppPredictionUI.axbundle/AppPredictionUI`](System__Library__AccessibilityBundles__AppPredictionUI.axbundle__AppPredictionUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AppPredictionUIWidget.axbundle/AppPredictionUIWidget`](System__Library__AccessibilityBundles__AppPredictionUIWidget.axbundle__AppPredictionUIWidget.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AppearanceModule.axbundle/AppearanceModule`](System__Library__AccessibilityBundles__AppearanceModule.axbundle__AppearanceModule.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AppleAccountUI.axbundle/AppleAccountUI`](System__Library__AccessibilityBundles__AppleAccountUI.axbundle__AppleAccountUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AppleTV.axbundle/AppleTV`](System__Library__AccessibilityBundles__AppleTV.axbundle__AppleTV.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Arcade.axbundle/Arcade`](System__Library__AccessibilityBundles__Arcade.axbundle__Arcade.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AssetExplorer.axbundle/AssetExplorer`](System__Library__AccessibilityBundles__AssetExplorer.axbundle__AssetExplorer.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AssetViewer.axbundle/AssetViewer`](System__Library__AccessibilityBundles__AssetViewer.axbundle__AssetViewer.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AssistantServices.axbundle/AssistantServices`](System__Library__AccessibilityBundles__AssistantServices.axbundle__AssistantServices.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AssistantUI.axbundle/AssistantUI`](System__Library__AccessibilityBundles__AssistantUI.axbundle__AssistantUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AttributionWeeApp.axbundle/AttributionWeeApp`](System__Library__AccessibilityBundles__AttributionWeeApp.axbundle__AttributionWeeApp.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Audio-QuickLook.axbundle/Audio-QuickLook`](System__Library__AccessibilityBundles__Audio-QuickLook.axbundle__Audio-QuickLook.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AuthenticationServices.axbundle/AuthenticationServices`](System__Library__AccessibilityBundles__AuthenticationServices.axbundle__AuthenticationServices.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AvatarKit.axbundle/AvatarKit`](System__Library__AccessibilityBundles__AvatarKit.axbundle__AvatarKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AvatarPickerMemojiPicker.axbundle/AvatarPickerMemojiPicker`](System__Library__AccessibilityBundles__AvatarPickerMemojiPicker.axbundle__AvatarPickerMemojiPicker.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AvatarUI.axbundle/AvatarUI`](System__Library__AccessibilityBundles__AvatarUI.axbundle__AvatarUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/BPSStingSetup.axbundle/BPSStingSetup`](System__Library__AccessibilityBundles__BPSStingSetup.axbundle__BPSStingSetup.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/BarcodeScanner.axbundle/BarcodeScanner`](System__Library__AccessibilityBundles__BarcodeScanner.axbundle__BarcodeScanner.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/BaseBoardUI.axbundle/BaseBoardUI`](System__Library__AccessibilityBundles__BaseBoardUI.axbundle__BaseBoardUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/BatteryCenterUI.axbundle/BatteryCenterUI`](System__Library__AccessibilityBundles__BatteryCenterUI.axbundle__BatteryCenterUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/BatteryWidget.axbundle/BatteryWidget`](System__Library__AccessibilityBundles__BatteryWidget.axbundle__BatteryWidget.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/BluetoothSettings.axbundle/BluetoothSettings`](System__Library__AccessibilityBundles__BluetoothSettings.axbundle__BluetoothSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Bridge.axbundle/Bridge`](System__Library__AccessibilityBundles__Bridge.axbundle__Bridge.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/BridgePreferences.axbundle/BridgePreferences`](System__Library__AccessibilityBundles__BridgePreferences.axbundle__BridgePreferences.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/BridgeStoreExtension.axbundle/BridgeStoreExtension`](System__Library__AccessibilityBundles__BridgeStoreExtension.axbundle__BridgeStoreExtension.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Business.axbundle/Business`](System__Library__AccessibilityBundles__Business.axbundle__Business.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/BusinessChatFramework.axbundle/BusinessChatFramework`](System__Library__AccessibilityBundles__BusinessChatFramework.axbundle__BusinessChatFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CARDNDUI.axbundle/CARDNDUI`](System__Library__AccessibilityBundles__CARDNDUI.axbundle__CARDNDUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Calculator.axbundle/Calculator`](System__Library__AccessibilityBundles__Calculator.axbundle__Calculator.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Calendar-Assistant.axbundle/Calendar-Assistant`](System__Library__AccessibilityBundles__Calendar-Assistant.axbundle__Calendar-Assistant.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Camera.axbundle/Camera`](System__Library__AccessibilityBundles__Camera.axbundle__Camera.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CameraEffectsKit.axbundle/CameraEffectsKit`](System__Library__AccessibilityBundles__CameraEffectsKit.axbundle__CameraEffectsKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CameraKit.axbundle/CameraKit`](System__Library__AccessibilityBundles__CameraKit.axbundle__CameraKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CameraOverlayAngel.axbundle/CameraOverlayAngel`](System__Library__AccessibilityBundles__CameraOverlayAngel.axbundle__CameraOverlayAngel.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CarModeModule.axbundle/CarModeModule`](System__Library__AccessibilityBundles__CarModeModule.axbundle__CarModeModule.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CarPlay.axbundle/CarPlay`](System__Library__AccessibilityBundles__CarPlay.axbundle__CarPlay.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CardKit.axbundle/CardKit`](System__Library__AccessibilityBundles__CardKit.axbundle__CardKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CarouselAppViewSettings.axbundle/CarouselAppViewSettings`](System__Library__AccessibilityBundles__CarouselAppViewSettings.axbundle__CarouselAppViewSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CertInfo.axbundle/CertInfo`](System__Library__AccessibilityBundles__CertInfo.axbundle__CertInfo.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ChargingViewService.axbundle/ChargingViewService`](System__Library__AccessibilityBundles__ChargingViewService.axbundle__ChargingViewService.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ChatKitAssistantUI-Assistant.axbundle/ChatKitAssistantUI-Assistant`](System__Library__AccessibilityBundles__ChatKitAssistantUI-Assistant.axbundle__ChatKitAssistantUI-Assistant.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CheckerBoard.axbundle/CheckerBoard`](System__Library__AccessibilityBundles__CheckerBoard.axbundle__CheckerBoard.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ChronoCore.axbundle/ChronoCore`](System__Library__AccessibilityBundles__ChronoCore.axbundle__ChronoCore.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ClipUIServices.axbundle/ClipUIServices`](System__Library__AccessibilityBundles__ClipUIServices.axbundle__ClipUIServices.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CompanionAppViewSetup.axbundle/CompanionAppViewSetup`](System__Library__AccessibilityBundles__CompanionAppViewSetup.axbundle__CompanionAppViewSetup.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CompanionStingSettings.axbundle/CompanionStingSettings`](System__Library__AccessibilityBundles__CompanionStingSettings.axbundle__CompanionStingSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Compass.axbundle/Compass`](System__Library__AccessibilityBundles__Compass.axbundle__Compass.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CompassViewCalibrationService.axbundle/CompassViewCalibrationService`](System__Library__AccessibilityBundles__CompassViewCalibrationService.axbundle__CompassViewCalibrationService.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ContinuityCapture.axbundle/ContinuityCapture`](System__Library__AccessibilityBundles__ContinuityCapture.axbundle__ContinuityCapture.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ContinuityDisplay.axbundle/ContinuityDisplay`](System__Library__AccessibilityBundles__ContinuityDisplay.axbundle__ContinuityDisplay.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ContinuousExposeModule.axbundle/ContinuousExposeModule`](System__Library__AccessibilityBundles__ContinuousExposeModule.axbundle__ContinuousExposeModule.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CoreAuthUI.axbundle/CoreAuthUI`](System__Library__AccessibilityBundles__CoreAuthUI.axbundle__CoreAuthUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CoreCDPUI.axbundle/CoreCDPUI`](System__Library__AccessibilityBundles__CoreCDPUI.axbundle__CoreCDPUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CoreDynamicUIPlugin.axbundle/CoreDynamicUIPlugin`](System__Library__AccessibilityBundles__CoreDynamicUIPlugin.axbundle__CoreDynamicUIPlugin.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CoreIDVRGBLiveness.axbundle/CoreIDVRGBLiveness`](System__Library__AccessibilityBundles__CoreIDVRGBLiveness.axbundle__CoreIDVRGBLiveness.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CoreIDVUI.axbundle/CoreIDVUI`](System__Library__AccessibilityBundles__CoreIDVUI.axbundle__CoreIDVUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CoreRecognition.axbundle/CoreRecognition`](System__Library__AccessibilityBundles__CoreRecognition.axbundle__CoreRecognition.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CoreSuggestionsUI.axbundle/CoreSuggestionsUI`](System__Library__AccessibilityBundles__CoreSuggestionsUI.axbundle__CoreSuggestionsUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CoverSheetKit.axbundle/CoverSheetKit`](System__Library__AccessibilityBundles__CoverSheetKit.axbundle__CoverSheetKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/DDActionsService.axbundle/DDActionsService`](System__Library__AccessibilityBundles__DDActionsService.axbundle__DDActionsService.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/DashBoard.axbundle/DashBoard`](System__Library__AccessibilityBundles__DashBoard.axbundle__DashBoard.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/DataActivation.axbundle/DataActivation`](System__Library__AccessibilityBundles__DataActivation.axbundle__DataActivation.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/DefaultMediaPlayer-QuickLook.axbundle/DefaultMediaPlayer-QuickLook`](System__Library__AccessibilityBundles__DefaultMediaPlayer-QuickLook.axbundle__DefaultMediaPlayer-QuickLook.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Diagnostics.axbundle/Diagnostics`](System__Library__AccessibilityBundles__Diagnostics.axbundle__Diagnostics.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/DictionarySettings.axbundle/DictionarySettings`](System__Library__AccessibilityBundles__DictionarySettings.axbundle__DictionarySettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/DigitalSeparationSettings.axbundle/DigitalSeparationSettings`](System__Library__AccessibilityBundles__DigitalSeparationSettings.axbundle__DigitalSeparationSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/DigitalTouchBalloonProvider.axbundle/DigitalTouchBalloonProvider`](System__Library__AccessibilityBundles__DigitalTouchBalloonProvider.axbundle__DigitalTouchBalloonProvider.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/DigitalTouchShared.axbundle/DigitalTouchShared`](System__Library__AccessibilityBundles__DigitalTouchShared.axbundle__DigitalTouchShared.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/DisplayModule.axbundle/DisplayModule`](System__Library__AccessibilityBundles__DisplayModule.axbundle__DisplayModule.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/DoNotDisturbModule.axbundle/DoNotDisturbModule`](System__Library__AccessibilityBundles__DoNotDisturbModule.axbundle__DoNotDisturbModule.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/DoNotDisturbSettings.axbundle/DoNotDisturbSettings`](System__Library__AccessibilityBundles__DoNotDisturbSettings.axbundle__DoNotDisturbSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/DockFolderViewService.axbundle/DockFolderViewService`](System__Library__AccessibilityBundles__DockFolderViewService.axbundle__DockFolderViewService.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/DocumentManager.axbundle/DocumentManager`](System__Library__AccessibilityBundles__DocumentManager.axbundle__DocumentManager.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/DocumentManagerExecutables.axbundle/DocumentManagerExecutables`](System__Library__AccessibilityBundles__DocumentManagerExecutables.axbundle__DocumentManagerExecutables.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/DocumentManagerUICore.axbundle/DocumentManagerUICore`](System__Library__AccessibilityBundles__DocumentManagerUICore.axbundle__DocumentManagerUICore.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/DrawingKit.axbundle/DrawingKit`](System__Library__AccessibilityBundles__DrawingKit.axbundle__DrawingKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/EmojiKit.axbundle/EmojiKit`](System__Library__AccessibilityBundles__EmojiKit.axbundle__EmojiKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ExposureNotificationSettingsUI.axbundle/ExposureNotificationSettingsUI`](System__Library__AccessibilityBundles__ExposureNotificationSettingsUI.axbundle__ExposureNotificationSettingsUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/FacebookSettings.axbundle/FacebookSettings`](System__Library__AccessibilityBundles__FacebookSettings.axbundle__FacebookSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Files.axbundle/Files`](System__Library__AccessibilityBundles__Files.axbundle__Files.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/FindMy.axbundle/FindMy`](System__Library__AccessibilityBundles__FindMy.axbundle__FindMy.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/FlashlightModule.axbundle/FlashlightModule`](System__Library__AccessibilityBundles__FlashlightModule.axbundle__FlashlightModule.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/FlightUtilities.axbundle/FlightUtilities`](System__Library__AccessibilityBundles__FlightUtilities.axbundle__FlightUtilities.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/FocusUI.axbundle/FocusUI`](System__Library__AccessibilityBundles__FocusUI.axbundle__FocusUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/FocusUIModule.axbundle/FocusUIModule`](System__Library__AccessibilityBundles__FocusUIModule.axbundle__FocusUIModule.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/FontPicker.axbundle/FontPicker`](System__Library__AccessibilityBundles__FontPicker.axbundle__FontPicker.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/FontSettings.axbundle/FontSettings`](System__Library__AccessibilityBundles__FontSettings.axbundle__FontSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/FrontBoard.axbundle/FrontBoard`](System__Library__AccessibilityBundles__FrontBoard.axbundle__FrontBoard.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Game`](System__Library__AccessibilityBundles__Game.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/GameCenterDashboardExtension.axbundle/GameCenterDashboardExtension`](System__Library__AccessibilityBundles__GameCenterDashboardExtension.axbundle__GameCenterDashboardExtension.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/GameCenterPrivateUIFramework.axbundle/GameCenterPrivateUIFramework`](System__Library__AccessibilityBundles__GameCenterPrivateUIFramework.axbundle__GameCenterPrivateUIFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/GameCenterUIFramework.axbundle/GameCenterUIFramework`](System__Library__AccessibilityBundles__GameCenterUIFramework.axbundle__GameCenterUIFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/GameCenterUIService.axbundle/GameCenterUIService`](System__Library__AccessibilityBundles__GameCenterUIService.axbundle__GameCenterUIService.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/GameKitFramework.axbundle/GameKitFramework`](System__Library__AccessibilityBundles__GameKitFramework.axbundle__GameKitFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/GeneralKnowledge-Assistant.axbundle/GeneralKnowledge-Assistant`](System__Library__AccessibilityBundles__GeneralKnowledge-Assistant.axbundle__GeneralKnowledge-Assistant.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/GeneralSettingsUI.axbundle/GeneralSettingsUI`](System__Library__AccessibilityBundles__GeneralSettingsUI.axbundle__GeneralSettingsUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/GeoServices.axbundle/GeoServices`](System__Library__AccessibilityBundles__GeoServices.axbundle__GeoServices.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Gif-QuickLook.axbundle/Gif-QuickLook`](System__Library__AccessibilityBundles__Gif-QuickLook.axbundle__Gif-QuickLook.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/HDSViewService.axbundle/HDSViewService`](System__Library__AccessibilityBundles__HDSViewService.axbundle__HDSViewService.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/HandwritingProvider.axbundle/HandwritingProvider`](System__Library__AccessibilityBundles__HandwritingProvider.axbundle__HandwritingProvider.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/HashtagImagesExtension.axbundle/HashtagImagesExtension`](System__Library__AccessibilityBundles__HashtagImagesExtension.axbundle__HashtagImagesExtension.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/HeadphoneProxService.axbundle/HeadphoneProxService`](System__Library__AccessibilityBundles__HeadphoneProxService.axbundle__HeadphoneProxService.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/HealthArticlesUI.axbundle/HealthArticlesUI`](System__Library__AccessibilityBundles__HealthArticlesUI.axbundle__HealthArticlesUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/HealthExposureNotificationUI.axbundle/HealthExposureNotificationUI`](System__Library__AccessibilityBundles__HealthExposureNotificationUI.axbundle__HealthExposureNotificationUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/HealthKitUI.axbundle/HealthKitUI`](System__Library__AccessibilityBundles__HealthKitUI.axbundle__HealthKitUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/HealthRecordsUI.axbundle/HealthRecordsUI`](System__Library__AccessibilityBundles__HealthRecordsUI.axbundle__HealthRecordsUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/HealthSafety.axbundle/HealthSafety`](System__Library__AccessibilityBundles__HealthSafety.axbundle__HealthSafety.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/HealthToolbox.axbundle/HealthToolbox`](System__Library__AccessibilityBundles__HealthToolbox.axbundle__HealthToolbox.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/HealthVisualization.axbundle/HealthVisualization`](System__Library__AccessibilityBundles__HealthVisualization.axbundle__HealthVisualization.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/HearingAidUIServer.axuiservice/HearingAidUIServer`](System__Library__AccessibilityBundles__HearingAidUIServer.axuiservice__HearingAidUIServer.md) | 3245.8.9.0.0 | light |
| [`/System/Library/AccessibilityBundles/HeartRhythmUI.axbundle/HeartRhythmUI`](System__Library__AccessibilityBundles__HeartRhythmUI.axbundle__HeartRhythmUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/HelpKit.axbundle/HelpKit`](System__Library__AccessibilityBundles__HelpKit.axbundle__HelpKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/HomeControlCenterCompactModule.axbundle/HomeControlCenterCompactModule`](System__Library__AccessibilityBundles__HomeControlCenterCompactModule.axbundle__HomeControlCenterCompactModule.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/HomeControlCenterModule.axbundle/HomeControlCenterModule`](System__Library__AccessibilityBundles__HomeControlCenterModule.axbundle__HomeControlCenterModule.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/HomeControlService.axbundle/HomeControlService`](System__Library__AccessibilityBundles__HomeControlService.axbundle__HomeControlService.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/HomeUI.axbundle/HomeUI`](System__Library__AccessibilityBundles__HomeUI.axbundle__HomeUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/HomeUIService.axbundle/HomeUIService`](System__Library__AccessibilityBundles__HomeUIService.axbundle__HomeUIService.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Image-QuickLook.axbundle/Image-QuickLook`](System__Library__AccessibilityBundles__Image-QuickLook.axbundle__Image-QuickLook.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/InCallLockScreen.axbundle/InCallLockScreen`](System__Library__AccessibilityBundles__InCallLockScreen.axbundle__InCallLockScreen.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/IncomingCall.axbundle/IncomingCall`](System__Library__AccessibilityBundles__IncomingCall.axbundle__IncomingCall.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/InputUI.axbundle/InputUI`](System__Library__AccessibilityBundles__InputUI.axbundle__InputUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/IntelligentCallScreeningSettingsBundle.axbundle/IntelligentCallScreeningSettingsBundle`](System__Library__AccessibilityBundles__IntelligentCallScreeningSettingsBundle.axbundle__IntelligentCallScreeningSettingsBundle.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/IntentsUI.axbundle/IntentsUI`](System__Library__AccessibilityBundles__IntentsUI.axbundle__IntentsUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/InternationalSettings.axbundle/InternationalSettings`](System__Library__AccessibilityBundles__InternationalSettings.axbundle__InternationalSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/KeyboardSettings.axbundle/KeyboardSettings`](System__Library__AccessibilityBundles__KeyboardSettings.axbundle__KeyboardSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/LinkPresentation.axbundle/LinkPresentation`](System__Library__AccessibilityBundles__LinkPresentation.axbundle__LinkPresentation.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/LiveTranscriptionUI.axbundle/LiveTranscriptionUI`](System__Library__AccessibilityBundles__LiveTranscriptionUI.axbundle__LiveTranscriptionUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/LocalAuthenticationRGBCapture.axbundle/LocalAuthenticationRGBCapture`](System__Library__AccessibilityBundles__LocalAuthenticationRGBCapture.axbundle__LocalAuthenticationRGBCapture.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/LocalAuthenticationUI.axbundle/LocalAuthenticationUI`](System__Library__AccessibilityBundles__LocalAuthenticationUI.axbundle__LocalAuthenticationUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/LoginUI.axbundle/LoginUI`](System__Library__AccessibilityBundles__LoginUI.axbundle__LoginUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Mail-Assistant.axbundle/Mail-Assistant`](System__Library__AccessibilityBundles__Mail-Assistant.axbundle__Mail-Assistant.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MailAttachmentPlugin.axbundle/MailAttachmentPlugin`](System__Library__AccessibilityBundles__MailAttachmentPlugin.axbundle__MailAttachmentPlugin.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MailVIPWidget.axbundle/MailVIPWidget`](System__Library__AccessibilityBundles__MailVIPWidget.axbundle__MailVIPWidget.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ManagedConfigurationUI.axbundle/ManagedConfigurationUI`](System__Library__AccessibilityBundles__ManagedConfigurationUI.axbundle__ManagedConfigurationUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MapKitFramework.axbundle/MapKitFramework`](System__Library__AccessibilityBundles__MapKitFramework.axbundle__MapKitFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MapKitSwiftUI.axbundle/MapKitSwiftUI`](System__Library__AccessibilityBundles__MapKitSwiftUI.axbundle__MapKitSwiftUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Maps-Assistant.axbundle/Maps-Assistant`](System__Library__AccessibilityBundles__Maps-Assistant.axbundle__Maps-Assistant.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MarkupUI.axbundle/MarkupUI`](System__Library__AccessibilityBundles__MarkupUI.axbundle__MarkupUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Measure.axbundle/Measure`](System__Library__AccessibilityBundles__Measure.axbundle__Measure.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MediaPlayerFramework.axbundle/MediaPlayerFramework`](System__Library__AccessibilityBundles__MediaPlayerFramework.axbundle__MediaPlayerFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MediaPlayerUIFramework.axbundle/MediaPlayerUIFramework`](System__Library__AccessibilityBundles__MediaPlayerUIFramework.axbundle__MediaPlayerUIFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MedicationsHealthAppPlugin.axbundle/MedicationsHealthAppPlugin`](System__Library__AccessibilityBundles__MedicationsHealthAppPlugin.axbundle__MedicationsHealthAppPlugin.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Memories.axbundle/Memories`](System__Library__AccessibilityBundles__Memories.axbundle__Memories.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Messages.axbundle/Messages`](System__Library__AccessibilityBundles__Messages.axbundle__Messages.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MessagesFlowDelegatePlugin.axbundle/MessagesFlowDelegatePlugin`](System__Library__AccessibilityBundles__MessagesFlowDelegatePlugin.axbundle__MessagesFlowDelegatePlugin.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MobileSMS.axbundle/MobileSMS`](System__Library__AccessibilityBundles__MobileSMS.axbundle__MobileSMS.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MobileSafari.axbundle/MobileSafari`](System__Library__AccessibilityBundles__MobileSafari.axbundle__MobileSafari.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MobileSafariFramework.axbundle/MobileSafariFramework`](System__Library__AccessibilityBundles__MobileSafariFramework.axbundle__MobileSafariFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MobileSafariSettings.axbundle/MobileSafariSettings`](System__Library__AccessibilityBundles__MobileSafariSettings.axbundle__MobileSafariSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MobileSafariUI.axbundle/MobileSafariUI`](System__Library__AccessibilityBundles__MobileSafariUI.axbundle__MobileSafariUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MobileSlideShow.axbundle/MobileSlideShow`](System__Library__AccessibilityBundles__MobileSlideShow.axbundle__MobileSlideShow.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MobileStore.axbundle/MobileStore`](System__Library__AccessibilityBundles__MobileStore.axbundle__MobileStore.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MobileStoreUI.axbundle/MobileStoreUI`](System__Library__AccessibilityBundles__MobileStoreUI.axbundle__MobileStoreUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MobileTimer-Assistant.axbundle/MobileTimer-Assistant`](System__Library__AccessibilityBundles__MobileTimer-Assistant.axbundle__MobileTimer-Assistant.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MobileTimerFramework.axbundle/MobileTimerFramework`](System__Library__AccessibilityBundles__MobileTimerFramework.axbundle__MobileTimerFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MobileTimerUIFramework.axbundle/MobileTimerUIFramework`](System__Library__AccessibilityBundles__MobileTimerUIFramework.axbundle__MobileTimerUIFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MonogramPosterExtension.axbundle/MonogramPosterExtension`](System__Library__AccessibilityBundles__MonogramPosterExtension.axbundle__MonogramPosterExtension.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Movie-QuickLook.axbundle/Movie-QuickLook`](System__Library__AccessibilityBundles__Movie-QuickLook.axbundle__Movie-QuickLook.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Movies-Assistant.axbundle/Movies-Assistant`](System__Library__AccessibilityBundles__Movies-Assistant.axbundle__Movies-Assistant.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MusicApplication.axbundle/MusicApplication`](System__Library__AccessibilityBundles__MusicApplication.axbundle__MusicApplication.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MusicMessagesApp.axbundle/MusicMessagesApp`](System__Library__AccessibilityBundles__MusicMessagesApp.axbundle__MusicMessagesApp.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MusicRecognition.axbundle/MusicRecognition`](System__Library__AccessibilityBundles__MusicRecognition.axbundle__MusicRecognition.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MusicSettings.axbundle/MusicSettings`](System__Library__AccessibilityBundles__MusicSettings.axbundle__MusicSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MusicUI.axbundle/MusicUI`](System__Library__AccessibilityBundles__MusicUI.axbundle__MusicUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MusicUsage.axbundle/MusicUsage`](System__Library__AccessibilityBundles__MusicUsage.axbundle__MusicUsage.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/MuteModule.axbundle/MuteModule`](System__Library__AccessibilityBundles__MuteModule.axbundle__MuteModule.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/NFCControlCenterModule.axbundle/NFCControlCenterModule`](System__Library__AccessibilityBundles__NFCControlCenterModule.axbundle__NFCControlCenterModule.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Nearby.axbundle/Nearby`](System__Library__AccessibilityBundles__Nearby.axbundle__Nearby.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/NotificationCenter.axbundle/NotificationCenter`](System__Library__AccessibilityBundles__NotificationCenter.axbundle__NotificationCenter.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/NotificationsSettings.axbundle/NotificationsSettings`](System__Library__AccessibilityBundles__NotificationsSettings.axbundle__NotificationsSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/OpusKit.axbundle/OpusKit`](System__Library__AccessibilityBundles__OpusKit.axbundle__OpusKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/OrientationLockModule.axbundle/OrientationLockModule`](System__Library__AccessibilityBundles__OrientationLockModule.axbundle__OrientationLockModule.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PassKitFramework.axbundle/PassKitFramework`](System__Library__AccessibilityBundles__PassKitFramework.axbundle__PassKitFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PassesLockScreenPlugin.axbundle/PassesLockScreenPlugin`](System__Library__AccessibilityBundles__PassesLockScreenPlugin.axbundle__PassesLockScreenPlugin.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PasswordsSettings.axbundle/PasswordsSettings`](System__Library__AccessibilityBundles__PasswordsSettings.axbundle__PasswordsSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PeerPaymentMessagesExtension.axbundle/PeerPaymentMessagesExtension`](System__Library__AccessibilityBundles__PeerPaymentMessagesExtension.axbundle__PeerPaymentMessagesExtension.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PerformanceTraceModule.axbundle/PerformanceTraceModule`](System__Library__AccessibilityBundles__PerformanceTraceModule.axbundle__PerformanceTraceModule.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PhoneCallFlowDelegatePlugin.axbundle/PhoneCallFlowDelegatePlugin`](System__Library__AccessibilityBundles__PhoneCallFlowDelegatePlugin.axbundle__PhoneCallFlowDelegatePlugin.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Photo`](System__Library__AccessibilityBundles__Photo.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PhotoLibraryFramework.axbundle/PhotoLibraryFramework`](System__Library__AccessibilityBundles__PhotoLibraryFramework.axbundle__PhotoLibraryFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PhotoLibraryServices.axbundle/PhotoLibraryServices`](System__Library__AccessibilityBundles__PhotoLibraryServices.axbundle__PhotoLibraryServices.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PhotosEditUI.axbundle/PhotosEditUI`](System__Library__AccessibilityBundles__PhotosEditUI.axbundle__PhotosEditUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PlatterKit.axbundle/PlatterKit`](System__Library__AccessibilityBundles__PlatterKit.axbundle__PlatterKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Podcasts.axbundle/Podcasts`](System__Library__AccessibilityBundles__Podcasts.axbundle__Podcasts.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PodcastsPodcastsTodayExtension.axbundle/PodcastsPodcastsTodayExtension`](System__Library__AccessibilityBundles__PodcastsPodcastsTodayExtension.axbundle__PodcastsPodcastsTodayExtension.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PosterBoard.axbundle/PosterBoard`](System__Library__AccessibilityBundles__PosterBoard.axbundle__PosterBoard.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PreBoard.axbundle/PreBoard`](System__Library__AccessibilityBundles__PreBoard.axbundle__PreBoard.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Preferences.axbundle/Preferences`](System__Library__AccessibilityBundles__Preferences.axbundle__Preferences.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PreferencesUI.axbundle/PreferencesUI`](System__Library__AccessibilityBundles__PreferencesUI.axbundle__PreferencesUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PreviewUI.axbundle/PreviewUI`](System__Library__AccessibilityBundles__PreviewUI.axbundle__PreviewUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PrintKitUI.axbundle/PrintKitUI`](System__Library__AccessibilityBundles__PrintKitUI.axbundle__PrintKitUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PrivacySettingsUI.axbundle/PrivacySettingsUI`](System__Library__AccessibilityBundles__PrivacySettingsUI.axbundle__PrivacySettingsUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ProductPageExtension.axbundle/ProductPageExtension`](System__Library__AccessibilityBundles__ProductPageExtension.axbundle__ProductPageExtension.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ProxCardKit.axbundle/ProxCardKit`](System__Library__AccessibilityBundles__ProxCardKit.axbundle__ProxCardKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/QuickLook.axbundle/QuickLook`](System__Library__AccessibilityBundles__QuickLook.axbundle__QuickLook.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/QuickSpeak.bundle/QuickSpeak`](System__Library__AccessibilityBundles__QuickSpeak.bundle__QuickSpeak.md) | 3245.8.9.0.0 | light |
| [`/System/Library/AccessibilityBundles/QuickTime`](System__Library__AccessibilityBundles__QuickTime.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/RealityFoundation.axbundle/RealityFoundation`](System__Library__AccessibilityBundles__RealityFoundation.axbundle__RealityFoundation.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/RealityKit.axbundle/RealityKit`](System__Library__AccessibilityBundles__RealityKit.axbundle__RealityKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/RecentlyPlayedTodayExtension.axbundle/RecentlyPlayedTodayExtension`](System__Library__AccessibilityBundles__RecentlyPlayedTodayExtension.axbundle__RecentlyPlayedTodayExtension.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/RecentsAvocado.axbundle/RecentsAvocado`](System__Library__AccessibilityBundles__RecentsAvocado.axbundle__RecentsAvocado.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Restaurants-Assistant.axbundle/Restaurants-Assistant`](System__Library__AccessibilityBundles__Restaurants-Assistant.axbundle__Restaurants-Assistant.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SIMSetupUIService.axbundle/SIMSetupUIService`](System__Library__AccessibilityBundles__SIMSetupUIService.axbundle__SIMSetupUIService.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SOSSettings.axbundle/SOSSettings`](System__Library__AccessibilityBundles__SOSSettings.axbundle__SOSSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SafariServices.axbundle/SafariServices`](System__Library__AccessibilityBundles__SafariServices.axbundle__SafariServices.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SafariSharedUI.axbundle/SafariSharedUI`](System__Library__AccessibilityBundles__SafariSharedUI.axbundle__SafariSharedUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SaveToFiles.axbundle/SaveToFiles`](System__Library__AccessibilityBundles__SaveToFiles.axbundle__SaveToFiles.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SceneKit.axbundle/SceneKit`](System__Library__AccessibilityBundles__SceneKit.axbundle__SceneKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ScreenTimeSettingsUI.axbundle/ScreenTimeSettingsUI`](System__Library__AccessibilityBundles__ScreenTimeSettingsUI.axbundle__ScreenTimeSettingsUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ScreenTimeUI.axbundle/ScreenTimeUI`](System__Library__AccessibilityBundles__ScreenTimeUI.axbundle__ScreenTimeUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ScreenshotServicesFramework.axbundle/ScreenshotServicesFramework`](System__Library__AccessibilityBundles__ScreenshotServicesFramework.axbundle__ScreenshotServicesFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ScreenshotServicesService.axbundle/ScreenshotServicesService`](System__Library__AccessibilityBundles__ScreenshotServicesService.axbundle__ScreenshotServicesService.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SearchFoundation.axbundle/SearchFoundation`](System__Library__AccessibilityBundles__SearchFoundation.axbundle__SearchFoundation.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SearchSettings.axbundle/SearchSettings`](System__Library__AccessibilityBundles__SearchSettings.axbundle__SearchSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Settings-Assistant.axbundle/Settings-Assistant`](System__Library__AccessibilityBundles__Settings-Assistant.axbundle__Settings-Assistant.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Setup.axbundle/Setup`](System__Library__AccessibilityBundles__Setup.axbundle__Setup.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SetupAssistantUI.axbundle/SetupAssistantUI`](System__Library__AccessibilityBundles__SetupAssistantUI.axbundle__SetupAssistantUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SharedWithYouFramework.axbundle/SharedWithYouFramework`](System__Library__AccessibilityBundles__SharedWithYouFramework.axbundle__SharedWithYouFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SharingUI.axbundle/SharingUI`](System__Library__AccessibilityBundles__SharingUI.axbundle__SharingUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SharingViewService.axbundle/SharingViewService`](System__Library__AccessibilityBundles__SharingViewService.axbundle__SharingViewService.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Shortcuts.axbundle/Shortcuts`](System__Library__AccessibilityBundles__Shortcuts.axbundle__Shortcuts.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ShortcutsUI.axbundle/ShortcutsUI`](System__Library__AccessibilityBundles__ShortcutsUI.axbundle__ShortcutsUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Sidecar.axbundle/Sidecar`](System__Library__AccessibilityBundles__Sidecar.axbundle__Sidecar.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SiriActivation.axbundle/SiriActivation`](System__Library__AccessibilityBundles__SiriActivation.axbundle__SiriActivation.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SiriKitRuntime.axbundle/SiriKitRuntime`](System__Library__AccessibilityBundles__SiriKitRuntime.axbundle__SiriKitRuntime.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SiriUI.axbundle/SiriUI`](System__Library__AccessibilityBundles__SiriUI.axbundle__SiriUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SiriUICore.axbundle/SiriUICore`](System__Library__AccessibilityBundles__SiriUICore.axbundle__SiriUICore.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Siriland.axbundle/Siriland`](System__Library__AccessibilityBundles__Siriland.axbundle__Siriland.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SleepHealthUI.axbundle/SleepHealthUI`](System__Library__AccessibilityBundles__SleepHealthUI.axbundle__SleepHealthUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SocialFramework.axbundle/SocialFramework`](System__Library__AccessibilityBundles__SocialFramework.axbundle__SocialFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SocialLayer.axbundle/SocialLayer`](System__Library__AccessibilityBundles__SocialLayer.axbundle__SocialLayer.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SocialWeeApp.axbundle/SocialWeeApp`](System__Library__AccessibilityBundles__SocialWeeApp.axbundle__SocialWeeApp.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SoftwareUpdateSettingsUI.axbundle/SoftwareUpdateSettingsUI`](System__Library__AccessibilityBundles__SoftwareUpdateSettingsUI.axbundle__SoftwareUpdateSettingsUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SoundsAndHapticsSettings.axbundle/SoundsAndHapticsSettings`](System__Library__AccessibilityBundles__SoundsAndHapticsSettings.axbundle__SoundsAndHapticsSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Sports-Assistant.axbundle/Sports-Assistant`](System__Library__AccessibilityBundles__Sports-Assistant.axbundle__Sports-Assistant.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Spotlight.axbundle/Spotlight`](System__Library__AccessibilityBundles__Spotlight.axbundle__Spotlight.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SpotlightUIInternalFramework.axbundle/SpotlightUIInternalFramework`](System__Library__AccessibilityBundles__SpotlightUIInternalFramework.axbundle__SpotlightUIInternalFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SpringBoardFoundation.axbundle/SpringBoardFoundation`](System__Library__AccessibilityBundles__SpringBoardFoundation.axbundle__SpringBoardFoundation.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SpringBoardUI.axbundle/SpringBoardUI`](System__Library__AccessibilityBundles__SpringBoardUI.axbundle__SpringBoardUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SpriteKit.axbundle/SpriteKit`](System__Library__AccessibilityBundles__SpriteKit.axbundle__SpriteKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Stocks-Assistant.axbundle/Stocks-Assistant`](System__Library__AccessibilityBundles__Stocks-Assistant.axbundle__Stocks-Assistant.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/StocksFramework.axbundle/StocksFramework`](System__Library__AccessibilityBundles__StocksFramework.axbundle__StocksFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/StocksWidget.axbundle/StocksWidget`](System__Library__AccessibilityBundles__StocksWidget.axbundle__StocksWidget.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/StorageSettings.axbundle/StorageSettings`](System__Library__AccessibilityBundles__StorageSettings.axbundle__StorageSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/StorageSettingsFramework.axbundle/StorageSettingsFramework`](System__Library__AccessibilityBundles__StorageSettingsFramework.axbundle__StorageSettingsFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/StoreKitFramework.axbundle/StoreKitFramework`](System__Library__AccessibilityBundles__StoreKitFramework.axbundle__StoreKitFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/StoreKitUI.axbundle/StoreKitUI`](System__Library__AccessibilityBundles__StoreKitUI.axbundle__StoreKitUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SubscribePageExtension.axbundle/SubscribePageExtension`](System__Library__AccessibilityBundles__SubscribePageExtension.axbundle__SubscribePageExtension.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/System-Assistant.axbundle/System-Assistant`](System__Library__AccessibilityBundles__System-Assistant.axbundle__System-Assistant.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SystemStatusUI.axbundle/SystemStatusUI`](System__Library__AccessibilityBundles__SystemStatusUI.axbundle__SystemStatusUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/TV.axbundle/TV`](System__Library__AccessibilityBundles__TV.axbundle__TV.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/TVMLKit.axbundle/TVMLKit`](System__Library__AccessibilityBundles__TVMLKit.axbundle__TVMLKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/TVRemoteModule.axbundle/TVRemoteModule`](System__Library__AccessibilityBundles__TVRemoteModule.axbundle__TVRemoteModule.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/TVRemoteUI.axbundle/TVRemoteUI`](System__Library__AccessibilityBundles__TVRemoteUI.axbundle__TVRemoteUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/TVRemoteUIService.axbundle/TVRemoteUIService`](System__Library__AccessibilityBundles__TVRemoteUIService.axbundle__TVRemoteUIService.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/TelephonyUIFramework.axbundle/TelephonyUIFramework`](System__Library__AccessibilityBundles__TelephonyUIFramework.axbundle__TelephonyUIFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/TemplateKit.axbundle/TemplateKit`](System__Library__AccessibilityBundles__TemplateKit.axbundle__TemplateKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/TimerModule.axbundle/TimerModule`](System__Library__AccessibilityBundles__TimerModule.axbundle__TimerModule.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/TipsApp.axbundle/TipsApp`](System__Library__AccessibilityBundles__TipsApp.axbundle__TipsApp.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/TipsNotificationExtension.axbundle/TipsNotificationExtension`](System__Library__AccessibilityBundles__TipsNotificationExtension.axbundle__TipsNotificationExtension.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/TipsWidgetExtension.axbundle/TipsWidgetExtension`](System__Library__AccessibilityBundles__TipsWidgetExtension.axbundle__TipsWidgetExtension.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Translate.axbundle/Translate`](System__Library__AccessibilityBundles__Translate.axbundle__Translate.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/TwitterFramework.axbundle/TwitterFramework`](System__Library__AccessibilityBundles__TwitterFramework.axbundle__TwitterFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/UpNext.axbundle/UpNext`](System__Library__AccessibilityBundles__UpNext.axbundle__UpNext.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/UsageSettings.axbundle/UsageSettings`](System__Library__AccessibilityBundles__UsageSettings.axbundle__UsageSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/UserNotificationsUI.axbundle/UserNotificationsUI`](System__Library__AccessibilityBundles__UserNotificationsUI.axbundle__UserNotificationsUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/VictoriaSettings.axbundle/VictoriaSettings`](System__Library__AccessibilityBundles__VictoriaSettings.axbundle__VictoriaSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Videos.axbundle/Videos`](System__Library__AccessibilityBundles__Videos.axbundle__Videos.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/VideosExtrasFramework.axbundle/VideosExtrasFramework`](System__Library__AccessibilityBundles__VideosExtrasFramework.axbundle__VideosExtrasFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/VoiceShortcutsUI.axbundle/VoiceShortcutsUI`](System__Library__AccessibilityBundles__VoiceShortcutsUI.axbundle__VoiceShortcutsUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/VolumeLimitSettings.axbundle/VolumeLimitSettings`](System__Library__AccessibilityBundles__VolumeLimitSettings.axbundle__VolumeLimitSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/WAAnswer-Assistant.axbundle/WAAnswer-Assistant`](System__Library__AccessibilityBundles__WAAnswer-Assistant.axbundle__WAAnswer-Assistant.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Wallpaper.axbundle/Wallpaper`](System__Library__AccessibilityBundles__Wallpaper.axbundle__Wallpaper.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/WallpaperSettings.axbundle/WallpaperSettings`](System__Library__AccessibilityBundles__WallpaperSettings.axbundle__WallpaperSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Weather.axbundle/Weather`](System__Library__AccessibilityBundles__Weather.axbundle__Weather.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/WebCore.axbundle/WebCore`](System__Library__AccessibilityBundles__WebCore.axbundle__WebCore.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/WebKit.axbundle/WebKit`](System__Library__AccessibilityBundles__WebKit.axbundle__WebKit.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/WebKitLegacy.axbundle/WebKitLegacy`](System__Library__AccessibilityBundles__WebKitLegacy.axbundle__WebKitLegacy.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/WebProcess.axbundle/WebProcess`](System__Library__AccessibilityBundles__WebProcess.axbundle__WebProcess.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/WebUI.axbundle/WebUI`](System__Library__AccessibilityBundles__WebUI.axbundle__WebUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/WiFiKitUI.axbundle/WiFiKitUI`](System__Library__AccessibilityBundles__WiFiKitUI.axbundle__WiFiKitUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/WidgetConfigurationExtension.axbundle/WidgetConfigurationExtension`](System__Library__AccessibilityBundles__WidgetConfigurationExtension.axbundle__WidgetConfigurationExtension.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/Widgets.axbundle/Widgets`](System__Library__AccessibilityBundles__Widgets.axbundle__Widgets.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/WirelessModemSettings.axbundle/WirelessModemSettings`](System__Library__AccessibilityBundles__WirelessModemSettings.axbundle__WirelessModemSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/WorkflowEditor.axbundle/WorkflowEditor`](System__Library__AccessibilityBundles__WorkflowEditor.axbundle__WorkflowEditor.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/WorkflowUI.axbundle/WorkflowUI`](System__Library__AccessibilityBundles__WorkflowUI.axbundle__WorkflowUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/WritingToolsUIService.axbundle/WritingToolsUIService`](System__Library__AccessibilityBundles__WritingToolsUIService.axbundle__WritingToolsUIService.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/com.apple.CloudDocsUI.CloudSharing-AppExtension.axbundle/com.apple.CloudDocsUI.CloudSharing-AppExtension`](System__Library__AccessibilityBundles__com.apple.CloudDocsUI.CloudSharing-AppExtension.axbundle__com.apple.CloudDocsUI.CloudSharing-AppExtension.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/com.apple.DocumentManager.Service-AppExtension.axbundle/com.apple.DocumentManager.Service-AppExtension`](System__Library__AccessibilityBundles__com.apple.DocumentManager.Service-AppExtension.axbundle__com.apple.DocumentManager.Service-AppExtension.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/iAdFramework.axbundle/iAdFramework`](System__Library__AccessibilityBundles__iAdFramework.axbundle__iAdFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/iCloudDriveApp.axbundle/iCloudDriveApp`](System__Library__AccessibilityBundles__iCloudDriveApp.axbundle__iCloudDriveApp.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/iTunesStoreFramework.axbundle/iTunesStoreFramework`](System__Library__AccessibilityBundles__iTunesStoreFramework.axbundle__iTunesStoreFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/iTunesStoreUIFramework.axbundle/iTunesStoreUIFramework`](System__Library__AccessibilityBundles__iTunesStoreUIFramework.axbundle__iTunesStoreUIFramework.md) | 3050.3.8.0.0 | light |
| [`/System/Library/Accounts/Access/CloudKitAccessPlugin.bundle/CloudKitAccessPlugin`](System__Library__Accounts__Access__CloudKitAccessPlugin.bundle__CloudKitAccessPlugin.md) | 2720.17.6.0.0 | light |
| [`/System/Library/Accounts/Access/DefaultAccessPlugin.bundle/DefaultAccessPlugin`](System__Library__Accounts__Access__DefaultAccessPlugin.bundle__DefaultAccessPlugin.md) | 1125.0.0.0.0 | light |
| [`/System/Library/Accounts/Access/YelpAccessPlugin.bundle/YelpAccessPlugin`](System__Library__Accounts__Access__YelpAccessPlugin.bundle__YelpAccessPlugin.md) | 1125.0.0.0.0 | light |
| [`/System/Library/Accounts/Authentication/AMSAccountAuthenticationPlugin.bundle/AMSAccountAuthenticationPlugin`](System__Library__Accounts__Authentication__AMSAccountAuthenticationPlugin.bundle__AMSAccountAuthenticationPlugin.md) | 10.1.18.2.1 | light |
| [`/System/Library/Accounts/Authentication/AppleIDAuthentication.bundle/AppleIDAuthentication`](System__Library__Accounts__Authentication__AppleIDAuthentication.bundle__AppleIDAuthentication.md) | 1069.125.7.0.0 | light |
| [`/System/Library/Accounts/Authentication/AppleIDSSOAuthenticationPlugin.bundle/AppleIDSSOAuthenticationPlugin`](System__Library__Accounts__Authentication__AppleIDSSOAuthenticationPlugin.bundle__AppleIDSSOAuthenticationPlugin.md) | 118.125.2.0.0 | light |
| [`/System/Library/Accounts/Authentication/CloudKitAuthenticationPlugin.bundle/CloudKitAuthenticationPlugin`](System__Library__Accounts__Authentication__CloudKitAuthenticationPlugin.bundle__CloudKitAuthenticationPlugin.md) | 2720.17.6.0.0 | light |
| [`/System/Library/Accounts/Authentication/DAAccountAuthenticator.bundle/DAAccountAuthenticator`](System__Library__Accounts__Authentication__DAAccountAuthenticator.bundle__DAAccountAuthenticator.md) | 2708.2.3.0.0 | light |
| [`/System/Library/Accounts/Authentication/ESAccountAuthenticator.bundle/ESAccountAuthenticator`](System__Library__Accounts__Authentication__ESAccountAuthenticator.bundle__ESAccountAuthenticator.md) | 2079.200.41.0.0 | light |
| [`/System/Library/Accounts/Authentication/GoogleAuthenticationPlugin.bundle/GoogleAuthenticationPlugin`](System__Library__Accounts__Authentication__GoogleAuthenticationPlugin.bundle__GoogleAuthenticationPlugin.md) | 774.0.0.0.0 | light |
| [`/System/Library/Accounts/Authentication/KerberosAuthenticationPlugin.bundle/KerberosAuthenticationPlugin`](System__Library__Accounts__Authentication__KerberosAuthenticationPlugin.bundle__KerberosAuthenticationPlugin.md) | 1125.0.0.0.0 | light |
| [`/System/Library/Accounts/Authentication/MessageAccountAuthenticationPlugin.bundle/MessageAccountAuthenticationPlugin`](System__Library__Accounts__Authentication__MessageAccountAuthenticationPlugin.bundle__MessageAccountAuthenticationPlugin.md) | 3901.200.71.21.4 | light |
| [`/System/Library/Accounts/Authentication/YahooAuthenticationPlugin.bundle/YahooAuthenticationPlugin`](System__Library__Accounts__Authentication__YahooAuthenticationPlugin.bundle__YahooAuthenticationPlugin.md) | 774.0.0.0.0 | light |
| [`/System/Library/Accounts/Notification/AAAccountNotificationPlugin.bundle/AAAccountNotificationPlugin`](System__Library__Accounts__Notification__AAAccountNotificationPlugin.bundle__AAAccountNotificationPlugin.md) | 1069.125.7.0.0 | light |
| [`/System/Library/Accounts/Notification/AADataclassEnableNotificationPlugin.bundle/AADataclassEnableNotificationPlugin`](System__Library__Accounts__Notification__AADataclassEnableNotificationPlugin.bundle__AADataclassEnableNotificationPlugin.md) | 1069.125.7.0.0 | light |
| [`/System/Library/Accounts/Notification/AAIDMSAccountNotificationPlugin.bundle/AAIDMSAccountNotificationPlugin`](System__Library__Accounts__Notification__AAIDMSAccountNotificationPlugin.bundle__AAIDMSAccountNotificationPlugin.md) | 1069.125.7.0.0 | light |
| [`/System/Library/Accounts/Notification/ACDatabaseBackupNotificationPlugin.bundle/ACDatabaseBackupNotificationPlugin`](System__Library__Accounts__Notification__ACDatabaseBackupNotificationPlugin.bundle__ACDatabaseBackupNotificationPlugin.md) | 1125.0.0.0.0 | light |
| [`/System/Library/Accounts/Notification/ADAccountsNotificationPlugin.bundle/ADAccountsNotificationPlugin`](System__Library__Accounts__Notification__ADAccountsNotificationPlugin.bundle__ADAccountsNotificationPlugin.md) | 638.2.3.0.0 | light |
| [`/System/Library/Accounts/Notification/AISAccountNotificationPlugin.bundle/AISAccountNotificationPlugin`](System__Library__Accounts__Notification__AISAccountNotificationPlugin.bundle__AISAccountNotificationPlugin.md) | 129.125.7.1.0 | light |
| [`/System/Library/Accounts/Notification/AKAccountNotificationPlugin.bundle/AKAccountNotificationPlugin`](System__Library__Accounts__Notification__AKAccountNotificationPlugin.bundle__AKAccountNotificationPlugin.md) | 560.125.6.1.0 | light |
| [`/System/Library/Accounts/Notification/AMSAccountNotificationPlugin.bundle/AMSAccountNotificationPlugin`](System__Library__Accounts__Notification__AMSAccountNotificationPlugin.bundle__AMSAccountNotificationPlugin.md) | 10.1.18.2.1 | light |
| [`/System/Library/Accounts/Notification/AMSAccountSyncNotificationPlugin.bundle/AMSAccountSyncNotificationPlugin`](System__Library__Accounts__Notification__AMSAccountSyncNotificationPlugin.bundle__AMSAccountSyncNotificationPlugin.md) | 10.1.18.2.1 | light |
| [`/System/Library/Accounts/Notification/ASDAccountNotficationPlugin.bundle/ASDAccountNotficationPlugin`](System__Library__Accounts__Notification__ASDAccountNotficationPlugin.bundle__ASDAccountNotficationPlugin.md) | 13.1.17.0.0 | light |
| [`/System/Library/Accounts/Notification/AppleIDSSONotificationPlugin.bundle/AppleIDSSONotificationPlugin`](System__Library__Accounts__Notification__AppleIDSSONotificationPlugin.bundle__AppleIDSSONotificationPlugin.md) | 118.125.2.0.0 | light |
| [`/System/Library/Accounts/Notification/BTCloudPairingAccountNotificationPlugin.bundle/BTCloudPairingAccountNotificationPlugin`](System__Library__Accounts__Notification__BTCloudPairingAccountNotificationPlugin.bundle__BTCloudPairingAccountNotificationPlugin.md) | 41.7.0.0.0 | light |
| [`/System/Library/Accounts/Notification/CDPAccountNotificationPlugin_IOS.bundle/CDPAccountNotificationPlugin_IOS`](System__Library__Accounts__Notification__CDPAccountNotificationPlugin_IOS.bundle__CDPAccountNotificationPlugin_IOS.md) | 448.125.10.0.0 | light |
| [`/System/Library/Accounts/Notification/ClassKitAccountNotificationPlugin.bundle/ClassKitAccountNotificationPlugin`](System__Library__Accounts__Notification__ClassKitAccountNotificationPlugin.bundle__ClassKitAccountNotificationPlugin.md) | 152.1.1.0.0 | light |
| [`/System/Library/Accounts/Notification/CloudKitNotificationPlugin.bundle/CloudKitNotificationPlugin`](System__Library__Accounts__Notification__CloudKitNotificationPlugin.bundle__CloudKitNotificationPlugin.md) | 2720.17.6.0.0 | light |
| [`/System/Library/Accounts/Notification/CoreLocationAccountNotificationPlugin.bundle/CoreLocationAccountNotificationPlugin`](System__Library__Accounts__Notification__CoreLocationAccountNotificationPlugin.bundle__CoreLocationAccountNotificationPlugin.md) | 3187.0.1.0.0 | full |
| [`/System/Library/Accounts/Notification/CoreRecentsAccountNotificationPlugin.bundle/CoreRecentsAccountNotificationPlugin`](System__Library__Accounts__Notification__CoreRecentsAccountNotificationPlugin.bundle__CoreRecentsAccountNotificationPlugin.md) | 1237.200.31.0.0 | light |
| [`/System/Library/Accounts/Notification/DAAccountNotifier.bundle/DAAccountNotifier`](System__Library__Accounts__Notification__DAAccountNotifier.bundle__DAAccountNotifier.md) | 2708.2.3.0.0 | light |
| [`/System/Library/Accounts/Notification/DMDAccountNotificationPlugin.bundle/DMDAccountNotificationPlugin`](System__Library__Accounts__Notification__DMDAccountNotificationPlugin.bundle__DMDAccountNotificationPlugin.md) | 267.0.0.0.0 | light |
| [`/System/Library/Accounts/Notification/DonationAccountWatcher.bundle/DonationAccountWatcher`](System__Library__Accounts__Notification__DonationAccountWatcher.bundle__DonationAccountWatcher.md) | 1130.200.1.0.0 | light |
| [`/System/Library/Accounts/Notification/ESAccountNotifier.bundle/ESAccountNotifier`](System__Library__Accounts__Notification__ESAccountNotifier.bundle__ESAccountNotifier.md) | 2079.200.41.0.0 | light |
| [`/System/Library/Accounts/Notification/FMFLocatorAccountNotificationPlugin.bundle/FMFLocatorAccountNotificationPlugin`](System__Library__Accounts__Notification__FMFLocatorAccountNotificationPlugin.bundle__FMFLocatorAccountNotificationPlugin.md) | 103.31.7.12.2 | light |
| [`/System/Library/Accounts/Notification/FindMyDeviceAccountNotificationPlugin.bundle/FindMyDeviceAccountNotificationPlugin`](System__Library__Accounts__Notification__FindMyDeviceAccountNotificationPlugin.bundle__FindMyDeviceAccountNotificationPlugin.md) | 482.31.6.16.21 | light |
| [`/System/Library/Accounts/Notification/GameCenterAccountNotificationPlugin.bundle/GameCenterAccountNotificationPlugin`](System__Library__Accounts__Notification__GameCenterAccountNotificationPlugin.bundle__GameCenterAccountNotificationPlugin.md) | 821.1.16.2.1 | light |
| [`/System/Library/Accounts/Notification/HealthKitAccountNotificationPlugin.bundle/HealthKitAccountNotificationPlugin`](System__Library__Accounts__Notification__HealthKitAccountNotificationPlugin.bundle__HealthKitAccountNotificationPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Accounts/Notification/IDSAccountNotificationPlugin.bundle/IDSAccountNotificationPlugin`](System__Library__Accounts__Notification__IDSAccountNotificationPlugin.bundle__IDSAccountNotificationPlugin.md) | 2003.200.71.2.4 | light |
| [`/System/Library/Accounts/Notification/IMAccountNotificationPlugin.bundle/IMAccountNotificationPlugin`](System__Library__Accounts__Notification__IMAccountNotificationPlugin.bundle__IMAccountNotificationPlugin.md) | 1491.200.101.21.5 | light |
| [`/System/Library/Accounts/Notification/INDAccountNotificationPlugin.bundle/INDAccountNotificationPlugin`](System__Library__Accounts__Notification__INDAccountNotificationPlugin.bundle__INDAccountNotificationPlugin.md) | 301.24.1.5.0 | light |
| [`/System/Library/Accounts/Notification/KeychainSyncAccountNotification.bundle/KeychainSyncAccountNotification`](System__Library__Accounts__Notification__KeychainSyncAccountNotification.bundle__KeychainSyncAccountNotification.md) | 62460.40.78.0.0 | full |
| [`/System/Library/Accounts/Notification/LockdownModeAccountNotificationPlugin.bundle/LockdownModeAccountNotificationPlugin`](System__Library__Accounts__Notification__LockdownModeAccountNotificationPlugin.bundle__LockdownModeAccountNotificationPlugin.md) | 128.40.5.0.0 | light |
| [`/System/Library/Accounts/Notification/MessageAccountNotificationPlugin.bundle/MessageAccountNotificationPlugin`](System__Library__Accounts__Notification__MessageAccountNotificationPlugin.bundle__MessageAccountNotificationPlugin.md) | 3901.200.71.21.4 | light |
| [`/System/Library/Accounts/Notification/MobileSyncAccountNotificationPlugin.bundle/MobileSyncAccountNotificationPlugin`](System__Library__Accounts__Notification__MobileSyncAccountNotificationPlugin.bundle__MobileSyncAccountNotificationPlugin.md) | 1025.0.0.0.0 | light |
| [`/System/Library/Accounts/Notification/NewsNotificationPlugin.bundle/NewsNotificationPlugin`](System__Library__Accounts__Notification__NewsNotificationPlugin.bundle__NewsNotificationPlugin.md) | 5971.1.0.0.0 | light |
| [`/System/Library/Accounts/Notification/NotesAccountNotificationPlugin.bundle/NotesAccountNotificationPlugin`](System__Library__Accounts__Notification__NotesAccountNotificationPlugin.bundle__NotesAccountNotificationPlugin.md) | 3001.42.1.0.0 | light |
| [`/System/Library/Accounts/Notification/PCSAccountNotificationPlugin.bundle/PCSAccountNotificationPlugin`](System__Library__Accounts__Notification__PCSAccountNotificationPlugin.bundle__PCSAccountNotificationPlugin.md) | 1303.40.11.0.0 | light |
| [`/System/Library/Accounts/Notification/PassbookAccountNotificationPlugin.bundle/PassbookAccountNotificationPlugin`](System__Library__Accounts__Notification__PassbookAccountNotificationPlugin.bundle__PassbookAccountNotificationPlugin.md) | 1696.2.9.2.0 | light |
| [`/System/Library/Accounts/Notification/PhotosAccountNotificationPlugin.bundle/PhotosAccountNotificationPlugin`](System__Library__Accounts__Notification__PhotosAccountNotificationPlugin.bundle__PhotosAccountNotificationPlugin.md) | 916.62.154.0.0 | light |
| [`/System/Library/Accounts/Notification/RPAccountNotificationPlugin.bundle/RPAccountNotificationPlugin`](System__Library__Accounts__Notification__RPAccountNotificationPlugin.bundle__RPAccountNotificationPlugin.md) | 751.200.101.0.0 | light |
| [`/System/Library/Accounts/Notification/RemindersAccountNotificationPlugin.bundle/RemindersAccountNotificationPlugin`](System__Library__Accounts__Notification__RemindersAccountNotificationPlugin.bundle__RemindersAccountNotificationPlugin.md) | 4080.0.0.0.0 | light |
| [`/System/Library/Accounts/Notification/SearchPartyAccountNotificationPlugin.bundle/SearchPartyAccountNotificationPlugin`](System__Library__Accounts__Notification__SearchPartyAccountNotificationPlugin.bundle__SearchPartyAccountNotificationPlugin.md) | 449.31.6.16.29 | light |
| [`/System/Library/Accounts/Notification/SecureBackupNotification.bundle/SecureBackupNotification`](System__Library__Accounts__Notification__SecureBackupNotification.bundle__SecureBackupNotification.md) | 747.40.9.0.0 | light |
| [`/System/Library/Accounts/Notification/SharingAccountNotificationPlugin.bundle/SharingAccountNotificationPlugin`](System__Library__Accounts__Notification__SharingAccountNotificationPlugin.bundle__SharingAccountNotificationPlugin.md) | 2131.21.31.21.8 | light |
| [`/System/Library/Accounts/Notification/ShortcutsCloudKitAccountNotificationPlugin.bundle/ShortcutsCloudKitAccountNotificationPlugin`](System__Library__Accounts__Notification__ShortcutsCloudKitAccountNotificationPlugin.bundle__ShortcutsCloudKitAccountNotificationPlugin.md) | 5114.0.12.0.0 | light |
| [`/System/Library/Accounts/Notification/SiriCloudKitAccountsNotifier.bundle/SiriCloudKitAccountsNotifier`](System__Library__Accounts__Notification__SiriCloudKitAccountsNotifier.bundle__SiriCloudKitAccountsNotifier.md) | 3605.31.1.11.2 | light |
| [`/System/Library/Accounts/Notification/SocialAccountNotificationPlugin.bundle/SocialAccountNotificationPlugin`](System__Library__Accounts__Notification__SocialAccountNotificationPlugin.bundle__SocialAccountNotificationPlugin.md) | 774.0.0.0.0 | light |
| [`/System/Library/Accounts/Notification/WebBookmarksNotificationPlugin.bundle/WebBookmarksNotificationPlugin`](System__Library__Accounts__Notification__WebBookmarksNotificationPlugin.bundle__WebBookmarksNotificationPlugin.md) | 7625.2.8.21.6 | light |
| [`/System/Library/Accounts/Notification/StoreKitAccountNotificationPlugin.bundle/StoreKitAccountNotificationPlugin`](System__Library__Accounts__Notification__StoreKitAccountNotificationPlugin.bundle__StoreKitAccountNotificationPlugin.md) | 816.1.16.0.0 | light |
| [`/System/Library/Accounts/Notification/com.apple.askpermission.AccountNotificationPlugin.bundle/com.apple.askpermission.AccountNotificationPlugin`](System__Library__Accounts__Notification__com.apple.askpermission.AccountNotificationPlugin.bundle__com.apple.askpermission.AccountNotificationPlugin.md) | 130.1.7.2.2 | light |
| [`/System/Library/Assistant/Plugins/AssistantTTSPlugin.assistantBundle/AssistantTTSPlugin`](System__Library__Assistant__Plugins__AssistantTTSPlugin.assistantBundle__AssistantTTSPlugin.md) | 3600.12.2.0.0 | light |
| [`/System/Library/Assistant/Plugins/Calendar.assistantBundle/Calendar`](System__Library__Assistant__Plugins__Calendar.assistantBundle__Calendar.md) | 919.0.0.0.0 | light |
| [`/System/Library/Assistant/Plugins/Contacts.assistantBundle/Contacts`](System__Library__Assistant__Plugins__Contacts.assistantBundle__Contacts.md) | 29.0.0.0.0 | light |
| [`/System/Library/Assistant/Plugins/CorrectionsProfilesSync.assistantBundle/CorrectionsProfilesSync`](System__Library__Assistant__Plugins__CorrectionsProfilesSync.assistantBundle__CorrectionsProfilesSync.md) | 3605.31.1.11.2 | light |
| [`/System/Library/Assistant/Plugins/GEO.assistantBundle/GEO`](System__Library__Assistant__Plugins__GEO.assistantBundle__GEO.md) | 2076.31.9.18.106 | light |
| [`/System/Library/Assistant/Plugins/HMAssistant.assistantBundle/HMAssistant`](System__Library__Assistant__Plugins__HMAssistant.assistantBundle__HMAssistant.md) | 1520.2.7.1.3 | light |
| [`/System/Library/Assistant/Plugins/LocaleSettings.assistantBundle/LocaleSettings`](System__Library__Assistant__Plugins__LocaleSettings.assistantBundle__LocaleSettings.md) | 3605.31.1.11.2 | light |
| [`/System/Library/Assistant/Plugins/Media.assistantBundle/Media`](System__Library__Assistant__Plugins__Media.assistantBundle__Media.md) | 4026.210.1.0.0 | light |
| [`/System/Library/Assistant/Plugins/Phone.assistantBundle/Phone`](System__Library__Assistant__Plugins__Phone.assistantBundle__Phone.md) | 3079.200.81.21.2 | light |
| [`/System/Library/Assistant/Plugins/Podcasts.assistantBundle/Podcasts`](System__Library__Assistant__Plugins__Podcasts.assistantBundle__Podcasts.md) | 4027.210.1.0.0 | light |
| [`/System/Library/Assistant/Plugins/Routine.assistantBundle/Routine`](System__Library__Assistant__Plugins__Routine.assistantBundle__Routine.md) | 1123.0.3.0.0 | light |
| [`/System/Library/Assistant/Plugins/SynapseSyncPlugin.assistantBundle/SynapseSyncPlugin`](System__Library__Assistant__Plugins__SynapseSyncPlugin.assistantBundle__SynapseSyncPlugin.md) | 3605.31.1.11.2 | light |
| [`/System/Library/Assistant/UIPlugins/SiriFindMyUIPlugin.siriUIBundle/Frameworks/SiriFindMyUI.framework/SiriFindMyUI`](System__Library__Assistant__UIPlugins__SiriFindMyUIPlugin.siriUIBundle__Frameworks__SiriFindMyUI.framework__SiriFindMyUI.md) | 3605.19.1.0.0 | light |
| [`/System/Library/ControlCenter/Bundles/AccessibilityHeadphoneLevelsControlCenterModule.bundle/AccessibilityHeadphoneLevelsControlCenterModule`](System__Library__ControlCenter__Bundles__AccessibilityHeadphoneLevelsControlCenterModule.bundle__AccessibilityHeadphoneLevelsControlCenterModule.md) | 3245.8.9.0.0 | light |
| [`/System/Library/ControlCenter/Bundles/AccessibilityLiveListenControlCenterModule.bundle/AccessibilityLiveListenControlCenterModule`](System__Library__ControlCenter__Bundles__AccessibilityLiveListenControlCenterModule.bundle__AccessibilityLiveListenControlCenterModule.md) | 3245.8.9.0.0 | light |
| [`/System/Library/ControlCenter/Bundles/AccessibilityMotionCuesControlCenterModule.bundle/AccessibilityMotionCuesControlCenterModule`](System__Library__ControlCenter__Bundles__AccessibilityMotionCuesControlCenterModule.bundle__AccessibilityMotionCuesControlCenterModule.md) | 3245.8.9.0.0 | light |
| [`/System/Library/ControlCenter/Bundles/AccessibilityNoiseLevelsControlCenterModule.bundle/AccessibilityNoiseLevelsControlCenterModule`](System__Library__ControlCenter__Bundles__AccessibilityNoiseLevelsControlCenterModule.bundle__AccessibilityNoiseLevelsControlCenterModule.md) | 3245.8.9.0.0 | light |
| [`/System/Library/ControlCenter/Bundles/AccessibilityShorcutsModule.bundle/AccessibilityShorcutsModule`](System__Library__ControlCenter__Bundles__AccessibilityShorcutsModule.bundle__AccessibilityShorcutsModule.md) | 3245.8.9.0.0 | light |
| [`/System/Library/ControlCenter/Bundles/AccessibilitySoundDetectionControlCenterModule.bundle/AccessibilitySoundDetectionControlCenterModule`](System__Library__ControlCenter__Bundles__AccessibilitySoundDetectionControlCenterModule.bundle__AccessibilitySoundDetectionControlCenterModule.md) | 3245.8.9.0.0 | light |
| [`/System/Library/ControlCenter/Bundles/AccessibilityTextSizeModule.bundle/AccessibilityTextSizeModule`](System__Library__ControlCenter__Bundles__AccessibilityTextSizeModule.bundle__AccessibilityTextSizeModule.md) | 3245.8.9.0.0 | light |
| [`/System/Library/ControlCenter/Bundles/AirPlayMirroringModule.bundle/AirPlayMirroringModule`](System__Library__ControlCenter__Bundles__AirPlayMirroringModule.bundle__AirPlayMirroringModule.md) | 4026.210.4.0.0 | light |
| [`/System/Library/ControlCenter/Bundles/AlarmModule.bundle/AlarmModule`](System__Library__ControlCenter__Bundles__AlarmModule.bundle__AlarmModule.md) | 704.2.4.0.3 | light |
| [`/System/Library/ControlCenter/Bundles/AppearanceModule.bundle/AppearanceModule`](System__Library__ControlCenter__Bundles__AppearanceModule.bundle__AppearanceModule.md) | 704.2.4.0.3 | light |
| [`/System/Library/ControlCenter/Bundles/BackgroundSoundsCCModule.bundle/BackgroundSoundsCCModule`](System__Library__ControlCenter__Bundles__BackgroundSoundsCCModule.bundle__BackgroundSoundsCCModule.md) | 3245.8.9.0.0 | light |
| [`/System/Library/ControlCenter/Bundles/CalculatorModule.bundle/CalculatorModule`](System__Library__ControlCenter__Bundles__CalculatorModule.bundle__CalculatorModule.md) | 704.2.4.0.3 | light |
| [`/System/Library/ControlCenter/Bundles/CameraModule.bundle/CameraModule`](System__Library__ControlCenter__Bundles__CameraModule.bundle__CameraModule.md) | 704.2.4.0.3 | full |
| [`/System/Library/ControlCenter/Bundles/ConnectivityModule.bundle/ConnectivityModule`](System__Library__ControlCenter__Bundles__ConnectivityModule.bundle__ConnectivityModule.md) | 704.2.4.0.3 | light |
| [`/System/Library/ControlCenter/Bundles/DisplayModule.bundle/DisplayModule`](System__Library__ControlCenter__Bundles__DisplayModule.bundle__DisplayModule.md) | 704.2.4.0.3 | full |
| [`/System/Library/ControlCenter/Bundles/FeedbackAssistantModule.bundle/FeedbackAssistantModule`](System__Library__ControlCenter__Bundles__FeedbackAssistantModule.bundle__FeedbackAssistantModule.md) | 704.2.4.0.3 | light |
| [`/System/Library/ControlCenter/Bundles/FlashlightModule.bundle/FlashlightModule`](System__Library__ControlCenter__Bundles__FlashlightModule.bundle__FlashlightModule.md) | 704.2.4.0.3 | full |
| [`/System/Library/ControlCenter/Bundles/HeadphoneAccommodationsCCModule.bundle/HeadphoneAccommodationsCCModule`](System__Library__ControlCenter__Bundles__HeadphoneAccommodationsCCModule.bundle__HeadphoneAccommodationsCCModule.md) | 3245.8.9.0.0 | light |
| [`/System/Library/ControlCenter/Bundles/HearingAidsModule.bundle/HearingAidsModule`](System__Library__ControlCenter__Bundles__HearingAidsModule.bundle__HearingAidsModule.md) | 3245.8.9.0.0 | light |
| [`/System/Library/ControlCenter/Bundles/HearingDevicesCCModule.bundle/HearingDevicesCCModule`](System__Library__ControlCenter__Bundles__HearingDevicesCCModule.bundle__HearingDevicesCCModule.md) | 3245.8.9.0.0 | light |
| [`/System/Library/ControlCenter/Bundles/HomeControlCenterModule.bundle/HomeControlCenterModule`](System__Library__ControlCenter__Bundles__HomeControlCenterModule.bundle__HomeControlCenterModule.md) | 1269.2.5.6.6 | light |
| [`/System/Library/ControlCenter/Bundles/HomeControlCenterSingleTileModule.bundle/HomeControlCenterSingleTileModule`](System__Library__ControlCenter__Bundles__HomeControlCenterSingleTileModule.bundle__HomeControlCenterSingleTileModule.md) | 1269.2.5.6.6 | light |
| [`/System/Library/ControlCenter/Bundles/KeyboardBrightnessModule.bundle/KeyboardBrightnessModule`](System__Library__ControlCenter__Bundles__KeyboardBrightnessModule.bundle__KeyboardBrightnessModule.md) | 9127.1.13.7.0 | full |
| [`/System/Library/ControlCenter/Bundles/LowPowerModule.bundle/LowPowerModule`](System__Library__ControlCenter__Bundles__LowPowerModule.bundle__LowPowerModule.md) | 704.2.4.0.3 | light |
| [`/System/Library/ControlCenter/Bundles/MagnifierModule.bundle/MagnifierModule`](System__Library__ControlCenter__Bundles__MagnifierModule.bundle__MagnifierModule.md) | 704.2.4.0.3 | light |
| [`/System/Library/ControlCenter/Bundles/MediaControlsAudioModule.bundle/MediaControlsAudioModule`](System__Library__ControlCenter__Bundles__MediaControlsAudioModule.bundle__MediaControlsAudioModule.md) | 4026.210.4.0.0 | light |
| [`/System/Library/ControlCenter/Bundles/MediaControlsModule.bundle/MediaControlsModule`](System__Library__ControlCenter__Bundles__MediaControlsModule.bundle__MediaControlsModule.md) | 4026.210.4.0.0 | light |
| [`/System/Library/ControlCenter/Bundles/MuteModule.bundle/MuteModule`](System__Library__ControlCenter__Bundles__MuteModule.bundle__MuteModule.md) | 704.2.4.0.3 | light |
| [`/System/Library/ControlCenter/Bundles/OrientationLockModule.bundle/OrientationLockModule`](System__Library__ControlCenter__Bundles__OrientationLockModule.bundle__OrientationLockModule.md) | 704.2.4.0.3 | light |
| [`/System/Library/ControlCenter/Bundles/PerformanceTraceModule.bundle/PerformanceTraceModule`](System__Library__ControlCenter__Bundles__PerformanceTraceModule.bundle__PerformanceTraceModule.md) | 704.2.4.0.3 | light |
| [`/System/Library/ControlCenter/Bundles/QRCodeModule.bundle/QRCodeModule`](System__Library__ControlCenter__Bundles__QRCodeModule.bundle__QRCodeModule.md) | 704.2.4.0.3 | light |
| [`/System/Library/ControlCenter/Bundles/QuickNoteModule.bundle/QuickNoteModule`](System__Library__ControlCenter__Bundles__QuickNoteModule.bundle__QuickNoteModule.md) | 3001.42.1.0.0 | light |
| [`/System/Library/ControlCenter/Bundles/ShazamModule.bundle/ShazamModule`](System__Library__ControlCenter__Bundles__ShazamModule.bundle__ShazamModule.md) | 427.2.6.0.0 | light |
| [`/System/Library/ControlCenter/Bundles/SpokenNotificationsModule.bundle/SpokenNotificationsModule`](System__Library__ControlCenter__Bundles__SpokenNotificationsModule.bundle__SpokenNotificationsModule.md) | 3605.23.2.3.0 | light |
| [`/System/Library/ControlCenter/Bundles/StopwatchModule.bundle/StopwatchModule`](System__Library__ControlCenter__Bundles__StopwatchModule.bundle__StopwatchModule.md) | 704.2.4.0.3 | light |
| [`/System/Library/ControlCenter/Bundles/TVRemoteModule.bundle/TVRemoteModule`](System__Library__ControlCenter__Bundles__TVRemoteModule.bundle__TVRemoteModule.md) | 627.11.4.0.0 | light |
| [`/System/Library/ControlCenter/Bundles/TimerModule.bundle/TimerModule`](System__Library__ControlCenter__Bundles__TimerModule.bundle__TimerModule.md) | 308.2.7.0.0 | light |
| [`/System/Library/ControlCenter/Bundles/VoiceMemosModule.bundle/VoiceMemosModule`](System__Library__ControlCenter__Bundles__VoiceMemosModule.bundle__VoiceMemosModule.md) | 704.2.4.0.3 | light |
| [`/System/Library/ControlCenter/Bundles/WalletModule.bundle/WalletModule`](System__Library__ControlCenter__Bundles__WalletModule.bundle__WalletModule.md) | 704.2.4.0.3 | light |
| [`/System/Library/CoreAccessories/PlugIns/Features/AssistiveTouch-iOS.feature/AssistiveTouch-iOS`](System__Library__CoreAccessories__PlugIns__Features__AssistiveTouch-iOS.feature__AssistiveTouch-iOS.md) | 1219.52.1.0.0 | light |
| [`/System/Library/CoreAccessories/PlugIns/Features/BLEPairing-iOS.feature/BLEPairing-iOS`](System__Library__CoreAccessories__PlugIns__Features__BLEPairing-iOS.feature__BLEPairing-iOS.md) | 1219.52.1.0.0 | light |
| [`/System/Library/CoreAccessories/PlugIns/Features/Communications-iOS.feature/Communications-iOS`](System__Library__CoreAccessories__PlugIns__Features__Communications-iOS.feature__Communications-iOS.md) | 1219.52.1.0.0 | light |
| [`/System/Library/CoreAccessories/PlugIns/Features/HID.feature/HID`](System__Library__CoreAccessories__PlugIns__Features__HID.feature__HID.md) | 1219.52.1.0.0 | full |
| [`/System/Library/CoreAccessories/PlugIns/Features/Navigation-iOS.feature/Navigation-iOS`](System__Library__CoreAccessories__PlugIns__Features__Navigation-iOS.feature__Navigation-iOS.md) | 1219.52.1.0.0 | light |
| [`/System/Library/CoreAccessories/PlugIns/Features/OOBBTPairing-iOS.feature/OOBBTPairing-iOS`](System__Library__CoreAccessories__PlugIns__Features__OOBBTPairing-iOS.feature__OOBBTPairing-iOS.md) | 1219.52.1.0.0 | light |
| [`/System/Library/CoreAccessories/PlugIns/Platform/IOKit.platform/IOKit`](System__Library__CoreAccessories__PlugIns__Platform__IOKit.platform__IOKit.md) | 1219.52.1.0.0 | full |
| [`/System/Library/CoreAccessories/PlugIns/Platform/Platform-Bluetooth.platform/Platform-Bluetooth`](System__Library__CoreAccessories__PlugIns__Platform__Platform-Bluetooth.platform__Platform-Bluetooth.md) | 1219.52.1.0.0 | full |
| [`/System/Library/CoreAccessories/PlugIns/Platform/System.platform/System`](System__Library__CoreAccessories__PlugIns__Platform__System.platform__System.md) | 1219.52.1.0.0 | light |
| [`/System/Library/CoreAccessories/PlugIns/Platform/WiFiSharing.platform/WiFiSharing`](System__Library__CoreAccessories__PlugIns__Platform__WiFiSharing.platform__WiFiSharing.md) | 1219.52.1.0.0 | full |
| [`/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager`](System__Library__CoreAccessories__PlugIns__Transports__IOAccessoryManager.transport__IOAccessoryManager.md) | 1219.52.1.0.0 | full |
| [`/System/Library/CoreAccessories/PlugIns/Transports/NFC.transport/NFC`](System__Library__CoreAccessories__PlugIns__Transports__NFC.transport__NFC.md) | 1219.52.1.0.0 | full |
| [`/System/Library/CoreAccessories/PlugIns/Transports/USBHost.transport/USBHost`](System__Library__CoreAccessories__PlugIns__Transports__USBHost.transport__USBHost.md) | 1219.52.1.0.0 | full |
| [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](System__Library__CoreServices__RawCamera.bundle__RawCamera.md) | 1821.40.6.0.0 | full |
| [`/System/Library/DataClassMigrators/DAAccount.migrator/DAAccount`](System__Library__DataClassMigrators__DAAccount.migrator__DAAccount.md) | 2708.2.3.0.0 | light |
| [`/System/Library/DataClassMigrators/FaceTimeMigrator.migrator/FaceTimeMigrator`](System__Library__DataClassMigrators__FaceTimeMigrator.migrator__FaceTimeMigrator.md) | 2003.200.71.2.4 | light |
| [`/System/Library/DataClassMigrators/MessagesDataMigrator.migrator/MessagesDataMigrator`](System__Library__DataClassMigrators__MessagesDataMigrator.migrator__MessagesDataMigrator.md) | 1491.200.101.21.5 | light |
| [`/System/Library/DigitalSeparation/SharingSources/PasswordsDigitalSeparation.bundle/PasswordsDigitalSeparation`](System__Library__DigitalSeparation__SharingSources__PasswordsDigitalSeparation.bundle__PasswordsDigitalSeparation.md) | 7625.2.8.21.6 | full |
| [`/System/Library/Extensions/AGXGPURawCounterBundle.bundle/AGXGPURawCounterBundle`](System__Library__Extensions__AGXGPURawCounterBundle.bundle__AGXGPURawCounterBundle.md) | 362.5.0.0.0 | full |
| [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) | 362.5.0.0.0 | full |
| [`/System/Library/Extensions/AppleHDQGasGaugeControl.kext/PlugIns/AppleHDQGasGaugeHID.plugin/AppleHDQGasGaugeHID`](System__Library__Extensions__AppleHDQGasGaugeControl.kext__PlugIns__AppleHDQGasGaugeHID.plugin__AppleHDQGasGaugeHID.md) | 240.0.0.0.0 | full |
| [`/System/Library/Extensions/AppleMetalGLRenderer.bundle/AppleMetalGLRenderer`](System__Library__Extensions__AppleMetalGLRenderer.bundle__AppleMetalGLRenderer.md) | 105.0.0.0.0 | full |
| [`/System/Library/Extensions/AppleMultitouchSPI.kext/PlugIns/MultitouchHID.plugin/MultitouchHID`](System__Library__Extensions__AppleMultitouchSPI.kext__PlugIns__MultitouchHID.plugin__MultitouchHID.md) | 10110.4.0.0.0 | full |
| [`/System/Library/Extensions/AppleSPU.kext/PlugIns/AppleSPULib.plugin/AppleSPULib`](System__Library__Extensions__AppleSPU.kext__PlugIns__AppleSPULib.plugin__AppleSPULib.md) | 1087.40.4.0.0 | full |
| [`/System/Library/Extensions/AppleSPU.kext/PlugIns/GNSSPassthroughLib.plugin/GNSSPassthroughLib`](System__Library__Extensions__AppleSPU.kext__PlugIns__GNSSPassthroughLib.plugin__GNSSPassthroughLib.md) | 1087.40.4.0.0 | full |
| [`/System/Library/Extensions/IOHIDFamily.kext/PlugIns/IOHIDLib.plugin/IOHIDLib`](System__Library__Extensions__IOHIDFamily.kext__PlugIns__IOHIDLib.plugin__IOHIDLib.md) | 2360.40.13.0.1 | full |
| [`/System/Library/Extensions/IOUSBDeviceFamily.kext/PlugIns/IOUSBDeviceLib.plugin/IOUSBDeviceLib`](System__Library__Extensions__IOUSBDeviceFamily.kext__PlugIns__IOUSBDeviceLib.plugin__IOUSBDeviceLib.md) | 896.40.5.0.0 | full |
| [`/System/Library/Fitness/Plugins/ActivitySharingAwardsPlugin.bundle/ActivitySharingAwardsPlugin`](System__Library__Fitness__Plugins__ActivitySharingAwardsPlugin.bundle__ActivitySharingAwardsPlugin.md) | 2027.1.7.0.0 | light |
| [`/System/Library/Fitness/Plugins/SeymourAwardsPlugin.bundle/SeymourAwardsPlugin`](System__Library__Fitness__Plugins__SeymourAwardsPlugin.bundle__SeymourAwardsPlugin.md) | 2027.1.69.0.0 | light |
| [`/System/Library/Frameworks/ARKit.framework/ARKit`](System__Library__Frameworks__ARKit.framework__ARKit.md) | 781.40.6.0.0 | light |
| [`/System/Library/Frameworks/AVFoundation.framework/AVFoundation`](System__Library__Frameworks__AVFoundation.framework__AVFoundation.md) | 2482.2.0.0.0 | full |
| [`/System/Library/Frameworks/AVSystemRouting.framework/AVSystemRouting`](System__Library__Frameworks__AVSystemRouting.framework__AVSystemRouting.md) | 385.10.1.0.0 | light |
| [`/System/Library/Frameworks/Accelerate.framework/Accelerate`](System__Library__Frameworks__Accelerate.framework__Accelerate.md) | 1155.0.0.0.0 | light |
| [`/System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/Libraries/libCGInterfaces.dylib`](System__Library__Frameworks__Accelerate.framework__Frameworks__vImage.framework__Libraries__libCGInterfaces.dylib.md) | 650.40.4.0.0 | light |
| [`/System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/vImage`](System__Library__Frameworks__Accelerate.framework__Frameworks__vImage.framework__vImage.md) | 650.40.4.0.0 | light |
| [`/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBLAS.dylib`](System__Library__Frameworks__Accelerate.framework__Frameworks__vecLib.framework__libBLAS.dylib.md) | 1617.40.9.0.0 | light |
| [`/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib`](System__Library__Frameworks__Accelerate.framework__Frameworks__vecLib.framework__libBNNS.dylib.md) | 2212.42.1.0.0 | light |
| [`/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libLinearAlgebra.dylib`](System__Library__Frameworks__Accelerate.framework__Frameworks__vecLib.framework__libLinearAlgebra.dylib.md) | 1617.40.9.0.0 | light |
| [`/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libQuadrature.dylib`](System__Library__Frameworks__Accelerate.framework__Frameworks__vecLib.framework__libQuadrature.dylib.md) | 10.0.0.0.0 | light |
| [`/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparse.dylib`](System__Library__Frameworks__Accelerate.framework__Frameworks__vecLib.framework__libSparse.dylib.md) | 196.0.1.0.0 | light |
| [`/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparseBLAS.dylib`](System__Library__Frameworks__Accelerate.framework__Frameworks__vecLib.framework__libSparseBLAS.dylib.md) | 196.0.1.0.0 | light |
| [`/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libvDSP.dylib`](System__Library__Frameworks__Accelerate.framework__Frameworks__vecLib.framework__libvDSP.dylib.md) | 1155.0.0.0.0 | light |
| [`/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libvMisc.dylib`](System__Library__Frameworks__Accelerate.framework__Frameworks__vecLib.framework__libvMisc.dylib.md) | 1155.0.0.0.0 | light |
| [`/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/vecLib`](System__Library__Frameworks__Accelerate.framework__Frameworks__vecLib.framework__vecLib.md) | 1155.0.0.0.0 | light |
| [`/System/Library/Frameworks/AccessoryLiveActivities.framework/AccessoryLiveActivities`](System__Library__Frameworks__AccessoryLiveActivities.framework__AccessoryLiveActivities.md) | 7749.2.13.0.3 | full |
| [`/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit`](System__Library__Frameworks__AccessorySetupKit.framework__AccessorySetupKit.md) | 2701.6.0.0.0 | full |
| [`/System/Library/Frameworks/AccessoryTransportExtension.framework/AccessoryTransportExtension`](System__Library__Frameworks__AccessoryTransportExtension.framework__AccessoryTransportExtension.md) | 2701.6.0.0.0 | full |
| [`/System/Library/Frameworks/AdServices.framework/AdServices`](System__Library__Frameworks__AdServices.framework__AdServices.md) | 557.2.14.0.0 | light |
| [`/System/Library/Frameworks/AdSupport.framework/AdSupport`](System__Library__Frameworks__AdSupport.framework__AdSupport.md) | 106.3.3.0.0 | light |
| [`/System/Library/Frameworks/AddressBook.framework/AddressBook`](System__Library__Frameworks__AddressBook.framework__AddressBook.md) | 12679.200.1.0.0 | light |
| [`/System/Library/Frameworks/AddressBookUI.framework/AddressBookUI`](System__Library__Frameworks__AddressBookUI.framework__AddressBookUI.md) | 2407.200.1.0.0 | light |
| [`/System/Library/Frameworks/AlarmKit.framework/AlarmKit`](System__Library__Frameworks__AlarmKit.framework__AlarmKit.md) | 2333.2.5.0.0 | light |
| [`/System/Library/Frameworks/AppClip.framework/AppClip`](System__Library__Frameworks__AppClip.framework__AppClip.md) | 1039.1.0.0.0 | light |
| [`/System/Library/Frameworks/AppIntentsTypeSupport.framework/AppIntentsTypeSupport`](System__Library__Frameworks__AppIntentsTypeSupport.framework__AppIntentsTypeSupport.md) | 301.1.16.0.0 | light |
| [`/System/Library/Frameworks/AppMigrationKit.framework/AppMigrationKit`](System__Library__Frameworks__AppMigrationKit.framework__AppMigrationKit.md) | 140.0.0.0.0 | light |
| [`/System/Library/Frameworks/AppTrackingTransparency.framework/AppTrackingTransparency`](System__Library__Frameworks__AppTrackingTransparency.framework__AppTrackingTransparency.md) | 106.3.3.0.0 | light |
| [`/System/Library/Frameworks/AssetsLibrary.framework/AssetsLibrary`](System__Library__Frameworks__AssetsLibrary.framework__AssetsLibrary.md) | 916.62.154.0.0 | light |
| [`/System/Library/Frameworks/AudioAccessoryKit.framework/AudioAccessoryKit`](System__Library__Frameworks__AudioAccessoryKit.framework__AudioAccessoryKit.md) | 41.7.0.0.0 | full |
| [`/System/Library/Frameworks/AudioToolbox.framework/libValidationCapsule.dylib`](System__Library__Frameworks__AudioToolbox.framework__libValidationCapsule.dylib.md) | 1638.215.0.0.0 | full |
| [`/System/Library/Frameworks/AudioToolbox.framework/libVibeSynthEngine.dylib`](System__Library__Frameworks__AudioToolbox.framework__libVibeSynthEngine.dylib.md) | 1638.215.0.0.0 | full |
| [`/System/Library/Frameworks/AutomatedDeviceEnrollment.framework/AutomatedDeviceEnrollment`](System__Library__Frameworks__AutomatedDeviceEnrollment.framework__AutomatedDeviceEnrollment.md) | 42.0.0.0.0 | light |
| [`/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/AutomaticAssessmentConfiguration`](System__Library__Frameworks__AutomaticAssessmentConfiguration.framework__AutomaticAssessmentConfiguration.md) | 56.40.4.0.0 | light |
| [`/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACClient.framework/AACClient`](System__Library__Frameworks__AutomaticAssessmentConfiguration.framework__Frameworks__AACClient.framework__AACClient.md) | 56.40.4.0.0 | light |
| [`/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACDependencies.framework/AACDependencies`](System__Library__Frameworks__AutomaticAssessmentConfiguration.framework__Frameworks__AACDependencies.framework__AACDependencies.md) | 56.40.4.0.0 | light |
| [`/System/Library/Frameworks/BrowserEngineCore.framework/BrowserEngineCore`](System__Library__Frameworks__BrowserEngineCore.framework__BrowserEngineCore.md) | 7625.2.1.1.0 | light |
| [`/System/Library/Frameworks/BrowserKit.framework/BrowserKit`](System__Library__Frameworks__BrowserKit.framework__BrowserKit.md) | 625.2.8.21.5 | light |
| [`/System/Library/Frameworks/BusinessChat.framework/BusinessChat`](System__Library__Frameworks__BusinessChat.framework__BusinessChat.md) | 30123.31.8.11.4 | light |
| [`/System/Library/Frameworks/CarKey.framework/CarKey`](System__Library__Frameworks__CarKey.framework__CarKey.md) | 71.9.3.0.0 | light |
| [`/System/Library/Frameworks/Cinematic.framework/Cinematic`](System__Library__Frameworks__Cinematic.framework__Cinematic.md) | 560.40.5.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend20.dylib`](usr__lib__objc__libobjcMsgSend20.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libLAPACK.dylib`](System__Library__Frameworks__Accelerate.framework__Frameworks__vecLib.framework__libLAPACK.dylib.md) | 1617.40.9.0.0 | light |
| [`/System/Library/Frameworks/Assignables.framework/Assignables`](System__Library__Frameworks__Assignables.framework__Assignables.md) | 3.0.2.0.0 | light |
| [`/System/Library/Frameworks/BackgroundAssets.framework/BackgroundAssets`](System__Library__Frameworks__BackgroundAssets.framework__BackgroundAssets.md) | 279.52.2.0.0 | light |
| [`/System/Library/Frameworks/CarPlay.framework/CarPlay`](System__Library__Frameworks__CarPlay.framework__CarPlay.md) | 552.7.1.0.0 | light |
| [`/System/Library/Frameworks/ClassKit.framework/ClassKit`](System__Library__Frameworks__ClassKit.framework__ClassKit.md) | 152.1.1.0.0 | light |
| [`/System/Library/Frameworks/ClassKitUI.framework/ClassKitUI`](System__Library__Frameworks__ClassKitUI.framework__ClassKitUI.md) | 152.1.1.0.0 | light |
| [`/System/Library/Frameworks/ComputeGraph.framework/ComputeGraph`](System__Library__Frameworks__ComputeGraph.framework__ComputeGraph.md) | 30.40.1.0.0 | light |
| [`/System/Library/Frameworks/ContactProvider.framework/ContactProvider`](System__Library__Frameworks__ContactProvider.framework__ContactProvider.md) | 58.200.1.0.0 | light |
| [`/System/Library/Frameworks/CoreAI.framework/CoreAI`](System__Library__Frameworks__CoreAI.framework__CoreAI.md) | 3605.6.4.0.0 | light |
| [`/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit`](System__Library__Frameworks__CoreAudioKit.framework__CoreAudioKit.md) | 296.200.0.0.0 | full |
| [`/System/Library/Frameworks/CoreLocationUI.framework/CoreLocationUI`](System__Library__Frameworks__CoreLocationUI.framework__CoreLocationUI.md) | 3187.0.1.0.0 | full |
| [`/System/Library/Frameworks/CoreMIDI.framework/CoreMIDI`](System__Library__Frameworks__CoreMIDI.framework__CoreMIDI.md) | 333.203.0.0.0 | light |
| [`/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO`](System__Library__Frameworks__CoreMediaIO.framework__CoreMediaIO.md) | 5634.41.3.0.1 | light |
| [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) | 371.8.0.0.0 | full |
| [`/System/Library/Frameworks/CoreTelephony.framework/Support/CTParser.framework/CTParser`](System__Library__Frameworks__CoreTelephony.framework__Support__CTParser.framework__CTParser.md) | 13499.0.0.0.0 | light |
| [`/System/Library/Frameworks/CoreTelephony.framework/Support/libCellularDecoders.dylib`](System__Library__Frameworks__CoreTelephony.framework__Support__libCellularDecoders.dylib.md) | 13499.0.0.0.0 | light |
| [`/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterAWDMetrics.dylib`](System__Library__Frameworks__CoreTelephony.framework__Support__libCommCenterAWDMetrics.dylib.md) | 13499.0.0.0.0 | full |
| [`/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib`](System__Library__Frameworks__CoreTelephony.framework__Support__libCommCenterBase.dylib.md) | 13499.0.0.0.0 | full |
| [`/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterCNTargetData.dylib`](System__Library__Frameworks__CoreTelephony.framework__Support__libCommCenterCNTargetData.dylib.md) | 13499.0.0.0.0 | full |
| [`/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterCommandDrivers.dylib`](System__Library__Frameworks__CoreTelephony.framework__Support__libCommCenterCommandDrivers.dylib.md) | 13499.0.0.0.0 | full |
| [`/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterKCommandDrivers.dylib`](System__Library__Frameworks__CoreTelephony.framework__Support__libCommCenterKCommandDrivers.dylib.md) | 13499.0.0.0.0 | full |
| [`/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterMCommandDrivers.dylib`](System__Library__Frameworks__CoreTelephony.framework__Support__libCommCenterMCommandDrivers.dylib.md) | 13499.0.0.0.0 | full |
| [`/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib`](System__Library__Frameworks__CoreTelephony.framework__Support__libSystemDetermination.dylib.md) | 13499.0.0.0.0 | light |
| [`/System/Library/Frameworks/CrashReportExtension.framework/CrashReportExtension`](System__Library__Frameworks__CrashReportExtension.framework__CrashReportExtension.md) | 1056.40.8.0.0 | light |
| [`/System/Library/Frameworks/CreateML.framework/CreateML`](System__Library__Frameworks__CreateML.framework__CreateML.md) | 1410.0.0.0.0 | light |
| [`/System/Library/Frameworks/CreateMLComponents.framework/CreateMLComponents`](System__Library__Frameworks__CreateMLComponents.framework__CreateMLComponents.md) | 1431.0.0.0.0 | light |
| [`/System/Library/Frameworks/DeclaredAgeRange.framework/DeclaredAgeRange`](System__Library__Frameworks__DeclaredAgeRange.framework__DeclaredAgeRange.md) | 28.125.4.0.0 | light |
| [`/System/Library/Frameworks/DeveloperToolsSupport.framework/DeveloperToolsSupport`](System__Library__Frameworks__DeveloperToolsSupport.framework__DeveloperToolsSupport.md) | 24.20.2.0.0 | light |
| [`/System/Library/Frameworks/DeviceActivity.framework/DeviceActivity`](System__Library__Frameworks__DeviceActivity.framework__DeviceActivity.md) | 407.1.5.0.0 | light |
| [`/System/Library/Frameworks/DeviceCheck.framework/DeviceCheck`](System__Library__Frameworks__DeviceCheck.framework__DeviceCheck.md) | 158.0.0.0.0 | light |
| [`/System/Library/Frameworks/DeviceDiscoveryExtension.framework/DeviceDiscoveryExtension`](System__Library__Frameworks__DeviceDiscoveryExtension.framework__DeviceDiscoveryExtension.md) | 2701.6.0.0.0 | light |
| [`/System/Library/Frameworks/DeviceDiscoveryUI.framework/DeviceDiscoveryUI`](System__Library__Frameworks__DeviceDiscoveryUI.framework__DeviceDiscoveryUI.md) | 2131.21.31.21.8 | light |
| [`/System/Library/Frameworks/DockKit.framework/DockKit`](System__Library__Frameworks__DockKit.framework__DockKit.md) | 432.0.0.0.0 | light |
| [`/System/Library/Frameworks/DriverKit.framework/DriverKit`](System__Library__Frameworks__DriverKit.framework__DriverKit.md) | 509.40.11.0.0 | full |
| [`/System/Library/Frameworks/ExposureNotification.framework/ExposureNotification`](System__Library__Frameworks__ExposureNotification.framework__ExposureNotification.md) | 2701.7.1.0.0 | light |
| [`/System/Library/Frameworks/FamilyControls.framework/FamilyControls`](System__Library__Frameworks__FamilyControls.framework__FamilyControls.md) | 1248.0.0.0.0 | light |
| [`/System/Library/Frameworks/FileProvider.framework/OverrideBundles/FileProviderOverride.bundle/FileProviderOverride`](System__Library__Frameworks__FileProvider.framework__OverrideBundles__FileProviderOverride.bundle__FileProviderOverride.md) | 4838.42.2.0.0 | light |
| [`/System/Library/Frameworks/FileProvider.framework/OverrideBundles/iCloudDriveFileProviderOverride.bundle/iCloudDriveFileProviderOverride`](System__Library__Frameworks__FileProvider.framework__OverrideBundles__iCloudDriveFileProviderOverride.bundle__iCloudDriveFileProviderOverride.md) | 5168.40.162.0.0 | light |
| [`/System/Library/Frameworks/FileProviderUI.framework/FileProviderUI`](System__Library__Frameworks__FileProviderUI.framework__FileProviderUI.md) | 57.0.0.0.0 | light |
| [`/System/Library/Frameworks/FinanceKitUI.framework/FinanceKitUI`](System__Library__Frameworks__FinanceKitUI.framework__FinanceKitUI.md) | 376.1.6.0.0 | light |
| [`/System/Library/Frameworks/GLKit.framework/GLKit`](System__Library__Frameworks__GLKit.framework__GLKit.md) | 129.0.0.0.0 | light |
| [`/System/Library/Frameworks/GSS.framework/GSS`](System__Library__Frameworks__GSS.framework__GSS.md) | 725.40.6.0.0 | light |
| [`/System/Library/Frameworks/GameKit.framework/GameKit`](System__Library__Frameworks__GameKit.framework__GameKit.md) | 821.1.16.2.1 | light |
| [`/System/Library/Frameworks/GameSave.framework/GameSave`](System__Library__Frameworks__GameSave.framework__GameSave.md) | 1.0.0.0.0 | light |
| [`/System/Library/Frameworks/GameplayKit.framework/GameplayKit`](System__Library__Frameworks__GameplayKit.framework__GameplayKit.md) | 102.1.2.0.0 | light |
| [`/System/Library/Frameworks/GeoToolbox.framework/GeoToolbox`](System__Library__Frameworks__GeoToolbox.framework__GeoToolbox.md) | 34.31.6.17.106 | light |
| [`/System/Library/Frameworks/IdentityDocumentServices.framework/IdentityDocumentServices`](System__Library__Frameworks__IdentityDocumentServices.framework__IdentityDocumentServices.md) | 9.108.0.0.0 | light |
| [`/System/Library/Frameworks/IdentityDocumentServicesUI.framework/IdentityDocumentServicesUI`](System__Library__Frameworks__IdentityDocumentServicesUI.framework__IdentityDocumentServicesUI.md) | 9.108.0.0.0 | light |
| [`/System/Library/Frameworks/IdentityLookup.framework/IdentityLookup`](System__Library__Frameworks__IdentityLookup.framework__IdentityLookup.md) | 1406.200.101.21.1 | light |
| [`/System/Library/Frameworks/IdentityLookupUI.framework/IdentityLookupUI`](System__Library__Frameworks__IdentityLookupUI.framework__IdentityLookupUI.md) | 158.200.81.21.9 | light |
| [`/System/Library/Frameworks/ImageCaptureCore.framework/ImageCaptureCore`](System__Library__Frameworks__ImageCaptureCore.framework__ImageCaptureCore.md) | 2118.1.0.0.0 | light |
| [`/System/Library/Frameworks/ImmersiveMediaSupport.framework/ImmersiveMediaSupport`](System__Library__Frameworks__ImmersiveMediaSupport.framework__ImmersiveMediaSupport.md) | 124.40.1.0.0 | light |
| [`/System/Library/Frameworks/JournalingSuggestions.framework/JournalingSuggestions`](System__Library__Frameworks__JournalingSuggestions.framework__JournalingSuggestions.md) | 502.0.8.0.0 | light |
| [`/System/Library/Frameworks/LiveCommunicationKit.framework/LiveCommunicationKit`](System__Library__Frameworks__LiveCommunicationKit.framework__LiveCommunicationKit.md) | 158.200.81.21.9 | light |
| [`/System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/DaemonUtils`](System__Library__Frameworks__LocalAuthentication.framework__Support__DaemonUtils.framework__DaemonUtils.md) | 2319.52.2.0.0 | light |
| [`/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/MechanismBase`](System__Library__Frameworks__LocalAuthentication.framework__Support__MechanismBase.framework__MechanismBase.md) | 2319.52.2.0.0 | light |
| [`/System/Library/Frameworks/LocalAuthentication.framework/Support/ModuleBase.framework/ModuleBase`](System__Library__Frameworks__LocalAuthentication.framework__Support__ModuleBase.framework__ModuleBase.md) | 2319.52.2.0.0 | light |
| [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) | 2319.52.2.0.0 | full |
| [`/System/Library/Frameworks/LockedCameraCapture.framework/LockedCameraCapture`](System__Library__Frameworks__LockedCameraCapture.framework__LockedCameraCapture.md) | 159.2.5.0.6 | full |
| [`/System/Library/Frameworks/MLCompute.framework/MLCompute`](System__Library__Frameworks__MLCompute.framework__MLCompute.md) | 87.0.0.0.0 | light |
| [`/System/Library/Frameworks/ManagedApp.framework/ManagedApp`](System__Library__Frameworks__ManagedApp.framework__ManagedApp.md) | 113.52.1.0.0 | light |
| [`/System/Library/Frameworks/ManagedSettingsUI.framework/ManagedSettingsUI`](System__Library__Frameworks__ManagedSettingsUI.framework__ManagedSettingsUI.md) | 319.40.1.0.0 | light |
| [`/System/Library/Frameworks/Matter.framework/Matter`](System__Library__Frameworks__Matter.framework__Matter.md) | 336.2.1.0.0 | light |
| [`/System/Library/Frameworks/MatterSupport.framework/MatterSupport`](System__Library__Frameworks__MatterSupport.framework__MatterSupport.md) | 1520.2.7.1.3 | light |
| [`/System/Library/Frameworks/MediaDevice.framework/MediaDevice`](System__Library__Frameworks__MediaDevice.framework__MediaDevice.md) | 385.10.1.0.0 | light |
| [`/System/Library/Frameworks/MediaIntelligence.framework/MediaIntelligence`](System__Library__Frameworks__MediaIntelligence.framework__MediaIntelligence.md) | 460.14.1.2.0 | light |
| [`/System/Library/Frameworks/MediaIntents.framework/MediaIntents`](System__Library__Frameworks__MediaIntents.framework__MediaIntents.md) | 3605.14.1.11.1 | light |
| [`/System/Library/Frameworks/MediaSetup.framework/MediaSetup`](System__Library__Frameworks__MediaSetup.framework__MediaSetup.md) | 261.10.1.0.0 | light |
| [`/System/Library/Frameworks/MediaToolbox.framework/Support/libSTS-N.dylib`](System__Library__Frameworks__MediaToolbox.framework__Support__libSTS-N.dylib.md) | 1638.215.0.0.0 | light |
| [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](System__Library__Frameworks__MetalFX.framework__MetalFX.md) | 40.9.0.0.0 | full |
| [`/System/Library/Frameworks/MetalKit.framework/MetalKit`](System__Library__Frameworks__MetalKit.framework__MetalKit.md) | 174.4.0.0.0 | full |
| [`/System/Library/Frameworks/MetalPerformancePrimitives.framework/MetalPerformancePrimitives`](System__Library__Frameworks__MetalPerformancePrimitives.framework__MetalPerformancePrimitives.md) | 130.1.4.0.0 | full |
| [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSBenchmarkLoop.framework/MPSBenchmarkLoop`](System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSBenchmarkLoop.framework__MPSBenchmarkLoop.md) | 130.1.4.0.0 | light |
| [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSCore.framework/MPSCore`](System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSCore.framework__MPSCore.md) | 130.1.4.0.0 | light |
| [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSFunctions.framework/MPSFunctions`](System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSFunctions.framework__MPSFunctions.md) | 130.1.4.0.0 | light |
| [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSHost.framework/MPSHost`](System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSHost.framework__MPSHost.md) | 130.1.4.0.0 | light |
| [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSImage.framework/MPSImage`](System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSImage.framework__MPSImage.md) | 130.1.4.0.0 | light |
| [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSMatrix.framework/MPSMatrix`](System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSMatrix.framework__MPSMatrix.md) | 130.1.4.0.0 | light |
| [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) | 130.1.4.0.0 | full |
| [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSRayIntersector.framework/MPSRayIntersector`](System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSRayIntersector.framework__MPSRayIntersector.md) | 130.1.4.0.0 | light |
| [`/System/Library/Frameworks/MetalPerformanceShaders.framework/MetalPerformanceShaders`](System__Library__Frameworks__MetalPerformanceShaders.framework__MetalPerformanceShaders.md) | 130.1.4.0.0 | full |
| [`/System/Library/Frameworks/MetricKit.framework/MetricKit`](System__Library__Frameworks__MetricKit.framework__MetricKit.md) | 369.40.2.0.0 | light |
| [`/System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices`](System__Library__Frameworks__MobileCoreServices.framework__MobileCoreServices.md) | 1517.1.12.0.0 | light |
| [`/System/Library/Frameworks/ModelIO.framework/ModelIO`](System__Library__Frameworks__ModelIO.framework__ModelIO.md) | 270.1.3.0.0 | light |
| [`/System/Library/Frameworks/MultipeerConnectivity.framework/MultipeerConnectivity`](System__Library__Frameworks__MultipeerConnectivity.framework__MultipeerConnectivity.md) | 180.100.1.0.0 | light |
| [`/System/Library/Frameworks/MusicUnderstanding.framework/MusicUnderstanding`](System__Library__Frameworks__MusicUnderstanding.framework__MusicUnderstanding.md) | 13.0.0.0.0 | light |
| [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) | 576.0.1.0.0 | full |
| [`/System/Library/Frameworks/NowPlaying.framework/NowPlaying`](System__Library__Frameworks__NowPlaying.framework__NowPlaying.md) | 4026.210.4.0.0 | light |
| [`/System/Library/Frameworks/OSLog.framework/OSLog`](System__Library__Frameworks__OSLog.framework__OSLog.md) | 1966.40.15.0.2 | light |
| [`/System/Library/Frameworks/OpenAL.framework/OpenAL`](System__Library__Frameworks__OpenAL.framework__OpenAL.md) | 84.1.0.0.0 | light |
| [`/System/Library/Frameworks/OpenGLES.framework/GLEngine.bundle/GLEngine`](System__Library__Frameworks__OpenGLES.framework__GLEngine.bundle__GLEngine.md) | 24.0.2.0.0 | light |
| [`/System/Library/Frameworks/OpenGLES.framework/OpenGLES`](System__Library__Frameworks__OpenGLES.framework__OpenGLES.md) | 24.0.2.0.0 | light |
| [`/System/Library/Frameworks/OpenGLES.framework/libCVMSPluginSupport.dylib`](System__Library__Frameworks__OpenGLES.framework__libCVMSPluginSupport.dylib.md) | 24.0.2.0.0 | light |
| [`/System/Library/Frameworks/OpenGLES.framework/libCoreFSCache.dylib`](System__Library__Frameworks__OpenGLES.framework__libCoreFSCache.dylib.md) | 405.0.0.0.0 | light |
| [`/System/Library/Frameworks/OpenGLES.framework/libCoreVMClient.dylib`](System__Library__Frameworks__OpenGLES.framework__libCoreVMClient.dylib.md) | 405.0.0.0.0 | light |
| [`/System/Library/Frameworks/OpenGLES.framework/libGFXShared.dylib`](System__Library__Frameworks__OpenGLES.framework__libGFXShared.dylib.md) | 24.0.2.0.0 | light |
| [`/System/Library/Frameworks/OpenGLES.framework/libGLImage.dylib`](System__Library__Frameworks__OpenGLES.framework__libGLImage.dylib.md) | 24.0.2.0.0 | light |
| [`/System/Library/Frameworks/OpenGLES.framework/libGLProgrammability.dylib`](System__Library__Frameworks__OpenGLES.framework__libGLProgrammability.dylib.md) | 24.0.2.0.0 | light |
| [`/System/Library/Frameworks/OpenGLES.framework/libGLVMPlugin.dylib`](System__Library__Frameworks__OpenGLES.framework__libGLVMPlugin.dylib.md) | 24.0.2.0.0 | light |
| [`/System/Library/Frameworks/OpenGLES.framework/libGLVMPlugin32023.dylib`](System__Library__Frameworks__OpenGLES.framework__libGLVMPlugin32023.dylib.md) | 24.0.2.0.0 | light |
| [`/System/Library/Frameworks/PassKit.framework/PassKit`](System__Library__Frameworks__PassKit.framework__PassKit.md) | 1696.2.9.2.0 | light |
| [`/System/Library/Frameworks/PermissionKit.framework/PermissionKit`](System__Library__Frameworks__PermissionKit.framework__PermissionKit.md) | 97.125.8.0.0 | light |
| [`/System/Library/Frameworks/ProximityReader.framework/ProximityReader`](System__Library__Frameworks__ProximityReader.framework__ProximityReader.md) | 151.6.0.0.0 | light |
| [`/System/Library/Frameworks/PushKit.framework/PushKit`](System__Library__Frameworks__PushKit.framework__PushKit.md) | 111.100.1.0.0 | light |
| [`/System/Library/Frameworks/PushToTalk.framework/PushToTalk`](System__Library__Frameworks__PushToTalk.framework__PushToTalk.md) | 158.200.81.21.9 | light |
| [`/System/Library/Frameworks/QuickLook.framework/QuickLook`](System__Library__Frameworks__QuickLook.framework__QuickLook.md) | 1034.1.7.0.0 | light |
| [`/System/Library/Frameworks/RelevanceKit.framework/RelevanceKit`](System__Library__Frameworks__RelevanceKit.framework__RelevanceKit.md) | 248.1.0.0.0 | light |
| [`/System/Library/Frameworks/ReplayKit.framework/ReplayKit`](System__Library__Frameworks__ReplayKit.framework__ReplayKit.md) | 765.15.2.0.0 | light |
| [`/System/Library/Frameworks/RoomPlan.framework/RoomPlan`](System__Library__Frameworks__RoomPlan.framework__RoomPlan.md) | 2.17.0.0.0 | light |
| [`/System/Library/Frameworks/SafetyKit.framework/SafetyKit`](System__Library__Frameworks__SafetyKit.framework__SafetyKit.md) | 175.0.5.0.0 | light |
| [`/System/Library/Frameworks/SceneKit.framework/SceneKit`](System__Library__Frameworks__SceneKit.framework__SceneKit.md) | 612.101.0.0.0 | light |
| [`/System/Library/Frameworks/ScreenCaptureKit.framework/ScreenCaptureKit`](System__Library__Frameworks__ScreenCaptureKit.framework__ScreenCaptureKit.md) | 765.15.2.0.0 | light |
| [`/System/Library/Frameworks/ScreenTime.framework/ScreenTime`](System__Library__Frameworks__ScreenTime.framework__ScreenTime.md) | 655.1.14.1.0 | light |
| [`/System/Library/Frameworks/SecureElementCredential.framework/SecureElementCredential`](System__Library__Frameworks__SecureElementCredential.framework__SecureElementCredential.md) | 71.9.3.0.0 | full |
| [`/System/Library/Frameworks/SecurityUI.framework/SecurityUI`](System__Library__Frameworks__SecurityUI.framework__SecurityUI.md) | 55222.40.4.0.0 | light |
| [`/System/Library/Frameworks/ServicesAccountLinking.framework/ServicesAccountLinking`](System__Library__Frameworks__ServicesAccountLinking.framework__ServicesAccountLinking.md) | 1.5.1.0.0 | light |
| [`/System/Library/Frameworks/ShazamKit.framework/ShazamKit`](System__Library__Frameworks__ShazamKit.framework__ShazamKit.md) | 427.2.6.0.0 | light |
| [`/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis`](System__Library__Frameworks__SoundAnalysis.framework__SoundAnalysis.md) | 510.16.0.0.0 | light |
| [`/System/Library/Frameworks/SpriteKit.framework/SpriteKit`](System__Library__Frameworks__SpriteKit.framework__SpriteKit.md) | 53.1.1.0.0 | light |
| [`/System/Library/Frameworks/StateReporting.framework/StateReporting`](System__Library__Frameworks__StateReporting.framework__StateReporting.md) | 205.0.0.0.0 | light |
| [`/System/Library/Frameworks/StickerFoundation.framework/StickerFoundation`](System__Library__Frameworks__StickerFoundation.framework__StickerFoundation.md) | 152.1.3.0.0 | light |
| [`/System/Library/Frameworks/SystemExtensions.framework/SystemExtensions`](System__Library__Frameworks__SystemExtensions.framework__SystemExtensions.md) | 224.40.5.0.0 | light |
| [`/System/Library/Frameworks/TabularData.framework/TabularData`](System__Library__Frameworks__TabularData.framework__TabularData.md) | 55.40.2.0.0 | light |
| [`/System/Library/Frameworks/TelephonyMessagingKit.framework/TelephonyMessagingKit`](System__Library__Frameworks__TelephonyMessagingKit.framework__TelephonyMessagingKit.md) | 13499.0.0.0.0 | full |
| [`/System/Library/Frameworks/ThreadNetwork.framework/ThreadNetwork`](System__Library__Frameworks__ThreadNetwork.framework__ThreadNetwork.md) | 446.0.4.0.0 | full |
| [`/System/Library/Frameworks/TouchController.framework/TouchController`](System__Library__Frameworks__TouchController.framework__TouchController.md) | 2.0.7.0.0 | light |
| [`/System/Library/Frameworks/Translation.framework/Translation`](System__Library__Frameworks__Translation.framework__Translation.md) | 396.2.0.0.0 | light |
| [`/System/Library/Frameworks/TranslationUIProvider.framework/TranslationUIProvider`](System__Library__Frameworks__TranslationUIProvider.framework__TranslationUIProvider.md) | 396.2.0.0.0 | light |
| [`/System/Library/Frameworks/Twitter.framework/Twitter`](System__Library__Frameworks__Twitter.framework__Twitter.md) | 231.0.0.0.0 | light |
| [`/System/Library/Frameworks/UIKit.framework/UIKit`](System__Library__Frameworks__UIKit.framework__UIKit.md) | 9127.1.13.13.0 | light |
| [`/System/Library/Frameworks/USDKit.framework/USDKit`](System__Library__Frameworks__USDKit.framework__USDKit.md) | 106.40.4.0.1 | light |
| [`/System/Library/Frameworks/UserNotificationsUI.framework/UserNotificationsUI`](System__Library__Frameworks__UserNotificationsUI.framework__UserNotificationsUI.md) | 1077.2.7.0.0 | light |
| [`/System/Library/Frameworks/VideoSubscriberAccount.framework/VideoSubscriberAccount`](System__Library__Frameworks__VideoSubscriberAccount.framework__VideoSubscriberAccount.md) | 609.10.3.0.0 | light |
| [`/System/Library/Frameworks/Vision.framework/libfaceCore.dylib`](System__Library__Frameworks__Vision.framework__libfaceCore.dylib.md) | 10.1.7.0.0 | light |
| [`/System/Library/Frameworks/VisionKit.framework/VisionKit`](System__Library__Frameworks__VisionKit.framework__VisionKit.md) | 347.1.3.0.0 | light |
| [`/System/Library/Frameworks/VisualIntelligence.framework/VisualIntelligence`](System__Library__Frameworks__VisualIntelligence.framework__VisualIntelligence.md) | 246.1.29.1.0 | light |
| [`/System/Library/Frameworks/WatchConnectivity.framework/WatchConnectivity`](System__Library__Frameworks__WatchConnectivity.framework__WatchConnectivity.md) | 224.100.1.0.0 | light |
| [`/System/Library/Frameworks/WatchKit.framework/WatchKit`](System__Library__Frameworks__WatchKit.framework__WatchKit.md) | 2001.4.2.0.0 | light |
| [`/System/Library/Frameworks/WeatherKit.framework/WeatherKit`](System__Library__Frameworks__WeatherKit.framework__WeatherKit.md) | 1474.0.0.0.0 | light |
| [`/System/Library/Frameworks/WebKit.framework/Frameworks/libWebKitSwift.dylib`](System__Library__Frameworks__WebKit.framework__Frameworks__libWebKitSwift.dylib.md) | 625.2.8.21.2 | light |
| [`/System/Library/Frameworks/WiFiAware.framework/WiFiAware`](System__Library__Frameworks__WiFiAware.framework__WiFiAware.md) | 887.9.0.0.0 | full |
| [`/System/Library/Frameworks/WiFiInfrastructure.framework/WiFiInfrastructure`](System__Library__Frameworks__WiFiInfrastructure.framework__WiFiInfrastructure.md) | 1032.9.0.0.0 | full |
| [`/System/Library/Frameworks/WirelessInsights.framework/WirelessInsights`](System__Library__Frameworks__WirelessInsights.framework__WirelessInsights.md) | 370.0.0.0.0 | light |
| [`/System/Library/Frameworks/_AVKit_SwiftUI.framework/_AVKit_SwiftUI`](System__Library__Frameworks___AVKit_SwiftUI.framework___AVKit_SwiftUI.md) | 1392.5.0.0.0 | light |
| [`/System/Library/Frameworks/_AdAttributionKit_StoreKit.framework/_AdAttributionKit_StoreKit`](System__Library__Frameworks___AdAttributionKit_StoreKit.framework___AdAttributionKit_StoreKit.md) | 4.1.1.0.0 | light |
| [`/System/Library/Frameworks/_AuthenticationServices_SwiftUI.framework/_AuthenticationServices_SwiftUI`](System__Library__Frameworks___AuthenticationServices_SwiftUI.framework___AuthenticationServices_SwiftUI.md) | 625.2.8.21.5 | light |
| [`/System/Library/Frameworks/_Contacts_AppIntents.framework/_Contacts_AppIntents`](System__Library__Frameworks___Contacts_AppIntents.framework___Contacts_AppIntents.md) | 3846.200.91.2.1 | light |
| [`/System/Library/Frameworks/_CoreData_CloudKit.framework/_CoreData_CloudKit`](System__Library__Frameworks___CoreData_CloudKit.framework___CoreData_CloudKit.md) | 25.0.0.0.0 | light |
| [`/System/Library/Frameworks/_CoreLocationUI_SwiftUI.framework/_CoreLocationUI_SwiftUI`](System__Library__Frameworks___CoreLocationUI_SwiftUI.framework___CoreLocationUI_SwiftUI.md) | 3187.0.1.0.0 | full |
| [`/System/Library/Frameworks/_CoreLocation_SwiftUI.framework/_CoreLocation_SwiftUI`](System__Library__Frameworks___CoreLocation_SwiftUI.framework___CoreLocation_SwiftUI.md) | 3187.0.1.0.0 | full |
| [`/System/Library/Frameworks/_CoreMotion_SwiftUI.framework/_CoreMotion_SwiftUI`](System__Library__Frameworks___CoreMotion_SwiftUI.framework___CoreMotion_SwiftUI.md) | 3187.0.1.0.0 | full |
| [`/System/Library/Frameworks/_CoreNFC_UIKit.framework/_CoreNFC_UIKit`](System__Library__Frameworks___CoreNFC_UIKit.framework___CoreNFC_UIKit.md) | 371.8.0.0.0 | full |
| [`/System/Library/Frameworks/_CoreSpotlight_FoundationModels.framework/_CoreSpotlight_FoundationModels`](System__Library__Frameworks___CoreSpotlight_FoundationModels.framework___CoreSpotlight_FoundationModels.md) | 2465.1.9.0.0 | light |
| [`/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/_DeviceActivity_SwiftUI`](System__Library__Frameworks___DeviceActivity_SwiftUI.framework___DeviceActivity_SwiftUI.md) | 407.1.5.0.0 | light |
| [`/System/Library/Frameworks/_DeviceDiscoveryUI_SwiftUI.framework/_DeviceDiscoveryUI_SwiftUI`](System__Library__Frameworks___DeviceDiscoveryUI_SwiftUI.framework___DeviceDiscoveryUI_SwiftUI.md) | 2131.21.31.21.8 | light |
| [`/System/Library/Frameworks/_FinanceKit_AppIntents.framework/_FinanceKit_AppIntents`](System__Library__Frameworks___FinanceKit_AppIntents.framework___FinanceKit_AppIntents.md) | 376.1.6.0.0 | light |
| [`/System/Library/Frameworks/_FoundationModels_UIKit.framework/_FoundationModels_UIKit`](System__Library__Frameworks___FoundationModels_UIKit.framework___FoundationModels_UIKit.md) | 2.1.14.0.0 | light |
| [`/System/Library/Frameworks/_GameController_SwiftUI.framework/_GameController_SwiftUI`](System__Library__Frameworks___GameController_SwiftUI.framework___GameController_SwiftUI.md) | 14.1.2.0.0 | light |
| [`/System/Library/Frameworks/_GeoToolbox_AppIntents.framework/_GeoToolbox_AppIntents`](System__Library__Frameworks___GeoToolbox_AppIntents.framework___GeoToolbox_AppIntents.md) | 34.31.6.17.106 | light |
| [`/System/Library/Frameworks/_HomeKit_SwiftUI.framework/_HomeKit_SwiftUI`](System__Library__Frameworks___HomeKit_SwiftUI.framework___HomeKit_SwiftUI.md) | 1520.2.7.1.3 | light |
| [`/System/Library/Frameworks/_Intents_TipKit.framework/_Intents_TipKit`](System__Library__Frameworks___Intents_TipKit.framework___Intents_TipKit.md) | 4016.1.16.0.0 | light |
| [`/System/Library/Frameworks/_LinkPresentation_AppIntents.framework/_LinkPresentation_AppIntents`](System__Library__Frameworks___LinkPresentation_AppIntents.framework___LinkPresentation_AppIntents.md) | 317.0.0.0.0 | light |
| [`/System/Library/Frameworks/_ManagedAppDistribution_SwiftUI.framework/_ManagedAppDistribution_SwiftUI`](System__Library__Frameworks___ManagedAppDistribution_SwiftUI.framework___ManagedAppDistribution_SwiftUI.md) | 3.0.23.0.0 | light |
| [`/System/Library/Frameworks/_MarketplaceKit_UIKit.framework/_MarketplaceKit_UIKit`](System__Library__Frameworks___MarketplaceKit_UIKit.framework___MarketplaceKit_UIKit.md) | 4.1.15.0.0 | light |
| [`/System/Library/Frameworks/_MediaIntents_AppIntents.framework/_MediaIntents_AppIntents`](System__Library__Frameworks___MediaIntents_AppIntents.framework___MediaIntents_AppIntents.md) | 3605.14.1.11.1 | light |
| [`/System/Library/Frameworks/_PassKit_SwiftUI.framework/_PassKit_SwiftUI`](System__Library__Frameworks___PassKit_SwiftUI.framework___PassKit_SwiftUI.md) | 1696.2.9.2.0 | light |
| [`/System/Library/Frameworks/_PermissionKit_SwiftUI.framework/_PermissionKit_SwiftUI`](System__Library__Frameworks___PermissionKit_SwiftUI.framework___PermissionKit_SwiftUI.md) | 97.125.8.0.0 | light |
| [`/System/Library/Frameworks/_PermissionKit_UIKit.framework/_PermissionKit_UIKit`](System__Library__Frameworks___PermissionKit_UIKit.framework___PermissionKit_UIKit.md) | 97.125.8.0.0 | light |
| [`/System/Library/Frameworks/_PhotosUI_SwiftUI.framework/_PhotosUI_SwiftUI`](System__Library__Frameworks___PhotosUI_SwiftUI.framework___PhotosUI_SwiftUI.md) | 916.62.154.0.0 | light |
| [`/System/Library/Frameworks/_Photos_AppIntents.framework/_Photos_AppIntents`](System__Library__Frameworks___Photos_AppIntents.framework___Photos_AppIntents.md) | 916.62.154.0.0 | light |
| [`/System/Library/Frameworks/_QuickLook_SwiftUI.framework/_QuickLook_SwiftUI`](System__Library__Frameworks___QuickLook_SwiftUI.framework___QuickLook_SwiftUI.md) | 1034.1.7.0.0 | light |
| [`/System/Library/Frameworks/_RealityKit_ComputeGraph.framework/_RealityKit_ComputeGraph`](System__Library__Frameworks___RealityKit_ComputeGraph.framework___RealityKit_ComputeGraph.md) | 30.40.1.0.0 | light |
| [`/System/Library/Frameworks/_RealityKit_SwiftUI.framework/_RealityKit_SwiftUI`](System__Library__Frameworks___RealityKit_SwiftUI.framework___RealityKit_SwiftUI.md) | 453.42.1.0.1 | light |
| [`/System/Library/Frameworks/_RelevanceKit_MapKit.framework/_RelevanceKit_MapKit`](System__Library__Frameworks___RelevanceKit_MapKit.framework___RelevanceKit_MapKit.md) | 248.1.0.0.0 | light |
| [`/System/Library/Frameworks/_SceneKit_SwiftUI.framework/_SceneKit_SwiftUI`](System__Library__Frameworks___SceneKit_SwiftUI.framework___SceneKit_SwiftUI.md) | 612.101.0.0.0 | light |
| [`/System/Library/Frameworks/_SecureElementCredential_SwiftUI.framework/_SecureElementCredential_SwiftUI`](System__Library__Frameworks___SecureElementCredential_SwiftUI.framework___SecureElementCredential_SwiftUI.md) | 71.9.3.0.0 | full |
| [`/System/Library/Frameworks/_SecureElementCredential_UIKit.framework/_SecureElementCredential_UIKit`](System__Library__Frameworks___SecureElementCredential_UIKit.framework___SecureElementCredential_UIKit.md) | 71.9.3.0.0 | full |
| [`/System/Library/Frameworks/_SharedWithYou_AppIntents.framework/_SharedWithYou_AppIntents`](System__Library__Frameworks___SharedWithYou_AppIntents.framework___SharedWithYou_AppIntents.md) | 217.200.51.0.0 | light |
| [`/System/Library/Frameworks/_SpriteKit_SwiftUI.framework/_SpriteKit_SwiftUI`](System__Library__Frameworks___SpriteKit_SwiftUI.framework___SpriteKit_SwiftUI.md) | 53.1.1.0.0 | light |
| [`/System/Library/Frameworks/_StoreKit_SwiftUI.framework/_StoreKit_SwiftUI`](System__Library__Frameworks___StoreKit_SwiftUI.framework___StoreKit_SwiftUI.md) | 816.1.16.0.0 | light |
| [`/System/Library/Frameworks/_SwiftData_CoreData.framework/_SwiftData_CoreData`](System__Library__Frameworks___SwiftData_CoreData.framework___SwiftData_CoreData.md) | 187.0.0.0.0 | light |
| [`/System/Library/Frameworks/_SwiftData_SwiftUI.framework/_SwiftData_SwiftUI`](System__Library__Frameworks___SwiftData_SwiftUI.framework___SwiftData_SwiftUI.md) | 187.0.0.0.0 | light |
| [`/System/Library/Frameworks/_Translation_SwiftUI.framework/_Translation_SwiftUI`](System__Library__Frameworks___Translation_SwiftUI.framework___Translation_SwiftUI.md) | 396.2.0.0.0 | light |
| [`/System/Library/Frameworks/_UserNotifications_AppIntents.framework/_UserNotifications_AppIntents`](System__Library__Frameworks___UserNotifications_AppIntents.framework___UserNotifications_AppIntents.md) | 720.2.7.0.0 | light |
| [`/System/Library/Frameworks/_Vision_FoundationModels.framework/_Vision_FoundationModels`](System__Library__Frameworks___Vision_FoundationModels.framework___Vision_FoundationModels.md) | 10.1.7.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend21.dylib`](usr__lib__objc__libobjcMsgSend21.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/Frameworks/_USDKit_RealityKit.framework/_USDKit_RealityKit`](System__Library__Frameworks___USDKit_RealityKit.framework___USDKit_RealityKit.md) | 106.40.4.0.1 | light |
| [`/System/Library/Frameworks/_WebKit_SwiftUI.framework/_WebKit_SwiftUI`](System__Library__Frameworks___WebKit_SwiftUI.framework___WebKit_SwiftUI.md) | 625.2.8.21.2 | light |
| [`/System/Library/Frameworks/_WorkoutKit_SwiftUI.framework/_WorkoutKit_SwiftUI`](System__Library__Frameworks___WorkoutKit_SwiftUI.framework___WorkoutKit_SwiftUI.md) | 2027.1.63.0.0 | light |
| [`/System/Library/Frameworks/iAd.framework/iAd`](System__Library__Frameworks__iAd.framework__iAd.md) | 1322.0.0.0.0 | light |
| [`/System/Library/HIDPlugins/AppleSPUAccCompassPlugin.plugin/AppleSPUAccCompassPlugin`](System__Library__HIDPlugins__AppleSPUAccCompassPlugin.plugin__AppleSPUAccCompassPlugin.md) | 1087.40.4.0.0 | full |
| [`/System/Library/HIDPlugins/AppleSPUDispCompassPlugin.plugin/AppleSPUDispCompassPlugin`](System__Library__HIDPlugins__AppleSPUDispCompassPlugin.plugin__AppleSPUDispCompassPlugin.md) | 1087.40.4.0.0 | full |
| [`/System/Library/HIDPlugins/AppleSPUHIDStatistics.plugin/AppleSPUHIDStatistics`](System__Library__HIDPlugins__AppleSPUHIDStatistics.plugin__AppleSPUHIDStatistics.md) | 1087.40.4.0.0 | full |
| [`/System/Library/HIDPlugins/IOHIDEventProcessorFilter.plugin/IOHIDEventProcessorFilter`](System__Library__HIDPlugins__IOHIDEventProcessorFilter.plugin__IOHIDEventProcessorFilter.md) | 2360.40.13.0.1 | full |
| [`/System/Library/HIDPlugins/IOHIDEventSystemStatistics.plugin/IOHIDEventSystemStatistics`](System__Library__HIDPlugins__IOHIDEventSystemStatistics.plugin__IOHIDEventSystemStatistics.md) | 2360.40.13.0.1 | full |
| [`/System/Library/HIDPlugins/IOHIDKeyboardFilter.plugin/IOHIDKeyboardFilter`](System__Library__HIDPlugins__IOHIDKeyboardFilter.plugin__IOHIDKeyboardFilter.md) | 2360.40.13.0.1 | full |
| [`/System/Library/HIDPlugins/IOHIDPointerScrollFilter.plugin/IOHIDPointerScrollFilter`](System__Library__HIDPlugins__IOHIDPointerScrollFilter.plugin__IOHIDPointerScrollFilter.md) | 2360.40.13.0.1 | full |
| [`/System/Library/HIDPlugins/IOHIDT8027USBSessionFilter.plugin/IOHIDT8027USBSessionFilter`](System__Library__HIDPlugins__IOHIDT8027USBSessionFilter.plugin__IOHIDT8027USBSessionFilter.md) | 2360.40.13.0.1 | full |
| [`/System/Library/Health/FeedItemPlugins/AppRecommendations.healthplugin/AppRecommendations`](System__Library__Health__FeedItemPlugins__AppRecommendations.healthplugin__AppRecommendations.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/FeedItemPlugins/HealthArticles.healthplugin/HealthArticles`](System__Library__Health__FeedItemPlugins__HealthArticles.healthplugin__HealthArticles.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/FeedItemPlugins/HealthCategories.healthplugin/HealthCategories`](System__Library__Health__FeedItemPlugins__HealthCategories.healthplugin__HealthCategories.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/FeedItemPlugins/HighlightAlertsPlugin.healthplugin/HighlightAlertsPlugin`](System__Library__Health__FeedItemPlugins__HighlightAlertsPlugin.healthplugin__HighlightAlertsPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/FeedItemPlugins/HighlightsPlugin.healthplugin/HighlightsPlugin`](System__Library__Health__FeedItemPlugins__HighlightsPlugin.healthplugin__HighlightsPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/FeedItemPlugins/LabKitAppPlugin.healthplugin/LabKitAppPlugin`](System__Library__Health__FeedItemPlugins__LabKitAppPlugin.healthplugin__LabKitAppPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/FeedItemPlugins/MentalHealthAppPlugin.healthplugin/MentalHealthAppPlugin`](System__Library__Health__FeedItemPlugins__MentalHealthAppPlugin.healthplugin__MentalHealthAppPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/FeedItemPlugins/MobilityAppPlugin.healthplugin/MobilityAppPlugin`](System__Library__Health__FeedItemPlugins__MobilityAppPlugin.healthplugin__MobilityAppPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/FeedItemPlugins/Profiles.healthplugin/Profiles`](System__Library__Health__FeedItemPlugins__Profiles.healthplugin__Profiles.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/FeedItemPlugins/ResearchApp.healthplugin/ResearchApp`](System__Library__Health__FeedItemPlugins__ResearchApp.healthplugin__ResearchApp.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/FeedItemPlugins/RespiratoryHealthAppPlugin.healthplugin/RespiratoryHealthAppPlugin`](System__Library__Health__FeedItemPlugins__RespiratoryHealthAppPlugin.healthplugin__RespiratoryHealthAppPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/FeedItemPlugins/SurveyKitAppPlugin.healthplugin/SurveyKitAppPlugin`](System__Library__Health__FeedItemPlugins__SurveyKitAppPlugin.healthplugin__SurveyKitAppPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/FeedItemPlugins/VisionHealthAppPlugin.healthplugin/VisionHealthAppPlugin`](System__Library__Health__FeedItemPlugins__VisionHealthAppPlugin.healthplugin__VisionHealthAppPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/Plugins/ActivityAwardsPlugin.bundle/ActivityAwardsPlugin`](System__Library__Health__Plugins__ActivityAwardsPlugin.bundle__ActivityAwardsPlugin.md) | 2027.1.4.0.0 | light |
| [`/System/Library/Health/Plugins/ActivitySharingPlugin.bundle/ActivitySharingPlugin`](System__Library__Health__Plugins__ActivitySharingPlugin.bundle__ActivitySharingPlugin.md) | 2027.1.7.0.0 | light |
| [`/System/Library/Health/Plugins/CompanionHealthPlugin.bundle/CompanionHealthPlugin`](System__Library__Health__Plugins__CompanionHealthPlugin.bundle__CompanionHealthPlugin.md) | 2027.1.48.0.0 | light |
| [`/System/Library/Health/Plugins/HealthAppPlugin.bundle/HealthAppPlugin`](System__Library__Health__Plugins__HealthAppPlugin.bundle__HealthAppPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/Plugins/HeartDaemonPlugin.bundle/HeartDaemonPlugin`](System__Library__Health__Plugins__HeartDaemonPlugin.bundle__HeartDaemonPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/Plugins/MenstrualCyclesDaemonPlugin.bundle/MenstrualCyclesDaemonPlugin`](System__Library__Health__Plugins__MenstrualCyclesDaemonPlugin.bundle__MenstrualCyclesDaemonPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/Plugins/RespiratoryHealthDaemonPlugin.bundle/RespiratoryHealthDaemonPlugin`](System__Library__Health__Plugins__RespiratoryHealthDaemonPlugin.bundle__RespiratoryHealthDaemonPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/Plugins/SleepHealthDaemonPlugin.bundle/SleepHealthDaemonPlugin`](System__Library__Health__Plugins__SleepHealthDaemonPlugin.bundle__SleepHealthDaemonPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/MediaCapture/H16ISP.mediacapture`](System__Library__MediaCapture__H16ISP.mediacapture.md) | 6.104.0.0.0 | full |
| [`/System/Library/MediaCapture/ISP.mediacapture`](System__Library__MediaCapture__ISP.mediacapture.md) | 20.112.0.0.0 | full |
| [`/System/Library/Messages/PlugIns/FaceTime.imservice/FaceTime`](System__Library__Messages__PlugIns__FaceTime.imservice__FaceTime.md) | 1491.200.101.21.5 | light |
| [`/System/Library/NanoPreferenceBundles/General/AccessibilitySettings.bundle/AccessibilitySettings`](System__Library__NanoPreferenceBundles__General__AccessibilitySettings.bundle__AccessibilitySettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/NanoTimeKit/ComplicationBundles/MessagesComplication.bundle/MessagesComplication`](System__Library__NanoTimeKit__ComplicationBundles__MessagesComplication.bundle__MessagesComplication.md) | 1491.200.101.21.5 | light |
| [`/System/Library/NanoTimeKit/ComplicationBundles/NanoCompassComplications.bundle/NanoCompassComplications`](System__Library__NanoTimeKit__ComplicationBundles__NanoCompassComplications.bundle__NanoCompassComplications.md) | 702.0.0.0.0 | light |
| [`/System/Library/NanoTimeKit/ComplicationBundles/NanoMenstrualCyclesComplication.bundle/NanoMenstrualCyclesComplication`](System__Library__NanoTimeKit__ComplicationBundles__NanoMenstrualCyclesComplication.bundle__NanoMenstrualCyclesComplication.md) | 7027.1.56.6.5 | light |
| [`/System/Library/NanoTimeKit/ComplicationBundles/NanoSleepComplication.bundle/NanoSleepComplication`](System__Library__NanoTimeKit__ComplicationBundles__NanoSleepComplication.bundle__NanoSleepComplication.md) | 7027.1.56.6.5 | light |
| [`/System/Library/NanoTimeKit/ComplicationBundles/WeatherComplications.bundle/WeatherComplications`](System__Library__NanoTimeKit__ComplicationBundles__WeatherComplications.bundle__WeatherComplications.md) | 1169.2.9.0.0 | light |
| [`/System/Library/NanoTimeKit/ComplicationBundles/WorldClockComplications.bundle/WorldClockComplications`](System__Library__NanoTimeKit__ComplicationBundles__WorldClockComplications.bundle__WorldClockComplications.md) | 354.2.1.0.0 | light |
| [`/System/Library/PreferenceBundles/AVKitSettings.bundle/AVKitSettings`](System__Library__PreferenceBundles__AVKitSettings.bundle__AVKitSettings.md) | 1392.5.0.0.0 | light |
| [`/System/Library/PreferenceBundles/AirPortSettings.bundle/AirPortSettings`](System__Library__PreferenceBundles__AirPortSettings.bundle__AirPortSettings.md) | 1175.0.0.0.0 | light |
| [`/System/Library/PreferenceBundles/BluetoothSettings.bundle/BluetoothSettings`](System__Library__PreferenceBundles__BluetoothSettings.bundle__BluetoothSettings.md) | 2701.4.0.0.0 | full |
| [`/System/Library/PreferenceBundles/CarrierSettings.bundle/CarrierSettings`](System__Library__PreferenceBundles__CarrierSettings.bundle__CarrierSettings.md) | 3079.200.81.21.2 | light |
| [`/System/Library/PreferenceBundles/EDGESettings.bundle/EDGESettings`](System__Library__PreferenceBundles__EDGESettings.bundle__EDGESettings.md) | 1080.0.0.0.0 | light |
| [`/System/Library/PreferenceBundles/MobilePhoneSettings.bundle/MobilePhoneSettings`](System__Library__PreferenceBundles__MobilePhoneSettings.bundle__MobilePhoneSettings.md) | 3079.200.81.21.2 | light |
| [`/System/Library/PreferenceBundles/ScheduleSettings.bundle/ScheduleSettings`](System__Library__PreferenceBundles__ScheduleSettings.bundle__ScheduleSettings.md) | 91.0.0.0.0 | light |
| [`/System/Library/PreferenceBundles/WirelessModemSettings.bundle/WirelessModemSettings`](System__Library__PreferenceBundles__WirelessModemSettings.bundle__WirelessModemSettings.md) | 840.22.0.0.0 | light |
| [`/System/Library/Previews/ShellPlugins/WidgetPreviewsShellPlugin.bundle/WidgetPreviewsShellPlugin`](System__Library__Previews__ShellPlugins__WidgetPreviewsShellPlugin.bundle__WidgetPreviewsShellPlugin.md) | 7749.2.13.0.3 | light |
| [`/System/Library/PrivateFrameworks/AAAFoundationUI.framework/AAAFoundationUI`](System__Library__PrivateFrameworks__AAAFoundationUI.framework__AAAFoundationUI.md) | 117.125.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/AACCore.framework/AACCore`](System__Library__PrivateFrameworks__AACCore.framework__AACCore.md) | 56.40.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/ABMHelper.framework/ABMHelper`](System__Library__PrivateFrameworks__ABMHelper.framework__ABMHelper.md) | 1594.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ACCBaker.framework/ACCBaker`](System__Library__PrivateFrameworks__ACCBaker.framework__ACCBaker.md) | 2.5.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ACIAdapter.framework/ACIAdapter`](System__Library__PrivateFrameworks__ACIAdapter.framework__ACIAdapter.md) | 202.4.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ACSEFoundation.framework/ACSEFoundation`](System__Library__PrivateFrameworks__ACSEFoundation.framework__ACSEFoundation.md) | 301.24.1.1.0 | light |
| [`/System/Library/PrivateFrameworks/ACTFramework.framework/ACTFramework`](System__Library__PrivateFrameworks__ACTFramework.framework__ACTFramework.md) | 560.40.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/AFKUser.framework/AFKUser`](System__Library__PrivateFrameworks__AFKUser.framework__AFKUser.md) | 743.40.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/AGXCompilerCore.framework/AGXCompilerCore`](System__Library__PrivateFrameworks__AGXCompilerCore.framework__AGXCompilerCore.md) | 362.5.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AGXGPURawCounter.framework/AGXGPURawCounter`](System__Library__PrivateFrameworks__AGXGPURawCounter.framework__AGXGPURawCounter.md) | 362.5.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/ALDataTypes.framework/ALDataTypes.dylib`](System__Library__PrivateFrameworks__ALDataTypes.framework__ALDataTypes.dylib.md) | 131.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ALSKit.framework/ALSKit`](System__Library__PrivateFrameworks__ALSKit.framework__ALSKit.md) | 2300.52.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/AMPCoreUI.framework/AMPCoreUI`](System__Library__PrivateFrameworks__AMPCoreUI.framework__AMPCoreUI.md) | 1453.1.1.2.2 | full |
| [`/System/Library/PrivateFrameworks/ANEClientSignals.framework/ANEClientSignals`](System__Library__PrivateFrameworks__ANEClientSignals.framework__ANEClientSignals.md) | 10.102.4.0.0 | full |
| [`/System/Library/PrivateFrameworks/ANECompiler.framework/libORTools.dylib`](System__Library__PrivateFrameworks__ANECompiler.framework__libORTools.dylib.md) | 10.205.4.0.0 | full |
| [`/System/Library/PrivateFrameworks/ANEServices.framework/ANEServices`](System__Library__PrivateFrameworks__ANEServices.framework__ANEServices.md) | 10.102.4.0.0 | full |
| [`/System/Library/PrivateFrameworks/ANSTKit.framework/ANSTKit`](System__Library__PrivateFrameworks__ANSTKit.framework__ANSTKit.md) | 45.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AONVL.framework/AONVL`](System__Library__PrivateFrameworks__AONVL.framework__AONVL.md) | 131.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AOPHaptics.framework/AOPHaptics`](System__Library__PrivateFrameworks__AOPHaptics.framework__AOPHaptics.md) | 1087.40.4.0.0 | full |
| [`/System/Library/PrivateFrameworks/AOSKit.framework/AOSKit`](System__Library__PrivateFrameworks__AOSKit.framework__AOSKit.md) | 125.2.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/APFS.framework/APFS`](System__Library__PrivateFrameworks__APFS.framework__APFS.md) | 3288.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/APTransport.framework/APTransport`](System__Library__PrivateFrameworks__APTransport.framework__APTransport.md) | 1005.13.1.1.0 | light |
| [`/System/Library/PrivateFrameworks/ARKitDaemon.framework/ARKitDaemon`](System__Library__PrivateFrameworks__ARKitDaemon.framework__ARKitDaemon.md) | 781.40.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/ASEProcessing.framework/ASEProcessing`](System__Library__PrivateFrameworks__ASEProcessing.framework__ASEProcessing.md) | 1.59.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/ASMExclaveSupport.framework/ASMExclaveSupport`](System__Library__PrivateFrameworks__ASMExclaveSupport.framework__ASMExclaveSupport.md) | 20.27.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/ASOctaneSupport.framework/ASOctaneSupport`](System__Library__PrivateFrameworks__ASOctaneSupport.framework__ASOctaneSupport.md) | 816.1.16.0.0 | full |
| [`/System/Library/PrivateFrameworks/ASRBridge.framework/ASRBridge`](System__Library__PrivateFrameworks__ASRBridge.framework__ASRBridge.md) | 3605.32.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AUDeveloperSettings.framework/AUDeveloperSettings`](System__Library__PrivateFrameworks__AUDeveloperSettings.framework__AUDeveloperSettings.md) | 1587.40.33.0.0 | light |
| [`/System/Library/PrivateFrameworks/AUSettings.framework/AUSettings`](System__Library__PrivateFrameworks__AUSettings.framework__AUSettings.md) | 1587.40.33.0.0 | light |
| [`/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/GKSPerformance.framework/GKSPerformance`](System__Library__PrivateFrameworks__AVConference.framework__Frameworks__GKSPerformance.framework__GKSPerformance.md) | 2263.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ICE.framework/ICE`](System__Library__PrivateFrameworks__AVConference.framework__Frameworks__ICE.framework__ICE.md) | 2263.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/LegacyHandle.framework/LegacyHandle`](System__Library__PrivateFrameworks__AVConference.framework__Frameworks__LegacyHandle.framework__LegacyHandle.md) | 2263.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/SimpleKeyExchange.framework/SimpleKeyExchange`](System__Library__PrivateFrameworks__AVConference.framework__Frameworks__SimpleKeyExchange.framework__SimpleKeyExchange.md) | 2263.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/snatmap.framework/snatmap`](System__Library__PrivateFrameworks__AVConference.framework__Frameworks__snatmap.framework__snatmap.md) | 2263.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AXAggregateStatisticsServices.framework/AXAggregateStatisticsServices`](System__Library__PrivateFrameworks__AXAggregateStatisticsServices.framework__AXAggregateStatisticsServices.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AXContainerServices.framework/AXContainerServices`](System__Library__PrivateFrameworks__AXContainerServices.framework__AXContainerServices.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AXElementInteraction.framework/AXElementInteraction`](System__Library__PrivateFrameworks__AXElementInteraction.framework__AXElementInteraction.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AXFrontBoardUtils.framework/AXFrontBoardUtils`](System__Library__PrivateFrameworks__AXFrontBoardUtils.framework__AXFrontBoardUtils.md) | 3245.8.9.0.0 | full |
| [`/System/Library/PrivateFrameworks/AXIDSServices.framework/AXIDSServices`](System__Library__PrivateFrameworks__AXIDSServices.framework__AXIDSServices.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AXImageExplorerServices.framework/AXImageExplorerServices`](System__Library__PrivateFrameworks__AXImageExplorerServices.framework__AXImageExplorerServices.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AXLocalizationCaptionService.framework/AXLocalizationCaptionService`](System__Library__PrivateFrameworks__AXLocalizationCaptionService.framework__AXLocalizationCaptionService.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AXMotionCuesServices.framework/AXMotionCuesServices`](System__Library__PrivateFrameworks__AXMotionCuesServices.framework__AXMotionCuesServices.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AXNTKUtilities.framework/AXNTKUtilities`](System__Library__PrivateFrameworks__AXNTKUtilities.framework__AXNTKUtilities.md) | 1040.4.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/AXSoundDetection.framework/AXSoundDetection`](System__Library__PrivateFrameworks__AXSoundDetection.framework__AXSoundDetection.md) | 543.2.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/AXSoundDetectionUI.framework/AXSoundDetectionUI`](System__Library__PrivateFrameworks__AXSoundDetectionUI.framework__AXSoundDetectionUI.md) | 543.2.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/AXSpeakFingerManager.framework/AXSpeakFingerManager`](System__Library__PrivateFrameworks__AXSpeakFingerManager.framework__AXSpeakFingerManager.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AXSpeechAssetServices.framework/AXSpeechAssetServices`](System__Library__PrivateFrameworks__AXSpeechAssetServices.framework__AXSpeechAssetServices.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AXTapToSpeakTime.framework/AXTapToSpeakTime`](System__Library__PrivateFrameworks__AXTapToSpeakTime.framework__AXTapToSpeakTime.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AXWatchRemoteScreenServices.framework/AXWatchRemoteScreenServices`](System__Library__PrivateFrameworks__AXWatchRemoteScreenServices.framework__AXWatchRemoteScreenServices.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AXWatchRemoteScreenUI.framework/AXWatchRemoteScreenUI`](System__Library__PrivateFrameworks__AXWatchRemoteScreenUI.framework__AXWatchRemoteScreenUI.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccelerateGPU.framework/AccelerateGPU`](System__Library__PrivateFrameworks__AccelerateGPU.framework__AccelerateGPU.md) | 35.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccelerateOpt.framework/AccelerateOpt`](System__Library__PrivateFrameworks__AccelerateOpt.framework__AccelerateOpt.md) | 7.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccelerateOpt.framework/libipopt.dylib`](System__Library__PrivateFrameworks__AccelerateOpt.framework__libipopt.dylib.md) | 7.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccessibilityAudit.framework/AccessibilityAudit`](System__Library__PrivateFrameworks__AccessibilityAudit.framework__AccessibilityAudit.md) | 193.2.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccessibilityFocusEngine.framework/AccessibilityFocusEngine`](System__Library__PrivateFrameworks__AccessibilityFocusEngine.framework__AccessibilityFocusEngine.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccessibilityPhysicalInteraction.framework/AccessibilityPhysicalInteraction`](System__Library__PrivateFrameworks__AccessibilityPhysicalInteraction.framework__AccessibilityPhysicalInteraction.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccessibilityPlatformTranslation.framework/AccessibilityPlatformTranslation`](System__Library__PrivateFrameworks__AccessibilityPlatformTranslation.framework__AccessibilityPlatformTranslation.md) | 591.4.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccessibilityReaderData.framework/AccessibilityReaderData`](System__Library__PrivateFrameworks__AccessibilityReaderData.framework__AccessibilityReaderData.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccessibilityReaderServices.framework/AccessibilityReaderServices`](System__Library__PrivateFrameworks__AccessibilityReaderServices.framework__AccessibilityReaderServices.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccessibilityReadingUI.framework/AccessibilityReadingUI`](System__Library__PrivateFrameworks__AccessibilityReadingUI.framework__AccessibilityReadingUI.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccessibilityRemoteServices.framework/AccessibilityRemoteServices`](System__Library__PrivateFrameworks__AccessibilityRemoteServices.framework__AccessibilityRemoteServices.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccessibilityRemoteUIServices.framework/AccessibilityRemoteUIServices`](System__Library__PrivateFrameworks__AccessibilityRemoteUIServices.framework__AccessibilityRemoteUIServices.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccessibilitySettingsUI.framework/AccessibilitySettingsUI`](System__Library__PrivateFrameworks__AccessibilitySettingsUI.framework__AccessibilitySettingsUI.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccessibilitySharedUISupport.framework/AccessibilitySharedUISupport`](System__Library__PrivateFrameworks__AccessibilitySharedUISupport.framework__AccessibilitySharedUISupport.md) | 591.4.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccessibilityUI.framework/AccessibilityUI`](System__Library__PrivateFrameworks__AccessibilityUI.framework__AccessibilityUI.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService`](System__Library__PrivateFrameworks__AccessibilityUIService.framework__AccessibilityUIService.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccessibilityUIShared.framework/AccessibilityUIShared`](System__Library__PrivateFrameworks__AccessibilityUIShared.framework__AccessibilityUIShared.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccessibilityUIViewServices.framework/AccessibilityUIViewServices`](System__Library__PrivateFrameworks__AccessibilityUIViewServices.framework__AccessibilityUIViewServices.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccessoryAudio.framework/AccessoryAudio`](System__Library__PrivateFrameworks__AccessoryAudio.framework__AccessoryAudio.md) | 1219.52.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/AccessoryComponentAuth.framework/AccessoryComponentAuth`](System__Library__PrivateFrameworks__AccessoryComponentAuth.framework__AccessoryComponentAuth.md) | 1219.52.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/AccessoryContextualService.framework/AccessoryContextualService`](System__Library__PrivateFrameworks__AccessoryContextualService.framework__AccessoryContextualService.md) | 41.7.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AccessoryDaemonSupport.framework/AccessoryDaemonSupport`](System__Library__PrivateFrameworks__AccessoryDaemonSupport.framework__AccessoryDaemonSupport.md) | 41.7.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AccessoryFirmwareUpdate.framework/AccessoryFirmwareUpdate`](System__Library__PrivateFrameworks__AccessoryFirmwareUpdate.framework__AccessoryFirmwareUpdate.md) | 33.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AccessoryLiveActivitiesUI.framework/AccessoryLiveActivitiesUI`](System__Library__PrivateFrameworks__AccessoryLiveActivitiesUI.framework__AccessoryLiveActivitiesUI.md) | 7749.2.13.0.3 | full |
| [`/System/Library/PrivateFrameworks/AccessorySensorManagerDarwin_Private.framework/AccessorySensorManagerDarwin_Private`](System__Library__PrivateFrameworks__AccessorySensorManagerDarwin_Private.framework__AccessorySensorManagerDarwin_Private.md) | 20.27.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AccessorySensorManagerDefines_Private.framework/AccessorySensorManagerDefines_Private`](System__Library__PrivateFrameworks__AccessorySensorManagerDefines_Private.framework__AccessorySensorManagerDefines_Private.md) | 20.27.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AccessorySensorManagerExclaveDaemon.framework/AccessorySensorManagerExclaveDaemon`](System__Library__PrivateFrameworks__AccessorySensorManagerExclaveDaemon.framework__AccessorySensorManagerExclaveDaemon.md) | 20.27.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AccessorySensorManagerServices.framework/AccessorySensorManagerServices`](System__Library__PrivateFrameworks__AccessorySensorManagerServices.framework__AccessorySensorManagerServices.md) | 20.27.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AccessoryServices.framework/AccessoryServices`](System__Library__PrivateFrameworks__AccessoryServices.framework__AccessoryServices.md) | 41.7.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AccessorySetupKitCore.framework/AccessorySetupKitCore`](System__Library__PrivateFrameworks__AccessorySetupKitCore.framework__AccessorySetupKitCore.md) | 2701.6.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AccessoryTypes.framework/AccessoryTypes`](System__Library__PrivateFrameworks__AccessoryTypes.framework__AccessoryTypes.md) | 41.7.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AccessoryVoiceOver.framework/AccessoryVoiceOver`](System__Library__PrivateFrameworks__AccessoryVoiceOver.framework__AccessoryVoiceOver.md) | 1219.52.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/AccessoryXPCServices.framework/AccessoryXPCServices`](System__Library__PrivateFrameworks__AccessoryXPCServices.framework__AccessoryXPCServices.md) | 41.7.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AccessoryiAP2Shim.framework/AccessoryiAP2Shim`](System__Library__PrivateFrameworks__AccessoryiAP2Shim.framework__AccessoryiAP2Shim.md) | 1219.52.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/AccountNotification.framework/AccountNotification`](System__Library__PrivateFrameworks__AccountNotification.framework__AccountNotification.md) | 14.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccountSuggestions.framework/AccountSuggestions`](System__Library__PrivateFrameworks__AccountSuggestions.framework__AccountSuggestions.md) | 113.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon`](System__Library__PrivateFrameworks__AccountsDaemon.framework__AccountsDaemon.md) | 1125.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccountsUISettings.framework/AccountsUISettings`](System__Library__PrivateFrameworks__AccountsUISettings.framework__AccountsUISettings.md) | 113.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AccountsUISupport.framework/AccountsUISupport`](System__Library__PrivateFrameworks__AccountsUISupport.framework__AccountsUISupport.md) | 3901.200.71.21.4 | light |
| [`/System/Library/PrivateFrameworks/AccountsUISupportShared.framework/AccountsUISupportShared`](System__Library__PrivateFrameworks__AccountsUISupportShared.framework__AccountsUISupportShared.md) | 3901.200.71.21.4 | light |
| [`/System/Library/PrivateFrameworks/AcousticMaterials.framework/AcousticMaterials`](System__Library__PrivateFrameworks__AcousticMaterials.framework__AcousticMaterials.md) | 24.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ActionButtonConfigurationUI.framework/ActionButtonConfigurationUI`](System__Library__PrivateFrameworks__ActionButtonConfigurationUI.framework__ActionButtonConfigurationUI.md) | 68.101.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ActionButtonSelector.framework/ActionButtonSelector`](System__Library__PrivateFrameworks__ActionButtonSelector.framework__ActionButtonSelector.md) | 68.101.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ActionKitUI.framework/ActionKitUI`](System__Library__PrivateFrameworks__ActionKitUI.framework__ActionKitUI.md) | 5114.0.12.0.0 | light |
| [`/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/ActionPredictionHeuristics`](System__Library__PrivateFrameworks__ActionPredictionHeuristics.framework__ActionPredictionHeuristics.md) | 678.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ActivityAchievements.framework/ActivityAchievements`](System__Library__PrivateFrameworks__ActivityAchievements.framework__ActivityAchievements.md) | 2027.1.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/ActivityAchievementsDaemon.framework/ActivityAchievementsDaemon`](System__Library__PrivateFrameworks__ActivityAchievementsDaemon.framework__ActivityAchievementsDaemon.md) | 2027.1.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/ActivityAwardsClient.framework/ActivityAwardsClient`](System__Library__PrivateFrameworks__ActivityAwardsClient.framework__ActivityAwardsClient.md) | 2027.1.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/ActivityAwardsCore.framework/ActivityAwardsCore`](System__Library__PrivateFrameworks__ActivityAwardsCore.framework__ActivityAwardsCore.md) | 2027.1.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/ActivityAwardsServices.framework/ActivityAwardsServices`](System__Library__PrivateFrameworks__ActivityAwardsServices.framework__ActivityAwardsServices.md) | 2027.1.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/ActivityProgressKit.framework/ActivityProgressKit`](System__Library__PrivateFrameworks__ActivityProgressKit.framework__ActivityProgressKit.md) | 391.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ActivitySharing.framework/ActivitySharing`](System__Library__PrivateFrameworks__ActivitySharing.framework__ActivitySharing.md) | 2027.1.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/ActivitySharingDaemonCore.framework/ActivitySharingDaemonCore`](System__Library__PrivateFrameworks__ActivitySharingDaemonCore.framework__ActivitySharingDaemonCore.md) | 2027.1.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/ActivitySharingHealthDaemon.framework/ActivitySharingHealthDaemon`](System__Library__PrivateFrameworks__ActivitySharingHealthDaemon.framework__ActivitySharingHealthDaemon.md) | 2027.1.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/ActivitySharingUI.framework/ActivitySharingUI`](System__Library__PrivateFrameworks__ActivitySharingUI.framework__ActivitySharingUI.md) | 2027.1.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/AdCore.framework/AdCore`](System__Library__PrivateFrameworks__AdCore.framework__AdCore.md) | 638.2.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/AdID.framework/AdID`](System__Library__PrivateFrameworks__AdID.framework__AdID.md) | 638.2.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/AdPlatforms.framework/AdPlatforms`](System__Library__PrivateFrameworks__AdPlatforms.framework__AdPlatforms.md) | 638.2.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/AdPlatformsCommonUI.framework/AdPlatformsCommonUI`](System__Library__PrivateFrameworks__AdPlatformsCommonUI.framework__AdPlatformsCommonUI.md) | 557.2.14.0.0 | light |
| [`/System/Library/PrivateFrameworks/AdPlatformsInternal.framework/AdPlatformsInternal`](System__Library__PrivateFrameworks__AdPlatformsInternal.framework__AdPlatformsInternal.md) | 638.2.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/AdaptiveMesh.framework/AdaptiveMesh`](System__Library__PrivateFrameworks__AdaptiveMesh.framework__AdaptiveMesh.md) | 14.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AdaptiveMusic.framework/AdaptiveMusic`](System__Library__PrivateFrameworks__AdaptiveMusic.framework__AdaptiveMusic.md) | 27.2.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AdaptiveVoiceShortcuts.framework/AdaptiveVoiceShortcuts`](System__Library__PrivateFrameworks__AdaptiveVoiceShortcuts.framework__AdaptiveVoiceShortcuts.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AdminLite.framework/AdminLite`](System__Library__PrivateFrameworks__AdminLite.framework__AdminLite.md) | 8.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AeroML.framework/AeroML`](System__Library__PrivateFrameworks__AeroML.framework__AeroML.md) | 99.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AfibBurden.framework/AfibBurden`](System__Library__PrivateFrameworks__AfibBurden.framework__AfibBurden.md) | 20.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AgentCanvasUIFoundation.framework/AgentCanvasUIFoundation`](System__Library__PrivateFrameworks__AgentCanvasUIFoundation.framework__AgentCanvasUIFoundation.md) | 3605.10.2.11.9 | light |
| [`/System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary`](System__Library__PrivateFrameworks__AggregateDictionary.framework__AggregateDictionary.md) | 446.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AggregateDictionaryHistory.framework/AggregateDictionaryHistory`](System__Library__PrivateFrameworks__AggregateDictionaryHistory.framework__AggregateDictionaryHistory.md) | 446.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AirDropSettingsSupport.framework/AirDropSettingsSupport`](System__Library__PrivateFrameworks__AirDropSettingsSupport.framework__AirDropSettingsSupport.md) | 2027.1.1.101.0 | light |
| [`/System/Library/PrivateFrameworks/AirPlayAndHandoffSettingsSupport.framework/AirPlayAndHandoffSettingsSupport`](System__Library__PrivateFrameworks__AirPlayAndHandoffSettingsSupport.framework__AirPlayAndHandoffSettingsSupport.md) | 2027.1.1.101.0 | light |
| [`/System/Library/PrivateFrameworks/AirPlayKit.framework/AirPlayKit`](System__Library__PrivateFrameworks__AirPlayKit.framework__AirPlayKit.md) | 2027.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AirPlayOverlays.framework/AirPlayOverlays`](System__Library__PrivateFrameworks__AirPlayOverlays.framework__AirPlayOverlays.md) | 807.4.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AirPlayOverlaysServer.framework/AirPlayOverlaysServer`](System__Library__PrivateFrameworks__AirPlayOverlaysServer.framework__AirPlayOverlaysServer.md) | 807.4.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver`](System__Library__PrivateFrameworks__AirPlayReceiver.framework__AirPlayReceiver.md) | 1005.13.1.1.0 | light |
| [`/System/Library/PrivateFrameworks/AirPlayReceiverKit.framework/AirPlayReceiverKit`](System__Library__PrivateFrameworks__AirPlayReceiverKit.framework__AirPlayReceiverKit.md) | 1005.13.1.1.0 | light |
| [`/System/Library/PrivateFrameworks/AirPlayRoutePrediction.framework/AirPlayRoutePrediction`](System__Library__PrivateFrameworks__AirPlayRoutePrediction.framework__AirPlayRoutePrediction.md) | 1977.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender`](System__Library__PrivateFrameworks__AirPlaySender.framework__AirPlaySender.md) | 1005.13.1.1.0 | light |
| [`/System/Library/PrivateFrameworks/AirPlaySenderKit.framework/AirPlaySenderKit`](System__Library__PrivateFrameworks__AirPlaySenderKit.framework__AirPlaySenderKit.md) | 1005.13.1.1.0 | light |
| [`/System/Library/PrivateFrameworks/AirPlaySenderUI.framework/AirPlaySenderUI`](System__Library__PrivateFrameworks__AirPlaySenderUI.framework__AirPlaySenderUI.md) | 1005.13.1.1.0 | light |
| [`/System/Library/PrivateFrameworks/AirPortAssistant.framework/AirPortAssistant`](System__Library__PrivateFrameworks__AirPortAssistant.framework__AirPortAssistant.md) | 116.30.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AirTraffic.framework/AirTraffic`](System__Library__PrivateFrameworks__AirTraffic.framework__AirTraffic.md) | 4026.200.21.0.0 | light |
| [`/System/Library/PrivateFrameworks/Airship.framework/Airship`](System__Library__PrivateFrameworks__Airship.framework__Airship.md) | 592.0.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/AirshipCentauriHelper.framework/AirshipCentauriHelper`](System__Library__PrivateFrameworks__AirshipCentauriHelper.framework__AirshipCentauriHelper.md) | 592.0.3.0.0 | full |
| [`/System/Library/PrivateFrameworks/AlarmAppIntents.framework/AlarmAppIntents`](System__Library__PrivateFrameworks__AlarmAppIntents.framework__AlarmAppIntents.md) | 308.2.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/AlarmKitCore.framework/AlarmKitCore`](System__Library__PrivateFrameworks__AlarmKitCore.framework__AlarmKitCore.md) | 2333.2.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/AlarmKitFoundation.framework/AlarmKitFoundation`](System__Library__PrivateFrameworks__AlarmKitFoundation.framework__AlarmKitFoundation.md) | 2333.2.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/AlarmUIFramework.framework/AlarmUIFramework`](System__Library__PrivateFrameworks__AlarmUIFramework.framework__AlarmUIFramework.md) | 3605.13.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AlchemistBase.framework/AlchemistBase`](System__Library__PrivateFrameworks__AlchemistBase.framework__AlchemistBase.md) | 32.0.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/AlchemistService.framework/AlchemistService`](System__Library__PrivateFrameworks__AlchemistService.framework__AlchemistService.md) | 32.0.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/AlgorithmsInternal.framework/AlgorithmsInternal`](System__Library__PrivateFrameworks__AlgorithmsInternal.framework__AlgorithmsInternal.md) | 5027.1.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) | 29.0.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/AlwaysOnExclavesDaemon.framework/AlwaysOnExclavesDaemon`](System__Library__PrivateFrameworks__AlwaysOnExclavesDaemon.framework__AlwaysOnExclavesDaemon.md) | 66.40.15.0.0 | full |
| [`/System/Library/PrivateFrameworks/AlwaysOnExclavesServices.framework/AlwaysOnExclavesServices`](System__Library__PrivateFrameworks__AlwaysOnExclavesServices.framework__AlwaysOnExclavesServices.md) | 66.40.15.0.0 | full |
| [`/System/Library/PrivateFrameworks/Ambient.framework/Ambient`](System__Library__PrivateFrameworks__Ambient.framework__Ambient.md) | 109.2.1.0.2 | light |
| [`/System/Library/PrivateFrameworks/AmbientSceneScope.framework/AmbientSceneScope`](System__Library__PrivateFrameworks__AmbientSceneScope.framework__AmbientSceneScope.md) | 9.26.4.12.0 | light |
| [`/System/Library/PrivateFrameworks/AmbientUI.framework/AmbientUI`](System__Library__PrivateFrameworks__AmbientUI.framework__AmbientUI.md) | 109.2.1.0.2 | light |
| [`/System/Library/PrivateFrameworks/AmbientUIKit.framework/AmbientUIKit`](System__Library__PrivateFrameworks__AmbientUIKit.framework__AmbientUIKit.md) | 109.2.1.0.2 | light |
| [`/System/Library/PrivateFrameworks/AmbientUIServices.framework/AmbientUIServices`](System__Library__PrivateFrameworks__AmbientUIServices.framework__AmbientUIServices.md) | 109.2.1.0.2 | light |
| [`/System/Library/PrivateFrameworks/AnnotationKit.framework/AnnotationKit`](System__Library__PrivateFrameworks__AnnotationKit.framework__AnnotationKit.md) | 584.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/Announce.framework/Announce`](System__Library__PrivateFrameworks__Announce.framework__Announce.md) | 340.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AnnounceAppIntents.framework/AnnounceAppIntents`](System__Library__PrivateFrameworks__AnnounceAppIntents.framework__AnnounceAppIntents.md) | 340.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AnnounceSiriExtensions.framework/AnnounceSiriExtensions`](System__Library__PrivateFrameworks__AnnounceSiriExtensions.framework__AnnounceSiriExtensions.md) | 340.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/Anvil.framework/Anvil`](System__Library__PrivateFrameworks__Anvil.framework__Anvil.md) | 112.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppC3D.framework/AppC3D`](System__Library__PrivateFrameworks__AppC3D.framework__AppC3D.md) | 1.25.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppConduit.framework/AppConduit`](System__Library__PrivateFrameworks__AppConduit.framework__AppConduit.md) | 408.40.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppDistributionKit.framework/AppDistributionKit`](System__Library__PrivateFrameworks__AppDistributionKit.framework__AppDistributionKit.md) | 4.1.15.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppDistributionUI.framework/AppDistributionUI`](System__Library__PrivateFrameworks__AppDistributionUI.framework__AppDistributionUI.md) | 4.1.15.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppInstallationMetrics.framework/AppInstallationMetrics`](System__Library__PrivateFrameworks__AppInstallationMetrics.framework__AppInstallationMetrics.md) | 3.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppIntentSchemas.framework/AppIntentSchemas`](System__Library__PrivateFrameworks__AppIntentSchemas.framework__AppIntentSchemas.md) | 3502.1.16.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppIntentsCLISupport.framework/AppIntentsCLISupport`](System__Library__PrivateFrameworks__AppIntentsCLISupport.framework__AppIntentsCLISupport.md) | 301.1.16.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppManagedFeaturesUI.framework/AppManagedFeaturesUI`](System__Library__PrivateFrameworks__AppManagedFeaturesUI.framework__AppManagedFeaturesUI.md) | 58.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppNotificationsLoggingClient.framework/AppNotificationsLoggingClient`](System__Library__PrivateFrameworks__AppNotificationsLoggingClient.framework__AppNotificationsLoggingClient.md) | 678.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppPredictionToolsInternal.framework/AppPredictionToolsInternal`](System__Library__PrivateFrameworks__AppPredictionToolsInternal.framework__AppPredictionToolsInternal.md) | 678.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppPredictionUI.framework/AppPredictionUI`](System__Library__PrivateFrameworks__AppPredictionUI.framework__AppPredictionUI.md) | 678.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppPredictionUIFoundation.framework/AppPredictionUIFoundation`](System__Library__PrivateFrameworks__AppPredictionUIFoundation.framework__AppPredictionUIFoundation.md) | 678.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppPredictionUIWidget.framework/AppPredictionUIWidget`](System__Library__PrivateFrameworks__AppPredictionUIWidget.framework__AppPredictionUIWidget.md) | 678.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppPrivateData.framework/AppPrivateData`](System__Library__PrivateFrameworks__AppPrivateData.framework__AppPrivateData.md) | 5.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppProtectionDaemon.framework/AppProtectionDaemon`](System__Library__PrivateFrameworks__AppProtectionDaemon.framework__AppProtectionDaemon.md) | 55.1.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppProtectionUI.framework/AppProtectionUI`](System__Library__PrivateFrameworks__AppProtectionUI.framework__AppProtectionUI.md) | 55.1.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppRemoteAssets.framework/AppRemoteAssets`](System__Library__PrivateFrameworks__AppRemoteAssets.framework__AppRemoteAssets.md) | 30.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppRestrictionsUI.framework/AppRestrictionsUI`](System__Library__PrivateFrameworks__AppRestrictionsUI.framework__AppRestrictionsUI.md) | 22.2.2.100.0 | light |
| [`/System/Library/PrivateFrameworks/AppSSOKerberos.framework/AppSSOKerberos`](System__Library__PrivateFrameworks__AppSSOKerberos.framework__AppSSOKerberos.md) | 643.40.34.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppSSOUI.framework/AppSSOUI`](System__Library__PrivateFrameworks__AppSSOUI.framework__AppSSOUI.md) | 643.40.34.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppServerSupport.framework/AppServerSupport`](System__Library__PrivateFrameworks__AppServerSupport.framework__AppServerSupport.md) | 3298.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppStoreEvalLighthouseUtils.framework/AppStoreEvalLighthouseUtils`](System__Library__PrivateFrameworks__AppStoreEvalLighthouseUtils.framework__AppStoreEvalLighthouseUtils.md) | 1.5.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppStoreFoundation.framework/AppStoreFoundation`](System__Library__PrivateFrameworks__AppStoreFoundation.framework__AppStoreFoundation.md) | 13.1.17.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppStoreOverlays.framework/AppStoreOverlays`](System__Library__PrivateFrameworks__AppStoreOverlays.framework__AppStoreOverlays.md) | 27.1.12.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppStoreUI.framework/AppStoreUI`](System__Library__PrivateFrameworks__AppStoreUI.framework__AppStoreUI.md) | 1203.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppStoreUtilities.framework/AppStoreUtilities`](System__Library__PrivateFrameworks__AppStoreUtilities.framework__AppStoreUtilities.md) | 13.1.17.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppSubscriptions.framework/AppSubscriptions`](System__Library__PrivateFrameworks__AppSubscriptions.framework__AppSubscriptions.md) | 72.3.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppSystemSettings.framework/AppSystemSettings`](System__Library__PrivateFrameworks__AppSystemSettings.framework__AppSystemSettings.md) | 2027.1.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppSystemSettingsUI.framework/AppSystemSettingsUI`](System__Library__PrivateFrameworks__AppSystemSettingsUI.framework__AppSystemSettingsUI.md) | 2027.1.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppUserEvents.framework/AppUserEvents`](System__Library__PrivateFrameworks__AppUserEvents.framework__AppUserEvents.md) | 12.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleAccountTransparency.framework/AppleAccountTransparency`](System__Library__PrivateFrameworks__AppleAccountTransparency.framework__AppleAccountTransparency.md) | 448.125.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI`](System__Library__PrivateFrameworks__AppleAccountUI.framework__AppleAccountUI.md) | 589.125.11.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleBasebandLink.framework/AppleBasebandLink`](System__Library__PrivateFrameworks__AppleBasebandLink.framework__AppleBasebandLink.md) | 1594.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AppleBasebandManager.framework/AppleBasebandManager`](System__Library__PrivateFrameworks__AppleBasebandManager.framework__AppleBasebandManager.md) | 1594.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AppleBasebandServices.framework/AppleBasebandServices`](System__Library__PrivateFrameworks__AppleBasebandServices.framework__AppleBasebandServices.md) | 1594.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AppleCV3DMOVKit.framework/AppleCV3DMOVKit`](System__Library__PrivateFrameworks__AppleCV3DMOVKit.framework__AppleCV3DMOVKit.md) | 9.26.7.9.0 | light |
| [`/System/Library/PrivateFrameworks/AppleCV3DModels.framework/AppleCV3DModels`](System__Library__PrivateFrameworks__AppleCV3DModels.framework__AppleCV3DModels.md) | 9.26.7.9.0 | light |
| [`/System/Library/PrivateFrameworks/AppleCVA.framework/AppleCVA`](System__Library__PrivateFrameworks__AppleCVA.framework__AppleCVA.md) | 1003.0.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleCVAPhoto.framework/AppleCVAPhoto`](System__Library__PrivateFrameworks__AppleCVAPhoto.framework__AppleCVAPhoto.md) | 620.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleCVHWA.framework/AppleCVHWA`](System__Library__PrivateFrameworks__AppleCVHWA.framework__AppleCVHWA.md) | 4.4.14.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleCameraISPExclaveKitServices.framework/AppleCameraISPExclaveKitServices`](System__Library__PrivateFrameworks__AppleCameraISPExclaveKitServices.framework__AppleCameraISPExclaveKitServices.md) | 20.112.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AppleCareSupport.framework/AppleCareSupport`](System__Library__PrivateFrameworks__AppleCareSupport.framework__AppleCareSupport.md) | 11.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleConvergedFirmwareUpdater.framework/AppleConvergedFirmwareUpdater`](System__Library__PrivateFrameworks__AppleConvergedFirmwareUpdater.framework__AppleConvergedFirmwareUpdater.md) | 468.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleDepth.framework/AppleDepth`](System__Library__PrivateFrameworks__AppleDepth.framework__AppleDepth.md) | 177.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleDepthCore.framework/AppleDepthCore`](System__Library__PrivateFrameworks__AppleDepthCore.framework__AppleDepthCore.md) | 177.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/AppleDeviceQuerySupport`](System__Library__PrivateFrameworks__AppleDeviceQuerySupport.framework__AppleDeviceQuerySupport.md) | 459.40.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/libZhuGeArmory.dylib`](System__Library__PrivateFrameworks__AppleDeviceQuerySupport.framework__libZhuGeArmory.dylib.md) | 459.40.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/libZhuGeRoster.dylib`](System__Library__PrivateFrameworks__AppleDeviceQuerySupport.framework__libZhuGeRoster.dylib.md) | 459.40.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleEmbeddedDisplayServices.framework/AppleEmbeddedDisplayServices`](System__Library__PrivateFrameworks__AppleEmbeddedDisplayServices.framework__AppleEmbeddedDisplayServices.md) | 230.40.6.0.0 | full |
| [`/System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression`](System__Library__PrivateFrameworks__AppleFSCompression.framework__AppleFSCompression.md) | 182.40.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleFirmwareUpdate.framework/AppleFirmwareUpdate`](System__Library__PrivateFrameworks__AppleFirmwareUpdate.framework__AppleFirmwareUpdate.md) | 1587.40.33.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleFlatBuffers.framework/AppleFlatBuffers`](System__Library__PrivateFrameworks__AppleFlatBuffers.framework__AppleFlatBuffers.md) | 17.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleGPIOUser.framework/AppleGPIOUser`](System__Library__PrivateFrameworks__AppleGPIOUser.framework__AppleGPIOUser.md) | 68.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleHIDFeedback.framework/AppleHIDFeedback`](System__Library__PrivateFrameworks__AppleHIDFeedback.framework__AppleHIDFeedback.md) | 14.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AppleHIDTransportSupport.framework/AppleHIDTransportSupport`](System__Library__PrivateFrameworks__AppleHIDTransportSupport.framework__AppleHIDTransportSupport.md) | 10110.1.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AppleIDAuthSupport.framework/AppleIDAuthSupport`](System__Library__PrivateFrameworks__AppleIDAuthSupport.framework__AppleIDAuthSupport.md) | 115.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup`](System__Library__PrivateFrameworks__AppleIDSetup.framework__AppleIDSetup.md) | 129.125.7.1.0 | light |
| [`/System/Library/PrivateFrameworks/AppleIDSetupDaemon.framework/AppleIDSetupDaemon`](System__Library__PrivateFrameworks__AppleIDSetupDaemon.framework__AppleIDSetupDaemon.md) | 129.125.7.1.0 | light |
| [`/System/Library/PrivateFrameworks/AppleIDSetupUI.framework/AppleIDSetupUI`](System__Library__PrivateFrameworks__AppleIDSetupUI.framework__AppleIDSetupUI.md) | 129.125.7.1.0 | light |
| [`/System/Library/PrivateFrameworks/AppleIntelligenceReportingProcessing.framework/AppleIntelligenceReportingProcessing`](System__Library__PrivateFrameworks__AppleIntelligenceReportingProcessing.framework__AppleIntelligenceReportingProcessing.md) | 232.40.17.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleJPEG.framework/AppleJPEG`](System__Library__PrivateFrameworks__AppleJPEG.framework__AppleJPEG.md) | 246.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleJPEGXL.framework/AppleJPEGXL`](System__Library__PrivateFrameworks__AppleJPEGXL.framework__AppleJPEGXL.md) | 24.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleLDAP.framework/AppleLDAP`](System__Library__PrivateFrameworks__AppleLDAP.framework__AppleLDAP.md) | 63.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleLatticeSupport.framework/AppleLatticeSupport`](System__Library__PrivateFrameworks__AppleLatticeSupport.framework__AppleLatticeSupport.md) | 200.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleMSG.framework/AppleMSG`](System__Library__PrivateFrameworks__AppleMSG.framework__AppleMSG.md) | 420.0.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleMediaServicesKitSupport.framework/AppleMediaServicesKitSupport`](System__Library__PrivateFrameworks__AppleMediaServicesKitSupport.framework__AppleMediaServicesKitSupport.md) | 10.1.18.2.1 | light |
| [`/System/Library/PrivateFrameworks/AppleMipcRouter.framework/AppleMipcRouter`](System__Library__PrivateFrameworks__AppleMipcRouter.framework__AppleMipcRouter.md) | 1594.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity`](System__Library__PrivateFrameworks__AppleMobileFileIntegrity.framework__AppleMobileFileIntegrity.md) | 1171.40.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleNVMe.framework/AppleNVMe`](System__Library__PrivateFrameworks__AppleNVMe.framework__AppleNVMe.md) | 877.40.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/ApplePDPHelper.framework/ApplePDPHelper`](System__Library__PrivateFrameworks__ApplePDPHelper.framework__ApplePDPHelper.md) | 186.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ApplePhotonDetectorServices.framework/ApplePhotonDetectorServices`](System__Library__PrivateFrameworks__ApplePhotonDetectorServices.framework__ApplePhotonDetectorServices.md) | 10.66.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleSARHelper.framework/AppleSARHelper`](System__Library__PrivateFrameworks__AppleSARHelper.framework__AppleSARHelper.md) | 1594.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleSRP.framework/AppleSRP`](System__Library__PrivateFrameworks__AppleSRP.framework__AppleSRP.md) | 40.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleSauce.framework/AppleSauce`](System__Library__PrivateFrameworks__AppleSauce.framework__AppleSauce.md) | 17.7.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleServiceToolkit.framework/AppleServiceToolkit`](System__Library__PrivateFrameworks__AppleServiceToolkit.framework__AppleServiceToolkit.md) | 234.40.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleSplatRendering.framework/AppleSplatRendering`](System__Library__PrivateFrameworks__AppleSplatRendering.framework__AppleSplatRendering.md) | 20.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppleTracingSupportSymbolication.framework/AppleTracingSupportSymbolication`](System__Library__PrivateFrameworks__AppleTracingSupportSymbolication.framework__AppleTracingSupportSymbolication.md) | 210.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AppliedSensingFitness.framework/AppliedSensingFitness`](System__Library__PrivateFrameworks__AppliedSensingFitness.framework__AppliedSensingFitness.md) | 27.0.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/ArchetypeFoundation.framework/ArchetypeFoundation`](System__Library__PrivateFrameworks__ArchetypeFoundation.framework__ArchetypeFoundation.md) | 41.14.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ArchetypeUI.framework/ArchetypeUI`](System__Library__PrivateFrameworks__ArchetypeUI.framework__ArchetypeUI.md) | 41.14.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ArgumentParserInternal.framework/ArgumentParserInternal`](System__Library__PrivateFrameworks__ArgumentParserInternal.framework__ArgumentParserInternal.md) | 1.3.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/Asen.framework/Asen.dylib`](System__Library__PrivateFrameworks__Asen.framework__Asen.dylib.md) | 131.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AskPermission.framework/AskPermission`](System__Library__PrivateFrameworks__AskPermission.framework__AskPermission.md) | 130.1.7.2.2 | light |
| [`/System/Library/PrivateFrameworks/AskTo.framework/AskTo`](System__Library__PrivateFrameworks__AskTo.framework__AskTo.md) | 97.125.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/AskToCore.framework/AskToCore`](System__Library__PrivateFrameworks__AskToCore.framework__AskToCore.md) | 97.125.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/AskToDaemon.framework/AskToDaemon`](System__Library__PrivateFrameworks__AskToDaemon.framework__AskToDaemon.md) | 97.125.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/AskToUI.framework/AskToUI`](System__Library__PrivateFrameworks__AskToUI.framework__AskToUI.md) | 97.125.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices`](System__Library__PrivateFrameworks__AssertionServices.framework__AssertionServices.md) | 1084.40.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/AssetCacheServices.framework/AssetCacheServices`](System__Library__PrivateFrameworks__AssetCacheServices.framework__AssetCacheServices.md) | 157.40.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/AssetCacheServicesExtensions.framework/AssetCacheServicesExtensions`](System__Library__PrivateFrameworks__AssetCacheServicesExtensions.framework__AssetCacheServicesExtensions.md) | 157.40.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/AssetExplorer.framework/AssetExplorer`](System__Library__PrivateFrameworks__AssetExplorer.framework__AssetExplorer.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/AssetViewer.framework/AssetViewer`](System__Library__PrivateFrameworks__AssetViewer.framework__AssetViewer.md) | 567.40.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/AssistantActionSuggestion.framework/AssistantActionSuggestion`](System__Library__PrivateFrameworks__AssistantActionSuggestion.framework__AssistantActionSuggestion.md) | 678.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AssistantCardServiceSupport.framework/AssistantCardServiceSupport`](System__Library__PrivateFrameworks__AssistantCardServiceSupport.framework__AssistantCardServiceSupport.md) | 3605.23.2.3.0 | light |
| [`/System/Library/PrivateFrameworks/AssistantSettingsFoundation.framework/AssistantSettingsFoundation`](System__Library__PrivateFrameworks__AssistantSettingsFoundation.framework__AssistantSettingsFoundation.md) | 3605.23.2.3.0 | light |
| [`/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettingsSupport`](System__Library__PrivateFrameworks__AssistantSettingsSupport.framework__AssistantSettingsSupport.md) | 3605.23.2.3.0 | light |
| [`/System/Library/PrivateFrameworks/AssistiveTouchUI.framework/AssistiveTouchUI`](System__Library__PrivateFrameworks__AssistiveTouchUI.framework__AssistiveTouchUI.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/AudioAccessoryAssetManagement.framework/AudioAccessoryAssetManagement`](System__Library__PrivateFrameworks__AudioAccessoryAssetManagement.framework__AudioAccessoryAssetManagement.md) | 41.7.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) | 41.7.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AudioDSPAnalysis.framework/AudioDSPAnalysis`](System__Library__PrivateFrameworks__AudioDSPAnalysis.framework__AudioDSPAnalysis.md) | 24.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AudioDataAnalysis.framework/AudioDataAnalysis`](System__Library__PrivateFrameworks__AudioDataAnalysis.framework__AudioDataAnalysis.md) | 881.210.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AudioDiagnosticExtensionCore.framework/AudioDiagnosticExtensionCore`](System__Library__PrivateFrameworks__AudioDiagnosticExtensionCore.framework__AudioDiagnosticExtensionCore.md) | 196.206.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AudioPasscode.framework/AudioPasscode`](System__Library__PrivateFrameworks__AudioPasscode.framework__AudioPasscode.md) | 68.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AudioPasscodeDSP.framework/AudioPasscodeDSP`](System__Library__PrivateFrameworks__AudioPasscodeDSP.framework__AudioPasscodeDSP.md) | 68.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AudioServerApplication.framework/AudioServerApplication`](System__Library__PrivateFrameworks__AudioServerApplication.framework__AudioServerApplication.md) | 1200.31.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AudioServerDriver.framework/AudioServerDriver`](System__Library__PrivateFrameworks__AudioServerDriver.framework__AudioServerDriver.md) | 1200.31.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AudioServerDriverTransports_Base.framework/AudioServerDriverTransports_Base`](System__Library__PrivateFrameworks__AudioServerDriverTransports_Base.framework__AudioServerDriverTransports_Base.md) | 400.35.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOA2.framework/AudioServerDriverTransports_IOA2`](System__Library__PrivateFrameworks__AudioServerDriverTransports_IOA2.framework__AudioServerDriverTransports_IOA2.md) | 400.35.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOP.framework/AudioServerDriverTransports_IOP`](System__Library__PrivateFrameworks__AudioServerDriverTransports_IOP.framework__AudioServerDriverTransports_IOP.md) | 400.35.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer`](System__Library__PrivateFrameworks__AudioSessionServer.framework__AudioSessionServer.md) | 449.207.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/AudioTranscriptionAnalysis.framework/AudioTranscriptionAnalysis`](System__Library__PrivateFrameworks__AudioTranscriptionAnalysis.framework__AudioTranscriptionAnalysis.md) | 30.4.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AudioTransportCommon.framework/AudioTransportCommon`](System__Library__PrivateFrameworks__AudioTransportCommon.framework__AudioTransportCommon.md) | 500.2.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AudiogramIngestion.framework/AudiogramIngestion`](System__Library__PrivateFrameworks__AudiogramIngestion.framework__AudiogramIngestion.md) | 543.2.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore`](System__Library__PrivateFrameworks__AuthenticationServicesCore.framework__AuthenticationServicesCore.md) | 625.2.8.21.5 | light |
| [`/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore`](System__Library__PrivateFrameworks__AutoBugCaptureCore.framework__AutoBugCaptureCore.md) | 469.40.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/AutoFillCore.framework/AutoFillCore`](System__Library__PrivateFrameworks__AutoFillCore.framework__AutoFillCore.md) | 43.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AutoLoop.framework/AutoLoop`](System__Library__PrivateFrameworks__AutoLoop.framework__AutoLoop.md) | 58.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AutoUnlock.framework/AutoUnlock`](System__Library__PrivateFrameworks__AutoUnlock.framework__AutoUnlock.md) | 2131.21.31.21.8 | light |
| [`/System/Library/PrivateFrameworks/AutoUnlockDaemon.framework/AutoUnlockDaemon`](System__Library__PrivateFrameworks__AutoUnlockDaemon.framework__AutoUnlockDaemon.md) | 2131.21.31.21.8 | light |
| [`/System/Library/PrivateFrameworks/AutomationMode.framework/AutomationMode`](System__Library__PrivateFrameworks__AutomationMode.framework__AutomationMode.md) | 35.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AvailabilityKit.framework/AvailabilityKit`](System__Library__PrivateFrameworks__AvailabilityKit.framework__AvailabilityKit.md) | 154.200.31.0.0 | light |
| [`/System/Library/PrivateFrameworks/AvatarPersistence.framework/AvatarPersistence`](System__Library__PrivateFrameworks__AvatarPersistence.framework__AvatarPersistence.md) | 406.200.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AvatarPoster.framework/AvatarPoster`](System__Library__PrivateFrameworks__AvatarPoster.framework__AvatarPoster.md) | 406.200.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/BNNSCoreAIDelegate.framework/BNNSCoreAIDelegate`](System__Library__PrivateFrameworks__BNNSCoreAIDelegate.framework__BNNSCoreAIDelegate.md) | 2212.42.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/BNNSGraphPCC.framework/BNNSGraphPCC`](System__Library__PrivateFrameworks__BNNSGraphPCC.framework__BNNSGraphPCC.md) | 2212.42.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/BNNSOdieDelegate.framework/BNNSOdieDelegate`](System__Library__PrivateFrameworks__BNNSOdieDelegate.framework__BNNSOdieDelegate.md) | 2212.42.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/BTCSEngine.framework/BTCSEngine`](System__Library__PrivateFrameworks__BTCSEngine.framework__BTCSEngine.md) | 2701.7.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/BackBoardHIDEventProcessors.framework/BackBoardHIDEventProcessors`](System__Library__PrivateFrameworks__BackBoardHIDEventProcessors.framework__BackBoardHIDEventProcessors.md) | 877.2.2.600.0 | full |
| [`/System/Library/PrivateFrameworks/BackgroundTaskAgent.framework/BackgroundTaskAgent`](System__Library__PrivateFrameworks__BackgroundTaskAgent.framework__BackgroundTaskAgent.md) | 63.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/BagKit.framework/BagKit`](System__Library__PrivateFrameworks__BagKit.framework__BagKit.md) | 2003.200.71.2.4 | light |
| [`/System/Library/PrivateFrameworks/BarcodeSupport.framework/BarcodeSupport`](System__Library__PrivateFrameworks__BarcodeSupport.framework__BarcodeSupport.md) | 1039.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/BarcodeSupportUI.framework/BarcodeSupportUI`](System__Library__PrivateFrameworks__BarcodeSupportUI.framework__BarcodeSupportUI.md) | 1039.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/BasebandTraceHelper.framework/BasebandTraceHelper`](System__Library__PrivateFrameworks__BasebandTraceHelper.framework__BasebandTraceHelper.md) | 1594.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/BatteryAlgorithms.framework/BatteryAlgorithms`](System__Library__PrivateFrameworks__BatteryAlgorithms.framework__BatteryAlgorithms.md) | 156.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/BatteryCenter.framework/BatteryCenter`](System__Library__PrivateFrameworks__BatteryCenter.framework__BatteryCenter.md) | 328.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/BatteryIntelligence.framework/BatteryIntelligence`](System__Library__PrivateFrameworks__BatteryIntelligence.framework__BatteryIntelligence.md) | 231.40.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/BehaviorMiner.framework/BehaviorMiner`](System__Library__PrivateFrameworks__BehaviorMiner.framework__BehaviorMiner.md) | 100.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/BinaryParsingInternal.framework/BinaryParsingInternal`](System__Library__PrivateFrameworks__BinaryParsingInternal.framework__BinaryParsingInternal.md) | 5027.1.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/BiomeSync.framework/BiomeSync`](System__Library__PrivateFrameworks__BiomeSync.framework__BiomeSync.md) | 259.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) | 685.1.3.0.1 | full |
| [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/Frameworks/Fluid.framework/Fluid`](System__Library__PrivateFrameworks__BiometricKitUI.framework__Frameworks__Fluid.framework__Fluid.md) | 685.1.3.0.1 | light |
| [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/Frameworks/MTLSpline.framework/MTLSpline`](System__Library__PrivateFrameworks__BiometricKitUI.framework__Frameworks__MTLSpline.framework__MTLSpline.md) | 685.1.3.0.1 | full |
| [`/System/Library/PrivateFrameworks/BiometricSupport.framework/BiometricSupport`](System__Library__PrivateFrameworks__BiometricSupport.framework__BiometricSupport.md) | 578.40.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/Biscuits.framework/Biscuits`](System__Library__PrivateFrameworks__Biscuits.framework__Biscuits.md) | 2.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/BlockMonitoring.framework/BlockMonitoring`](System__Library__PrivateFrameworks__BlockMonitoring.framework__BlockMonitoring.md) | 441.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/BluetoothAudio.framework/BluetoothAudio`](System__Library__PrivateFrameworks__BluetoothAudio.framework__BluetoothAudio.md) | 2701.7.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager`](System__Library__PrivateFrameworks__BluetoothManager.framework__BluetoothManager.md) | 2701.7.1.0.0 | full |
| [`/usr/lib/objc/libobjcMsgSend22.dylib`](usr__lib__objc__libobjcMsgSend22.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/BluetoothServices.framework/BluetoothServices`](System__Library__PrivateFrameworks__BluetoothServices.framework__BluetoothServices.md) | 41.7.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/BluetoothServicesUI.framework/BluetoothServicesUI`](System__Library__PrivateFrameworks__BluetoothServicesUI.framework__BluetoothServicesUI.md) | 41.7.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/Bom.framework/Bom`](System__Library__PrivateFrameworks__Bom.framework__Bom.md) | 280.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/BookCoverUtility.framework/BookCoverUtility`](System__Library__PrivateFrameworks__BookCoverUtility.framework__BookCoverUtility.md) | 2354.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/BookLibrary.framework/BookLibrary`](System__Library__PrivateFrameworks__BookLibrary.framework__BookLibrary.md) | 2354.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/BookLibraryCore.framework/BookLibraryCore`](System__Library__PrivateFrameworks__BookLibraryCore.framework__BookLibraryCore.md) | 2354.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/BookUtility.framework/BookUtility`](System__Library__PrivateFrameworks__BookUtility.framework__BookUtility.md) | 2354.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/BrailleFoundation.framework/BrailleFoundation`](System__Library__PrivateFrameworks__BrailleFoundation.framework__BrailleFoundation.md) | 467.3.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/BrailleServer.framework/BrailleServer`](System__Library__PrivateFrameworks__BrailleServer.framework__BrailleServer.md) | 467.3.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/BrailleSymbology.framework/BrailleSymbology`](System__Library__PrivateFrameworks__BrailleSymbology.framework__BrailleSymbology.md) | 591.4.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/BrailleTranslation.framework/BrailleTranslation`](System__Library__PrivateFrameworks__BrailleTranslation.framework__BrailleTranslation.md) | 467.3.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/BrainTrust.framework/BrainTrust`](System__Library__PrivateFrameworks__BrainTrust.framework__BrainTrust.md) | 2718.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/BreathingAlgorithms.framework/BreathingAlgorithms`](System__Library__PrivateFrameworks__BreathingAlgorithms.framework__BreathingAlgorithms.md) | 35.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/BridgeCommons.framework/BridgeCommons`](System__Library__PrivateFrameworks__BridgeCommons.framework__BridgeCommons.md) | 1373.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/BridgeLiveActivity.framework/BridgeLiveActivity`](System__Library__PrivateFrameworks__BridgeLiveActivity.framework__BridgeLiveActivity.md) | 1373.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/BridgePreferences.framework/BridgePreferences`](System__Library__PrivateFrameworks__BridgePreferences.framework__BridgePreferences.md) | 1373.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/BridgeReporting.framework/BridgeReporting`](System__Library__PrivateFrameworks__BridgeReporting.framework__BridgeReporting.md) | 1373.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/BridgeSecurePairing.framework/BridgeSecurePairing`](System__Library__PrivateFrameworks__BridgeSecurePairing.framework__BridgeSecurePairing.md) | 1373.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/BrightnessControl.framework/BrightnessControl`](System__Library__PrivateFrameworks__BrightnessControl.framework__BrightnessControl.md) | 2300.52.5.0.0 | full |
| [`/System/Library/PrivateFrameworks/BrookDataCollection.framework/BrookDataCollection`](System__Library__PrivateFrameworks__BrookDataCollection.framework__BrookDataCollection.md) | 253.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/BrookServices.framework/BrookServices`](System__Library__PrivateFrameworks__BrookServices.framework__BrookServices.md) | 253.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/BrowserSupportKit.framework/BrowserSupportKit`](System__Library__PrivateFrameworks__BrowserSupportKit.framework__BrowserSupportKit.md) | 625.2.8.21.5 | light |
| [`/System/Library/PrivateFrameworks/BufferSharingService.framework/BufferSharingService`](System__Library__PrivateFrameworks__BufferSharingService.framework__BufferSharingService.md) | 256.0.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard`](System__Library__PrivateFrameworks__BulletinBoard.framework__BulletinBoard.md) | 955.2.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/BulletinDistributorCompanion.framework/BulletinDistributorCompanion`](System__Library__PrivateFrameworks__BulletinDistributorCompanion.framework__BulletinDistributorCompanion.md) | 382.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/BusinessChatService.framework/BusinessChatService`](System__Library__PrivateFrameworks__BusinessChatService.framework__BusinessChatService.md) | 30123.31.8.11.4 | light |
| [`/System/Library/PrivateFrameworks/BusinessFoundation.framework/BusinessFoundation`](System__Library__PrivateFrameworks__BusinessFoundation.framework__BusinessFoundation.md) | 30123.31.8.11.4 | light |
| [`/System/Library/PrivateFrameworks/BusinessServices.framework/BusinessServices`](System__Library__PrivateFrameworks__BusinessServices.framework__BusinessServices.md) | 30123.31.8.11.4 | light |
| [`/System/Library/PrivateFrameworks/BusinessServicesUI.framework/BusinessServicesUI`](System__Library__PrivateFrameworks__BusinessServicesUI.framework__BusinessServicesUI.md) | 30123.31.8.11.4 | light |
| [`/System/Library/PrivateFrameworks/ButtonResolver.framework/ButtonResolver`](System__Library__PrivateFrameworks__ButtonResolver.framework__ButtonResolver.md) | 41.40.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/ByteMatrixVerification.framework/ByteMatrixVerification`](System__Library__PrivateFrameworks__ByteMatrixVerification.framework__ByteMatrixVerification.md) | 383.40.14.0.0 | light |
| [`/System/Library/PrivateFrameworks/C2.framework/C2`](System__Library__PrivateFrameworks__C2.framework__C2.md) | 2700.112.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CAFCombine.framework/CAFCombine`](System__Library__PrivateFrameworks__CAFCombine.framework__CAFCombine.md) | 552.7.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CAFUI.framework/CAFUI`](System__Library__PrivateFrameworks__CAFUI.framework__CAFUI.md) | 552.7.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CBORLibrary.framework/CBORLibrary`](System__Library__PrivateFrameworks__CBORLibrary.framework__CBORLibrary.md) | 6.0.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/CDDataAccess.framework/CDDataAccess`](System__Library__PrivateFrameworks__CDDataAccess.framework__CDDataAccess.md) | 4080.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CDDataAccess.framework/Frameworks/DACalDAV.framework/DACalDAV`](System__Library__PrivateFrameworks__CDDataAccess.framework__Frameworks__DACalDAV.framework__DACalDAV.md) | 4080.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CDDataAccess.framework/Frameworks/DACoreDAVGlue.framework/DACoreDAVGlue`](System__Library__PrivateFrameworks__CDDataAccess.framework__Frameworks__DACoreDAVGlue.framework__DACoreDAVGlue.md) | 4080.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CDDataAccess.framework/Frameworks/DADaemonSupport.framework/DADaemonSupport`](System__Library__PrivateFrameworks__CDDataAccess.framework__Frameworks__DADaemonSupport.framework__DADaemonSupport.md) | 4080.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CDDataAccessExpress.framework/CDDataAccessExpress`](System__Library__PrivateFrameworks__CDDataAccessExpress.framework__CDDataAccessExpress.md) | 4080.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore`](System__Library__PrivateFrameworks__CMCaptureCore.framework__CMCaptureCore.md) | 764.42.9.0.0 | full |
| [`/System/Library/PrivateFrameworks/CMCaptureDevice.framework/CMCaptureDevice`](System__Library__PrivateFrameworks__CMCaptureDevice.framework__CMCaptureDevice.md) | 764.42.9.0.0 | full |
| [`/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore`](System__Library__PrivateFrameworks__CMContinuityCaptureCore.framework__CMContinuityCaptureCore.md) | 764.42.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/CMContinuityCaptureHost.framework/CMContinuityCaptureHost`](System__Library__PrivateFrameworks__CMContinuityCaptureHost.framework__CMContinuityCaptureHost.md) | 764.42.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/CMContinuityCaptureNWActorProtocols.framework/CMContinuityCaptureNWActorProtocols`](System__Library__PrivateFrameworks__CMContinuityCaptureNWActorProtocols.framework__CMContinuityCaptureNWActorProtocols.md) | 764.42.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/CMContinuityCaptureRemote.framework/CMContinuityCaptureRemote`](System__Library__PrivateFrameworks__CMContinuityCaptureRemote.framework__CMContinuityCaptureRemote.md) | 764.42.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/CPAnalytics.framework/CPAnalytics`](System__Library__PrivateFrameworks__CPAnalytics.framework__CPAnalytics.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/CPMLBestShim.framework/CPMLBestShim`](System__Library__PrivateFrameworks__CPMLBestShim.framework__CPMLBestShim.md) | 117.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CPMS.framework/CPMS`](System__Library__PrivateFrameworks__CPMS.framework__CPMS.md) | 1191.40.27.0.1 | light |
| [`/System/Library/PrivateFrameworks/CSExattrCrypto.framework/CSExattrCrypto`](System__Library__PrivateFrameworks__CSExattrCrypto.framework__CSExattrCrypto.md) | 2465.1.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/CTBlastDoorSupport.framework/CTBlastDoorSupport`](System__Library__PrivateFrameworks__CTBlastDoorSupport.framework__CTBlastDoorSupport.md) | 13499.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CTCarrierSpace.framework/CTCarrierSpace`](System__Library__PrivateFrameworks__CTCarrierSpace.framework__CTCarrierSpace.md) | 13499.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CTLazuliSupport.framework/CTLazuliSupport`](System__Library__PrivateFrameworks__CTLazuliSupport.framework__CTLazuliSupport.md) | 13499.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CacheExpert.framework/CacheExpert`](System__Library__PrivateFrameworks__CacheExpert.framework__CacheExpert.md) | 11.40.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/CalDAV.framework/CalDAV`](System__Library__PrivateFrameworks__CalDAV.framework__CalDAV.md) | 1166.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CalendarMigration.framework/CalendarMigration`](System__Library__PrivateFrameworks__CalendarMigration.framework__CalendarMigration.md) | 1291.2.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/CalendarNotification.framework/CalendarNotification`](System__Library__PrivateFrameworks__CalendarNotification.framework__CalendarNotification.md) | 1547.2.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CalendarUIKitInternal.framework/CalendarUIKitInternal`](System__Library__PrivateFrameworks__CalendarUIKitInternal.framework__CalendarUIKitInternal.md) | 1327.2.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/CallAudioServiceClient.framework/CallAudioServiceClient`](System__Library__PrivateFrameworks__CallAudioServiceClient.framework__CallAudioServiceClient.md) | 2774.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CallsPersistence.framework/CallsPersistence`](System__Library__PrivateFrameworks__CallsPersistence.framework__CallsPersistence.md) | 158.200.81.21.9 | light |
| [`/System/Library/PrivateFrameworks/CallsUtilities.framework/CallsUtilities`](System__Library__PrivateFrameworks__CallsUtilities.framework__CallsUtilities.md) | 158.200.81.21.9 | light |
| [`/System/Library/PrivateFrameworks/CallsXPC.framework/CallsXPC`](System__Library__PrivateFrameworks__CallsXPC.framework__CallsXPC.md) | 158.200.81.21.9 | light |
| [`/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`](System__Library__PrivateFrameworks__CameraColorProcessing.framework__CameraColorProcessing.md) | 764.42.9.0.0 | full |
| [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) | 6312.0.6.0.0 | full |
| [`/System/Library/PrivateFrameworks/CameraOverlayServices.framework/CameraOverlayServices`](System__Library__PrivateFrameworks__CameraOverlayServices.framework__CameraOverlayServices.md) | 4178.40.10.0.0 | full |
| [`/System/Library/PrivateFrameworks/CampoUIServices.framework/CampoUIServices`](System__Library__PrivateFrameworks__CampoUIServices.framework__CampoUIServices.md) | 3605.10.2.11.9 | light |
| [`/System/Library/PrivateFrameworks/CaptiveNetwork.framework/CaptiveNetwork`](System__Library__PrivateFrameworks__CaptiveNetwork.framework__CaptiveNetwork.md) | 545.40.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/CarAccessoryDaemon.framework/CarAccessoryDaemon`](System__Library__PrivateFrameworks__CarAccessoryDaemon.framework__CarAccessoryDaemon.md) | 552.7.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) | 552.7.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/CarAssetUtils.framework/CarAssetUtils`](System__Library__PrivateFrameworks__CarAssetUtils.framework__CarAssetUtils.md) | 509.8.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CarCommandsUIFramework.framework/CarCommandsUIFramework`](System__Library__PrivateFrameworks__CarCommandsUIFramework.framework__CarCommandsUIFramework.md) | 3605.4.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CarPlayAssetUI.framework/CarPlayAssetUI`](System__Library__PrivateFrameworks__CarPlayAssetUI.framework__CarPlayAssetUI.md) | 509.8.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CarPlayDesignLibrary.framework/CarPlayDesignLibrary`](System__Library__PrivateFrameworks__CarPlayDesignLibrary.framework__CarPlayDesignLibrary.md) | 2.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CarPlayDisplayUtils.framework/CarPlayDisplayUtils`](System__Library__PrivateFrameworks__CarPlayDisplayUtils.framework__CarPlayDisplayUtils.md) | 807.4.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/CarPlayServices.framework/CarPlayServices`](System__Library__PrivateFrameworks__CarPlayServices.framework__CarPlayServices.md) | 591.6.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CarPlaySetup.framework/CarPlaySetup`](System__Library__PrivateFrameworks__CarPlaySetup.framework__CarPlaySetup.md) | 807.4.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport`](System__Library__PrivateFrameworks__CarPlaySupport.framework__CarPlaySupport.md) | 552.7.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CarPlayUI.framework/CarPlayUI`](System__Library__PrivateFrameworks__CarPlayUI.framework__CarPlayUI.md) | 552.7.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CarPlayUIServices.framework/CarPlayUIServices`](System__Library__PrivateFrameworks__CarPlayUIServices.framework__CarPlayUIServices.md) | 591.6.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CarbonCore.framework/CarbonCore`](System__Library__PrivateFrameworks__CarbonCore.framework__CarbonCore.md) | 1406.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/CardServices.framework/CardServices`](System__Library__PrivateFrameworks__CardServices.framework__CardServices.md) | 3520.8.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CardioHealth.framework/CardioHealth`](System__Library__PrivateFrameworks__CardioHealth.framework__CardioHealth.md) | 3187.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/Cards.framework/Cards`](System__Library__PrivateFrameworks__Cards.framework__Cards.md) | 3520.8.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine`](System__Library__PrivateFrameworks__CascadeEngine.framework__CascadeEngine.md) | 259.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/Catalyst.framework/Catalyst`](System__Library__PrivateFrameworks__Catalyst.framework__Catalyst.md) | 24.40.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/Categories.framework/Categories`](System__Library__PrivateFrameworks__Categories.framework__Categories.md) | 58.1.7.1.0 | light |
| [`/System/Library/PrivateFrameworks/Celestial.framework/Celestial`](System__Library__PrivateFrameworks__Celestial.framework__Celestial.md) | 3385.14.1.3.0 | light |
| [`/System/Library/PrivateFrameworks/CellularBridgeUI.framework/CellularBridgeUI`](System__Library__PrivateFrameworks__CellularBridgeUI.framework__CellularBridgeUI.md) | 1161.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/CellularDataDiagnosticsSuite.framework/CellularDataDiagnosticsSuite`](System__Library__PrivateFrameworks__CellularDataDiagnosticsSuite.framework__CellularDataDiagnosticsSuite.md) | 1251.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CellularPlanManager.framework/CellularPlanManager`](System__Library__PrivateFrameworks__CellularPlanManager.framework__CellularPlanManager.md) | 13499.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/Centauri.framework/Centauri`](System__Library__PrivateFrameworks__Centauri.framework__Centauri.md) | 129.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/CentauriAlphaPatchBay.framework/CentauriAlphaPatchBay`](System__Library__PrivateFrameworks__CentauriAlphaPatchBay.framework__CentauriAlphaPatchBay.md) | 92.4.10.0.0 | full |
| [`/System/Library/PrivateFrameworks/CentauriBetaPatchBay.framework/CentauriBetaPatchBay`](System__Library__PrivateFrameworks__CentauriBetaPatchBay.framework__CentauriBetaPatchBay.md) | 26.218.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/CentauriBooter.framework/CentauriBooter`](System__Library__PrivateFrameworks__CentauriBooter.framework__CentauriBooter.md) | 80.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/CentauriController.framework/CentauriController`](System__Library__PrivateFrameworks__CentauriController.framework__CentauriController.md) | 129.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/CentauriDiagnostic.framework/CentauriDiagnostic`](System__Library__PrivateFrameworks__CentauriDiagnostic.framework__CentauriDiagnostic.md) | 129.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/CertInfo.framework/CertInfo`](System__Library__PrivateFrameworks__CertInfo.framework__CertInfo.md) | 2055.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CertUI.framework/CertUI`](System__Library__PrivateFrameworks__CertUI.framework__CertUI.md) | 2055.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CheckerBoardServices.framework/CheckerBoardServices`](System__Library__PrivateFrameworks__CheckerBoardServices.framework__CheckerBoardServices.md) | 294.40.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/Chirp.framework/Chirp`](System__Library__PrivateFrameworks__Chirp.framework__Chirp.md) | 383.40.14.0.0 | light |
| [`/System/Library/PrivateFrameworks/ChronoCore.framework/Support/WidgetPreviewsExtensionAgent.bundle/WidgetPreviewsExtensionAgent`](System__Library__PrivateFrameworks__ChronoCore.framework__Support__WidgetPreviewsExtensionAgent.bundle__WidgetPreviewsExtensionAgent.md) | 7749.2.13.0.3 | light |
| [`/System/Library/PrivateFrameworks/ChronoCore.framework/Support/WidgetPreviewsSupport.framework/WidgetPreviewsSupport`](System__Library__PrivateFrameworks__ChronoCore.framework__Support__WidgetPreviewsSupport.framework__WidgetPreviewsSupport.md) | 7749.2.13.0.3 | light |
| [`/System/Library/PrivateFrameworks/ChunkingLibrary.framework/ChunkingLibrary`](System__Library__PrivateFrameworks__ChunkingLibrary.framework__ChunkingLibrary.md) | 2700.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CiderAudioServer.framework/CiderAudioServer`](System__Library__PrivateFrameworks__CiderAudioServer.framework__CiderAudioServer.md) | 64.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CinematicCommunication.framework/CinematicCommunication`](System__Library__PrivateFrameworks__CinematicCommunication.framework__CinematicCommunication.md) | 560.40.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/CinematicFraming.framework/CinematicFraming`](System__Library__PrivateFrameworks__CinematicFraming.framework__CinematicFraming.md) | 764.42.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/CinematicUtil.framework/CinematicUtil`](System__Library__PrivateFrameworks__CinematicUtil.framework__CinematicUtil.md) | 560.40.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/ClarityBoardFoundation.framework/ClarityBoardFoundation`](System__Library__PrivateFrameworks__ClarityBoardFoundation.framework__ClarityBoardFoundation.md) | 170.3.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/ClassKitNotificationUI.framework/ClassKitNotificationUI`](System__Library__PrivateFrameworks__ClassKitNotificationUI.framework__ClassKitNotificationUI.md) | 152.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ClassroomKit.framework/ClassroomKit`](System__Library__PrivateFrameworks__ClassroomKit.framework__ClassroomKit.md) | 148.40.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/ClassroomKit.framework/Frameworks/ClassroomUIKit.framework/ClassroomUIKit`](System__Library__PrivateFrameworks__ClassroomKit.framework__Frameworks__ClassroomUIKit.framework__ClassroomUIKit.md) | 148.40.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/ClipServices.framework/ClipServices`](System__Library__PrivateFrameworks__ClipServices.framework__ClipServices.md) | 1039.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ClipUIServices.framework/ClipUIServices`](System__Library__PrivateFrameworks__ClipUIServices.framework__ClipUIServices.md) | 1039.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ClockAppIntentsSupport.framework/ClockAppIntentsSupport`](System__Library__PrivateFrameworks__ClockAppIntentsSupport.framework__ClockAppIntentsSupport.md) | 308.2.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/ClockComplications.framework/ClockComplications`](System__Library__PrivateFrameworks__ClockComplications.framework__ClockComplications.md) | 2483.561.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ClockFacePostersUI.framework/ClockFacePostersUI`](System__Library__PrivateFrameworks__ClockFacePostersUI.framework__ClockFacePostersUI.md) | 123.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ClockKitUI.framework/ClockKitUI`](System__Library__PrivateFrameworks__ClockKitUI.framework__ClockKitUI.md) | 2483.561.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ClockPoster.framework/ClockPoster`](System__Library__PrivateFrameworks__ClockPoster.framework__ClockPoster.md) | 123.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ClockUIFramework.framework/ClockUIFramework`](System__Library__PrivateFrameworks__ClockUIFramework.framework__ClockUIFramework.md) | 3605.13.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ClothPhysics.framework/ClothPhysics`](System__Library__PrivateFrameworks__ClothPhysics.framework__ClothPhysics.md) | 21.0.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/CloudAsset.framework/CloudAsset`](System__Library__PrivateFrameworks__CloudAsset.framework__CloudAsset.md) | 2720.17.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/CloudAssets.framework/CloudAssets`](System__Library__PrivateFrameworks__CloudAssets.framework__CloudAssets.md) | 2700.112.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CloudAssetsCommons.framework/CloudAssetsCommons`](System__Library__PrivateFrameworks__CloudAssetsCommons.framework__CloudAssetsCommons.md) | 2700.112.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CloudAssetsDaemon.framework/CloudAssetsDaemon`](System__Library__PrivateFrameworks__CloudAssetsDaemon.framework__CloudAssetsDaemon.md) | 2700.112.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CloudDocsUI.framework/CloudDocsUI`](System__Library__PrivateFrameworks__CloudDocsUI.framework__CloudDocsUI.md) | 177.2.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CloudKitCode.framework/CloudKitCode`](System__Library__PrivateFrameworks__CloudKitCode.framework__CloudKitCode.md) | 2720.17.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/CloudKitCodeProtobuf.framework/CloudKitCodeProtobuf`](System__Library__PrivateFrameworks__CloudKitCodeProtobuf.framework__CloudKitCodeProtobuf.md) | 2720.17.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/CloudKitSharingManagement.framework/CloudKitSharingManagement`](System__Library__PrivateFrameworks__CloudKitSharingManagement.framework__CloudKitSharingManagement.md) | 27.125.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/CloudMediaServicesInterfaceKit.framework/CloudMediaServicesInterfaceKit`](System__Library__PrivateFrameworks__CloudMediaServicesInterfaceKit.framework__CloudMediaServicesInterfaceKit.md) | 261.10.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CloudPhotoServices.framework/CloudPhotoServices`](System__Library__PrivateFrameworks__CloudPhotoServices.framework__CloudPhotoServices.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/CloudRecommendation.framework/CloudRecommendation`](System__Library__PrivateFrameworks__CloudRecommendation.framework__CloudRecommendation.md) | 301.24.1.4.0 | light |
| [`/System/Library/PrivateFrameworks/CloudRecommendationUI.framework/CloudRecommendationUI`](System__Library__PrivateFrameworks__CloudRecommendationUI.framework__CloudRecommendationUI.md) | 301.24.1.4.0 | light |
| [`/System/Library/PrivateFrameworks/CloudServices.framework/CloudServices`](System__Library__PrivateFrameworks__CloudServices.framework__CloudServices.md) | 747.40.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/CloudSettings.framework/CloudSettings`](System__Library__PrivateFrameworks__CloudSettings.framework__CloudSettings.md) | 113.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CloudSharing.framework/CloudSharing`](System__Library__PrivateFrameworks__CloudSharing.framework__CloudSharing.md) | 240.1.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/CloudSharingUI.framework/CloudSharingUI`](System__Library__PrivateFrameworks__CloudSharingUI.framework__CloudSharingUI.md) | 240.1.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/CodesignKit.framework/CodesignKit`](System__Library__PrivateFrameworks__CodesignKit.framework__CodesignKit.md) | 16.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CognitiveHealth.framework/CognitiveHealth`](System__Library__PrivateFrameworks__CognitiveHealth.framework__CognitiveHealth.md) | 27.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CollectionViewCore.framework/CollectionViewCore`](System__Library__PrivateFrameworks__CollectionViewCore.framework__CollectionViewCore.md) | 9127.1.13.13.0 | light |
| [`/System/Library/PrivateFrameworks/CombineCocoa.framework/CombineCocoa`](System__Library__PrivateFrameworks__CombineCocoa.framework__CombineCocoa.md) | 3023.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CommandAndControlUI.framework/CommandAndControlUI`](System__Library__PrivateFrameworks__CommandAndControlUI.framework__CommandAndControlUI.md) | 191.2.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/CommonAuth.framework/CommonAuth`](System__Library__PrivateFrameworks__CommonAuth.framework__CommonAuth.md) | 725.40.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/CommunicationDetails.framework/CommunicationDetails`](System__Library__PrivateFrameworks__CommunicationDetails.framework__CommunicationDetails.md) | 1491.200.101.21.5 | light |
| [`/System/Library/PrivateFrameworks/CommunicationSafetySettingsUI.framework/CommunicationSafetySettingsUI`](System__Library__PrivateFrameworks__CommunicationSafetySettingsUI.framework__CommunicationSafetySettingsUI.md) | 2027.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/CommunicationTrust.framework/CommunicationTrust`](System__Library__PrivateFrameworks__CommunicationTrust.framework__CommunicationTrust.md) | 158.200.81.21.9 | light |
| [`/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CommunicationsFilter`](System__Library__PrivateFrameworks__CommunicationsFilter.framework__CommunicationsFilter.md) | 196.200.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI`](System__Library__PrivateFrameworks__CommunicationsSetupUI.framework__CommunicationsSetupUI.md) | 1576.200.51.0.0 | light |
| [`/System/Library/PrivateFrameworks/CompanionCamera.framework/CompanionCamera`](System__Library__PrivateFrameworks__CompanionCamera.framework__CompanionCamera.md) | 2024.200.4.0.0 | full |
| [`/System/Library/PrivateFrameworks/CompanionHealthDaemon.framework/CompanionHealthDaemon`](System__Library__PrivateFrameworks__CompanionHealthDaemon.framework__CompanionHealthDaemon.md) | 2027.1.48.0.0 | light |
| [`/System/Library/PrivateFrameworks/CompanionInferenceCore.framework/CompanionInferenceCore`](System__Library__PrivateFrameworks__CompanionInferenceCore.framework__CompanionInferenceCore.md) | 12.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CompanionServices.framework/CompanionServices`](System__Library__PrivateFrameworks__CompanionServices.framework__CompanionServices.md) | 524.11.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/CompanionSetupKit.framework/CompanionSetupKit`](System__Library__PrivateFrameworks__CompanionSetupKit.framework__CompanionSetupKit.md) | 524.11.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/CompassUI.framework/CompassUI`](System__Library__PrivateFrameworks__CompassUI.framework__CompassUI.md) | 367.31.9.18.102 | light |
| [`/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay`](System__Library__PrivateFrameworks__ComplicationDisplay.framework__ComplicationDisplay.md) | 2483.561.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/ConditionInducer.framework/ConditionInducer`](System__Library__PrivateFrameworks__ConditionInducer.framework__ConditionInducer.md) | 250.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ConfigurationEngineModel.framework/ConfigurationEngineModel`](System__Library__PrivateFrameworks__ConfigurationEngineModel.framework__ConfigurationEngineModel.md) | 267.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ConnectedMode.framework/ConnectedMode`](System__Library__PrivateFrameworks__ConnectedMode.framework__ConnectedMode.md) | 15.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ConstantClasses.framework/ConstantClasses`](System__Library__PrivateFrameworks__ConstantClasses.framework__ConstantClasses.md) | 28.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ContactlessReaderUI.framework/ContactlessReaderUI`](System__Library__PrivateFrameworks__ContactlessReaderUI.framework__ContactlessReaderUI.md) | 151.6.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ContactsAccounts.framework/ContactsAccounts`](System__Library__PrivateFrameworks__ContactsAccounts.framework__ContactsAccounts.md) | 3846.200.91.2.1 | light |
| [`/System/Library/PrivateFrameworks/ContactsAssistantServices.framework/ContactsAssistantServices`](System__Library__PrivateFrameworks__ContactsAssistantServices.framework__ContactsAssistantServices.md) | 29.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ContactsAutocomplete.framework/ContactsAutocomplete`](System__Library__PrivateFrameworks__ContactsAutocomplete.framework__ContactsAutocomplete.md) | 1384.200.41.0.0 | light |
| [`/System/Library/PrivateFrameworks/ContactsDonationFeedback.framework/ContactsDonationFeedback`](System__Library__PrivateFrameworks__ContactsDonationFeedback.framework__ContactsDonationFeedback.md) | 1130.200.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ContactsMetrics.framework/ContactsMetrics`](System__Library__PrivateFrameworks__ContactsMetrics.framework__ContactsMetrics.md) | 28.200.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ContactsPersistence.framework/ContactsPersistence`](System__Library__PrivateFrameworks__ContactsPersistence.framework__ContactsPersistence.md) | 3846.200.91.2.1 | light |
| [`/System/Library/PrivateFrameworks/ContactsWidgetUI.framework/ContactsWidgetUI`](System__Library__PrivateFrameworks__ContactsWidgetUI.framework__ContactsWidgetUI.md) | 148.125.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/ContainerManagerSystem.framework/ContainerManagerSystem`](System__Library__PrivateFrameworks__ContainerManagerSystem.framework__ContainerManagerSystem.md) | 833.40.18.0.1 | light |
| [`/System/Library/PrivateFrameworks/ContainerManagerUser.framework/ContainerManagerUser`](System__Library__PrivateFrameworks__ContainerManagerUser.framework__ContainerManagerUser.md) | 833.40.18.0.1 | light |
| [`/System/Library/PrivateFrameworks/ContextKitCore.framework/ContextKitCore`](System__Library__PrivateFrameworks__ContextKitCore.framework__ContextKitCore.md) | 308.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ContextKitPrediction.framework/ContextKitPrediction`](System__Library__PrivateFrameworks__ContextKitPrediction.framework__ContextKitPrediction.md) | 308.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ContextSync.framework/ContextSync`](System__Library__PrivateFrameworks__ContextSync.framework__ContextSync.md) | 259.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ContextualSuggestionClient.framework/ContextualSuggestionClient`](System__Library__PrivateFrameworks__ContextualSuggestionClient.framework__ContextualSuggestionClient.md) | 678.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ContextualUnderstanding.framework/ContextualUnderstanding`](System__Library__PrivateFrameworks__ContextualUnderstanding.framework__ContextualUnderstanding.md) | 194.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ContinuitySing.framework/ContinuitySing`](System__Library__PrivateFrameworks__ContinuitySing.framework__ContinuitySing.md) | 764.42.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/ContinuousDialogManagerService.framework/ContinuousDialogManagerService`](System__Library__PrivateFrameworks__ContinuousDialogManagerService.framework__ContinuousDialogManagerService.md) | 3605.19.1.11.1 | light |
| [`/System/Library/PrivateFrameworks/ControlCenterServices.framework/ControlCenterServices`](System__Library__PrivateFrameworks__ControlCenterServices.framework__ControlCenterServices.md) | 704.2.4.0.3 | light |
| [`/System/Library/PrivateFrameworks/ConversationalInteraction.framework/ConversationalInteraction`](System__Library__PrivateFrameworks__ConversationalInteraction.framework__ConversationalInteraction.md) | 3600.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CookingData.framework/CookingData`](System__Library__PrivateFrameworks__CookingData.framework__CookingData.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/Coordination.framework/Coordination`](System__Library__PrivateFrameworks__Coordination.framework__Coordination.md) | 249.10.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoordinationCore.framework/CoordinationCore`](System__Library__PrivateFrameworks__CoordinationCore.framework__CoordinationCore.md) | 249.10.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreALD.framework/CoreALD`](System__Library__PrivateFrameworks__CoreALD.framework__CoreALD.md) | 0.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreAUC.framework/CoreAUC`](System__Library__PrivateFrameworks__CoreAUC.framework__CoreAUC.md) | 638.12.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreAccessoriesFeatures.framework/CoreAccessoriesFeatures`](System__Library__PrivateFrameworks__CoreAccessoriesFeatures.framework__CoreAccessoriesFeatures.md) | 1219.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreAppleCVA.framework/CoreAppleCVA`](System__Library__PrivateFrameworks__CoreAppleCVA.framework__CoreAppleCVA.md) | 4.4.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreAudioOrchestration.framework/CoreAudioOrchestration`](System__Library__PrivateFrameworks__CoreAudioOrchestration.framework__CoreAudioOrchestration.md) | 95.202.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/CoreBluetoothUI`](System__Library__PrivateFrameworks__CoreBluetoothUI.framework__CoreBluetoothUI.md) | 2701.7.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`](System__Library__PrivateFrameworks__CoreCDPInternal.framework__CoreCDPInternal.md) | 448.125.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI`](System__Library__PrivateFrameworks__CoreCDPUI.framework__CoreCDPUI.md) | 448.125.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreCDPUIInternal.framework/CoreCDPUIInternal`](System__Library__PrivateFrameworks__CoreCDPUIInternal.framework__CoreCDPUIInternal.md) | 448.125.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreCapture.framework/CoreCapture`](System__Library__PrivateFrameworks__CoreCapture.framework__CoreCapture.md) | 1355.45.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreCaptureControl.framework/CoreCaptureControl`](System__Library__PrivateFrameworks__CoreCaptureControl.framework__CoreCaptureControl.md) | 1355.45.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon`](System__Library__PrivateFrameworks__CoreCaptureDaemon.framework__CoreCaptureDaemon.md) | 1355.45.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreDAV.framework/CoreDAV`](System__Library__PrivateFrameworks__CoreDAV.framework__CoreDAV.md) | 1248.2.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreDeviceSelection.framework/CoreDeviceSelection`](System__Library__PrivateFrameworks__CoreDeviceSelection.framework__CoreDeviceSelection.md) | 3605.25.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreDuetDaemonProtocol.framework/CoreDuetDaemonProtocol`](System__Library__PrivateFrameworks__CoreDuetDaemonProtocol.framework__CoreDuetDaemonProtocol.md) | 1977.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreDuetSync.framework/CoreDuetSync`](System__Library__PrivateFrameworks__CoreDuetSync.framework__CoreDuetSync.md) | 1977.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreFollowUpUI.framework/CoreFollowUpUI`](System__Library__PrivateFrameworks__CoreFollowUpUI.framework__CoreFollowUpUI.md) | 2027.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreGEM.framework/CoreGEM.dylib`](System__Library__PrivateFrameworks__CoreGEM.framework__CoreGEM.dylib.md) | 36.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreGPSTest.framework/CoreGPSTest.dylib`](System__Library__PrivateFrameworks__CoreGPSTest.framework__CoreGPSTest.dylib.md) | 367.0.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/CoreHID.framework/CoreHID`](System__Library__PrivateFrameworks__CoreHID.framework__CoreHID.md) | 2360.40.13.0.1 | full |
| [`/System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred`](System__Library__PrivateFrameworks__CoreIDCred.framework__CoreIDCred.md) | 9.108.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreIDCredBuilder.framework/CoreIDCredBuilder`](System__Library__PrivateFrameworks__CoreIDCredBuilder.framework__CoreIDCredBuilder.md) | 9.108.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreIDV.framework/CoreIDV`](System__Library__PrivateFrameworks__CoreIDV.framework__CoreIDV.md) | 9.108.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreIDVDaemonSupport.framework/CoreIDVDaemonSupport`](System__Library__PrivateFrameworks__CoreIDVDaemonSupport.framework__CoreIDVDaemonSupport.md) | 9.108.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreIDVPAD.framework/CoreIDVPAD`](System__Library__PrivateFrameworks__CoreIDVPAD.framework__CoreIDVPAD.md) | 5.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreIDVRGBLiveness.framework/CoreIDVRGBLiveness`](System__Library__PrivateFrameworks__CoreIDVRGBLiveness.framework__CoreIDVRGBLiveness.md) | 9.108.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreIDVUI.framework/CoreIDVUI`](System__Library__PrivateFrameworks__CoreIDVUI.framework__CoreIDVUI.md) | 9.108.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreIK.framework/CoreIK`](System__Library__PrivateFrameworks__CoreIK.framework__CoreIK.md) | 271.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreIMS.framework/CoreIMS`](System__Library__PrivateFrameworks__CoreIMS.framework__CoreIMS.md) | 124.40.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreIndoor.framework/CoreIndoor`](System__Library__PrivateFrameworks__CoreIndoor.framework__CoreIndoor.md) | 803.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) | 170.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/CoreLocationReplay.framework/CoreLocationReplay`](System__Library__PrivateFrameworks__CoreLocationReplay.framework__CoreLocationReplay.md) | 3187.0.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/CoreLocationTiles.framework/CoreLocationTiles`](System__Library__PrivateFrameworks__CoreLocationTiles.framework__CoreLocationTiles.md) | 3187.0.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/CoreMLOdie.framework/CoreMLOdie`](System__Library__PrivateFrameworks__CoreMLOdie.framework__CoreMLOdie.md) | 3605.3.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/CoreMaterial3D.framework/CoreMaterial3D`](System__Library__PrivateFrameworks__CoreMaterial3D.framework__CoreMaterial3D.md) | 22.40.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreMediaStream.framework/CoreMediaStream`](System__Library__PrivateFrameworks__CoreMediaStream.framework__CoreMediaStream.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreMotionAlgorithms.framework/CoreMotionAlgorithms`](System__Library__PrivateFrameworks__CoreMotionAlgorithms.framework__CoreMotionAlgorithms.md) | 3187.0.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/CoreMotionFDNML.framework/CoreMotionFDNML`](System__Library__PrivateFrameworks__CoreMotionFDNML.framework__CoreMotionFDNML.md) | 28.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/CoreMotionModels.framework/CoreMotionModels`](System__Library__PrivateFrameworks__CoreMotionModels.framework__CoreMotionModels.md) | 29.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/CoreNameParser.framework/CoreNameParser`](System__Library__PrivateFrameworks__CoreNameParser.framework__CoreNameParser.md) | 15.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreOC.framework/CoreOC`](System__Library__PrivateFrameworks__CoreOC.framework__CoreOC.md) | 11.3.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreOCModules.framework/CoreOCModules`](System__Library__PrivateFrameworks__CoreOCModules.framework__CoreOCModules.md) | 11.3.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreODI.framework/CoreODI`](System__Library__PrivateFrameworks__CoreODI.framework__CoreODI.md) | 27.2.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreOptimization.framework/CoreOptimization`](System__Library__PrivateFrameworks__CoreOptimization.framework__CoreOptimization.md) | 117.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CorePDF.framework/CorePDF`](System__Library__PrivateFrameworks__CorePDF.framework__CorePDF.md) | 556.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers`](System__Library__PrivateFrameworks__CorePhoneNumbers.framework__CorePhoneNumbers.md) | 158.200.81.21.9 | light |
| [`/System/Library/PrivateFrameworks/CorePhotogrammetry.framework/CorePhotogrammetry`](System__Library__PrivateFrameworks__CorePhotogrammetry.framework__CorePhotogrammetry.md) | 3.9.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/CorePrediction.framework/CorePrediction`](System__Library__PrivateFrameworks__CorePrediction.framework__CorePrediction.md) | 117.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CorePrescription.framework/CorePrescription`](System__Library__PrivateFrameworks__CorePrescription.framework__CorePrescription.md) | 230.40.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreRC.framework/CoreRC`](System__Library__PrivateFrameworks__CoreRC.framework__CoreRC.md) | 277.40.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreRE3DGSFoundation.framework/CoreRE3DGSFoundation`](System__Library__PrivateFrameworks__CoreRE3DGSFoundation.framework__CoreRE3DGSFoundation.md) | 20.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreRealityIO.framework/CoreRealityIO`](System__Library__PrivateFrameworks__CoreRealityIO.framework__CoreRealityIO.md) | 235.40.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreRecognition.framework/CoreRecognition`](System__Library__PrivateFrameworks__CoreRecognition.framework__CoreRecognition.md) | 446.15.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit`](System__Library__PrivateFrameworks__CoreRepairKit.framework__CoreRepairKit.md) | 1307.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreRepairLite.framework/CoreRepairLite`](System__Library__PrivateFrameworks__CoreRepairLite.framework__CoreRepairLite.md) | 1307.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI`](System__Library__PrivateFrameworks__CoreRepairUI.framework__CoreRepairUI.md) | 1307.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreReporting.framework/CoreReporting`](System__Library__PrivateFrameworks__CoreReporting.framework__CoreReporting.md) | 13.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreSDB.framework/CoreSDB`](System__Library__PrivateFrameworks__CoreSDB.framework__CoreSDB.md) | 211.200.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreServicesUI.framework/CoreServicesUI`](System__Library__PrivateFrameworks__CoreServicesUI.framework__CoreServicesUI.md) | 469.1.12.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreSpeechDataAnalytics.framework/CoreSpeechDataAnalytics`](System__Library__PrivateFrameworks__CoreSpeechDataAnalytics.framework__CoreSpeechDataAnalytics.md) | 3605.32.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreSpeechExclave.framework/CoreSpeechExclave`](System__Library__PrivateFrameworks__CoreSpeechExclave.framework__CoreSpeechExclave.md) | 3605.32.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/CoreSpeechUtils.framework/CoreSpeechUtils`](System__Library__PrivateFrameworks__CoreSpeechUtils.framework__CoreSpeechUtils.md) | 3605.32.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreSuggestionsML.framework/CoreSuggestionsML`](System__Library__PrivateFrameworks__CoreSuggestionsML.framework__CoreSuggestionsML.md) | 1354.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreThemeDefinition.framework/CoreThemeDefinition`](System__Library__PrivateFrameworks__CoreThemeDefinition.framework__CoreThemeDefinition.md) | 664.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreThread.framework/CoreThread`](System__Library__PrivateFrameworks__CoreThread.framework__CoreThread.md) | 446.0.4.0.0 | full |
| [`/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio`](System__Library__PrivateFrameworks__CoreThreadRadio.framework__CoreThreadRadio.md) | 446.0.4.0.0 | full |
| [`/System/Library/PrivateFrameworks/CoreTransparency.framework/CoreTransparency`](System__Library__PrivateFrameworks__CoreTransparency.framework__CoreTransparency.md) | 1766.40.58.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP`](System__Library__PrivateFrameworks__CoreUARP.framework__CoreUARP.md) | 1587.40.33.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreUtilsExtras.framework/CoreUtilsExtras`](System__Library__PrivateFrameworks__CoreUtilsExtras.framework__CoreUtilsExtras.md) | 910.31.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreUtilsShims.framework/CoreUtilsShims`](System__Library__PrivateFrameworks__CoreUtilsShims.framework__CoreUtilsShims.md) | 910.31.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreUtilsUI.framework/CoreUtilsUI`](System__Library__PrivateFrameworks__CoreUtilsUI.framework__CoreUtilsUI.md) | 910.31.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/Cornobble.framework/Cornobble`](System__Library__PrivateFrameworks__Cornobble.framework__Cornobble.md) | 56.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CosmeticAssessment.framework/CosmeticAssessment`](System__Library__PrivateFrameworks__CosmeticAssessment.framework__CosmeticAssessment.md) | 195.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CrisisResources.framework/CrisisResources`](System__Library__PrivateFrameworks__CrisisResources.framework__CrisisResources.md) | 3605.11.1.11.1 | light |
| [`/System/Library/PrivateFrameworks/CryptoKitCBridging.framework/CryptoKitCBridging`](System__Library__PrivateFrameworks__CryptoKitCBridging.framework__CryptoKitCBridging.md) | 383.40.14.0.0 | light |
| [`/System/Library/PrivateFrameworks/DAAPKit.framework/DAAPKit`](System__Library__PrivateFrameworks__DAAPKit.framework__DAAPKit.md) | 4026.200.13.0.0 | light |
| [`/System/Library/PrivateFrameworks/DAEASOAuthFramework.framework/DAEASOAuthFramework`](System__Library__PrivateFrameworks__DAEASOAuthFramework.framework__DAEASOAuthFramework.md) | 2079.200.41.0.0 | light |
| [`/System/Library/PrivateFrameworks/DANECPWrapper.framework/DANECPWrapper`](System__Library__PrivateFrameworks__DANECPWrapper.framework__DANECPWrapper.md) | 2701.6.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/DASDaemon.framework/DASDaemon`](System__Library__PrivateFrameworks__DASDaemon.framework__DASDaemon.md) | 2467.52.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/DASDelegate.framework/DASDelegate`](System__Library__PrivateFrameworks__DASDelegate.framework__DASDelegate.md) | 2467.52.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/DEPClientLibrary.framework/DEPClientLibrary`](System__Library__PrivateFrameworks__DEPClientLibrary.framework__DEPClientLibrary.md) | 113.52.1.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend23.dylib`](usr__lib__objc__libobjcMsgSend23.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreSpotlightAgenticCore.framework/CoreSpotlightAgenticCore`](System__Library__PrivateFrameworks__CoreSpotlightAgenticCore.framework__CoreSpotlightAgenticCore.md) | 2465.1.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/Cosmo.framework/Cosmo`](System__Library__PrivateFrameworks__Cosmo.framework__Cosmo.md) | 5.40.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CryptexKit.framework/CryptexKit`](System__Library__PrivateFrameworks__CryptexKit.framework__CryptexKit.md) | 761.40.23.0.0 | light |
| [`/System/Library/PrivateFrameworks/CryptexServer.framework/CryptexServer`](System__Library__PrivateFrameworks__CryptexServer.framework__CryptexServer.md) | 761.40.23.0.0 | light |
| [`/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary`](System__Library__PrivateFrameworks__DMCEnrollmentLibrary.framework__DMCEnrollmentLibrary.md) | 113.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider`](System__Library__PrivateFrameworks__DMCEnrollmentProvider.framework__DMCEnrollmentProvider.md) | 113.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/DMCTools.framework/DMCTools`](System__Library__PrivateFrameworks__DMCTools.framework__DMCTools.md) | 113.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/DMCToolsUIUtilities.framework/DMCToolsUIUtilities`](System__Library__PrivateFrameworks__DMCToolsUIUtilities.framework__DMCToolsUIUtilities.md) | 113.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/DRMFoundation.framework/DRMFoundation`](System__Library__PrivateFrameworks__DRMFoundation.framework__DRMFoundation.md) | 288.40.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/DSContinuityPairing.framework/DSContinuityPairing`](System__Library__PrivateFrameworks__DSContinuityPairing.framework__DSContinuityPairing.md) | 653.0.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/DSRemotePairing.framework/DSRemotePairing`](System__Library__PrivateFrameworks__DSRemotePairing.framework__DSRemotePairing.md) | 653.0.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/DTXConnectionServices.framework/DTXConnectionServices`](System__Library__PrivateFrameworks__DTXConnectionServices.framework__DTXConnectionServices.md) | 64578.209.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DVTInstrumentsFoundation`](System__Library__PrivateFrameworks__DVTInstrumentsFoundation.framework__DVTInstrumentsFoundation.md) | 64578.209.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/DVTInstrumentsUtilities.framework/DVTInstrumentsUtilities`](System__Library__PrivateFrameworks__DVTInstrumentsUtilities.framework__DVTInstrumentsUtilities.md) | 64578.209.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/DarwinDirectory.framework/DarwinDirectory`](System__Library__PrivateFrameworks__DarwinDirectory.framework__DarwinDirectory.md) | 129.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/DarwinDirectoryInternal.framework/DarwinDirectoryInternal`](System__Library__PrivateFrameworks__DarwinDirectoryInternal.framework__DarwinDirectoryInternal.md) | 129.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/DarwinDirectoryQuery.framework/DarwinDirectoryQuery`](System__Library__PrivateFrameworks__DarwinDirectoryQuery.framework__DarwinDirectoryQuery.md) | 129.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/DashBoard.framework/DashBoard`](System__Library__PrivateFrameworks__DashBoard.framework__DashBoard.md) | 591.6.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/DataAccess.framework/DataAccess`](System__Library__PrivateFrameworks__DataAccess.framework__DataAccess.md) | 2708.2.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACalDAV.framework/DACalDAV`](System__Library__PrivateFrameworks__DataAccess.framework__Frameworks__DACalDAV.framework__DACalDAV.md) | 2708.2.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACardDAV.framework/DACardDAV`](System__Library__PrivateFrameworks__DataAccess.framework__Frameworks__DACardDAV.framework__DACardDAV.md) | 2708.2.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACoreDAVGlue.framework/DACoreDAVGlue`](System__Library__PrivateFrameworks__DataAccess.framework__Frameworks__DACoreDAVGlue.framework__DACoreDAVGlue.md) | 2708.2.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DADaemonSupport.framework/DADaemonSupport`](System__Library__PrivateFrameworks__DataAccess.framework__Frameworks__DADaemonSupport.framework__DADaemonSupport.md) | 2708.2.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DAIMAPNotes.framework/DAIMAPNotes`](System__Library__PrivateFrameworks__DataAccess.framework__Frameworks__DAIMAPNotes.framework__DAIMAPNotes.md) | 2708.2.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DALDAP.framework/DALDAP`](System__Library__PrivateFrameworks__DataAccess.framework__Frameworks__DALDAP.framework__DALDAP.md) | 2708.2.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DASubCal.framework/DASubCal`](System__Library__PrivateFrameworks__DataAccess.framework__Frameworks__DASubCal.framework__DASubCal.md) | 2708.2.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/DataAccessUI.framework/DataAccessUI`](System__Library__PrivateFrameworks__DataAccessUI.framework__DataAccessUI.md) | 2708.2.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/DataCollector.framework/DataCollector`](System__Library__PrivateFrameworks__DataCollector.framework__DataCollector.md) | 3605.6.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/DataCollectorLibrary.framework/DataCollectorLibrary`](System__Library__PrivateFrameworks__DataCollectorLibrary.framework__DataCollectorLibrary.md) | 3605.6.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/DataDetectorsCore.framework/PlugIns/PhoneNumbers.plugin/PhoneNumbers`](System__Library__PrivateFrameworks__DataDetectorsCore.framework__PlugIns__PhoneNumbers.plugin__PhoneNumbers.md) | 852.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DataDetectorsNaturalLanguage.framework/DataDetectorsNaturalLanguage`](System__Library__PrivateFrameworks__DataDetectorsNaturalLanguage.framework__DataDetectorsNaturalLanguage.md) | 175.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DataDetectorsUI.framework/DataDetectorsUI`](System__Library__PrivateFrameworks__DataDetectorsUI.framework__DataDetectorsUI.md) | 616.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DataFlow.framework/DataFlow`](System__Library__PrivateFrameworks__DataFlow.framework__DataFlow.md) | 2027.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/DataMigration.framework/DataMigration`](System__Library__PrivateFrameworks__DataMigration.framework__DataMigration.md) | 2858.1.5.100.0 | light |
| [`/System/Library/PrivateFrameworks/DataRelay.framework/DataRelay`](System__Library__PrivateFrameworks__DataRelay.framework__DataRelay.md) | 41.7.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DataRelay_Private.framework/DataRelay_Private`](System__Library__PrivateFrameworks__DataRelay_Private.framework__DataRelay_Private.md) | 41.7.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DateAndTimeSupport.framework/DateAndTimeSupport`](System__Library__PrivateFrameworks__DateAndTimeSupport.framework__DateAndTimeSupport.md) | 2027.1.1.101.0 | light |
| [`/System/Library/PrivateFrameworks/DeepThought.framework/DeepThought`](System__Library__PrivateFrameworks__DeepThought.framework__DeepThought.md) | 6.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/DeepVideoProcessingCore.framework/DeepVideoProcessingCore`](System__Library__PrivateFrameworks__DeepVideoProcessingCore.framework__DeepVideoProcessingCore.md) | 3.7.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DefaultAppsSettings.framework/DefaultAppsSettings`](System__Library__PrivateFrameworks__DefaultAppsSettings.framework__DefaultAppsSettings.md) | 2027.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/DefaultAppsSettingsUI.framework/DefaultAppsSettingsUI`](System__Library__PrivateFrameworks__DefaultAppsSettingsUI.framework__DefaultAppsSettingsUI.md) | 2027.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/Dendrite.framework/Dendrite`](System__Library__PrivateFrameworks__Dendrite.framework__Dendrite.md) | 8.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DepthCore.framework/DepthCore`](System__Library__PrivateFrameworks__DepthCore.framework__DepthCore.md) | 2027.1.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/DesktopServicesUI.framework/DesktopServicesUI`](System__Library__PrivateFrameworks__DesktopServicesUI.framework__DesktopServicesUI.md) | 1857.1.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess`](System__Library__PrivateFrameworks__DeviceAccess.framework__DeviceAccess.md) | 2701.6.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/DeviceCheckInternal`](System__Library__PrivateFrameworks__DeviceCheckInternal.framework__DeviceCheckInternal.md) | 158.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DeviceDiscoveryUICore.framework/DeviceDiscoveryUICore`](System__Library__PrivateFrameworks__DeviceDiscoveryUICore.framework__DeviceDiscoveryUICore.md) | 2131.21.31.21.8 | light |
| [`/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/DeviceExpertIntents`](System__Library__PrivateFrameworks__DeviceExpertIntents.framework__DeviceExpertIntents.md) | 3605.6.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/DeviceExpertUI.framework/DeviceExpertUI`](System__Library__PrivateFrameworks__DeviceExpertUI.framework__DeviceExpertUI.md) | 3605.6.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/DeviceManagementTools.framework/DeviceManagementTools`](System__Library__PrivateFrameworks__DeviceManagementTools.framework__DeviceManagementTools.md) | 87.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DeviceOMatic.framework/DeviceOMatic`](System__Library__PrivateFrameworks__DeviceOMatic.framework__DeviceOMatic.md) | 66.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DevicePresence.framework/DevicePresence`](System__Library__PrivateFrameworks__DevicePresence.framework__DevicePresence.md) | 30.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DeviceRecovery.framework/DeviceRecovery`](System__Library__PrivateFrameworks__DeviceRecovery.framework__DeviceRecovery.md) | 150.40.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/DeviceRegulatoryInfo.framework/DeviceRegulatoryInfo`](System__Library__PrivateFrameworks__DeviceRegulatoryInfo.framework__DeviceRegulatoryInfo.md) | 2027.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/DeviceSelectionEmergencyFlow.framework/DeviceSelectionEmergencyFlow`](System__Library__PrivateFrameworks__DeviceSelectionEmergencyFlow.framework__DeviceSelectionEmergencyFlow.md) | 3605.25.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/DeviceSharingEnrollmentServices.framework/DeviceSharingEnrollmentServices`](System__Library__PrivateFrameworks__DeviceSharingEnrollmentServices.framework__DeviceSharingEnrollmentServices.md) | 40.0.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/DeviceSharingEnterpriseServices.framework/DeviceSharingEnterpriseServices`](System__Library__PrivateFrameworks__DeviceSharingEnterpriseServices.framework__DeviceSharingEnterpriseServices.md) | 40.0.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/DeviceSharingServices.framework/DeviceSharingServices`](System__Library__PrivateFrameworks__DeviceSharingServices.framework__DeviceSharingServices.md) | 40.0.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/DeviceSharingServicesCore.framework/DeviceSharingServicesCore`](System__Library__PrivateFrameworks__DeviceSharingServicesCore.framework__DeviceSharingServicesCore.md) | 40.0.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/DeviceSharingUI.framework/DeviceSharingUI`](System__Library__PrivateFrameworks__DeviceSharingUI.framework__DeviceSharingUI.md) | 40.0.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/DeviceToDeviceManager.framework/DeviceToDeviceManager`](System__Library__PrivateFrameworks__DeviceToDeviceManager.framework__DeviceToDeviceManager.md) | 40.2.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DeviceTreeKit.framework/DeviceTreeKit`](System__Library__PrivateFrameworks__DeviceTreeKit.framework__DeviceTreeKit.md) | 509.40.11.0.0 | light |
| [`/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions`](System__Library__PrivateFrameworks__DiagnosticExtensions.framework__DiagnosticExtensions.md) | 151.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/DiagnosticExtensionsDaemon`](System__Library__PrivateFrameworks__DiagnosticExtensionsDaemon.framework__DiagnosticExtensionsDaemon.md) | 225.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DiagnosticExtensionsKit.framework/DiagnosticExtensionsKit`](System__Library__PrivateFrameworks__DiagnosticExtensionsKit.framework__DiagnosticExtensionsKit.md) | 151.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DiagnosticLogCollection.framework/DiagnosticLogCollection`](System__Library__PrivateFrameworks__DiagnosticLogCollection.framework__DiagnosticLogCollection.md) | 1138.200.21.0.0 | light |
| [`/System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest`](System__Library__PrivateFrameworks__DiagnosticRequest.framework__DiagnosticRequest.md) | 469.40.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/DiagnosticRequestService.framework/DiagnosticRequestService`](System__Library__PrivateFrameworks__DiagnosticRequestService.framework__DiagnosticRequestService.md) | 469.40.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/DiagnosticsCheckup.framework/DiagnosticsCheckup`](System__Library__PrivateFrameworks__DiagnosticsCheckup.framework__DiagnosticsCheckup.md) | 1374.42.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit`](System__Library__PrivateFrameworks__DiagnosticsKit.framework__DiagnosticsKit.md) | 104.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DiagnosticsSessionAvailability.framework/DiagnosticsSessionAvailability`](System__Library__PrivateFrameworks__DiagnosticsSessionAvailability.framework__DiagnosticsSessionAvailability.md) | 1374.42.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport`](System__Library__PrivateFrameworks__DiagnosticsSupport.framework__DiagnosticsSupport.md) | 1374.42.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/DictionaryUI.framework/DictionaryUI`](System__Library__PrivateFrameworks__DictionaryUI.framework__DictionaryUI.md) | 54.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`](System__Library__PrivateFrameworks__DigitalSeparation.framework__DigitalSeparation.md) | 653.0.10.0.0 | full |
| [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) | 653.0.10.0.0 | full |
| [`/System/Library/PrivateFrameworks/DigitalTouchShared.framework/DigitalTouchShared`](System__Library__PrivateFrameworks__DigitalTouchShared.framework__DigitalTouchShared.md) | 583.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DirectResource.framework/DirectResource`](System__Library__PrivateFrameworks__DirectResource.framework__DirectResource.md) | 47.40.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/Disembark.framework/Disembark`](System__Library__PrivateFrameworks__Disembark.framework__Disembark.md) | 285.1.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/DisembarkUI.framework/DisembarkUI`](System__Library__PrivateFrameworks__DisembarkUI.framework__DisembarkUI.md) | 285.1.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/DiskArbitration.framework/DiskArbitration`](System__Library__PrivateFrameworks__DiskArbitration.framework__DiskArbitration.md) | 597.40.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/DiskImageKit.framework/DiskImageKit`](System__Library__PrivateFrameworks__DiskImageKit.framework__DiskImageKit.md) | 598.40.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/DiskImages.framework/DiskImages`](System__Library__PrivateFrameworks__DiskImages.framework__DiskImages.md) | 710.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2`](System__Library__PrivateFrameworks__DiskImages2.framework__DiskImages2.md) | 598.40.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/DiskSpaceDiagnostics.framework/DiskSpaceDiagnostics`](System__Library__PrivateFrameworks__DiskSpaceDiagnostics.framework__DiskSpaceDiagnostics.md) | 1023.40.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/DistributedEvaluation.framework/DistributedEvaluation`](System__Library__PrivateFrameworks__DistributedEvaluation.framework__DistributedEvaluation.md) | 113.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DistributedSensing.framework/DistributedSensing`](System__Library__PrivateFrameworks__DistributedSensing.framework__DistributedSensing.md) | 2.4.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DistributedTimers.framework/DistributedTimers`](System__Library__PrivateFrameworks__DistributedTimers.framework__DistributedTimers.md) | 524.11.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/DistributedTimersDaemon.framework/DistributedTimersDaemon`](System__Library__PrivateFrameworks__DistributedTimersDaemon.framework__DistributedTimersDaemon.md) | 524.11.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/DoNotDisturbKit.framework/DoNotDisturbKit`](System__Library__PrivateFrameworks__DoNotDisturbKit.framework__DoNotDisturbKit.md) | 511.2.7.0.1 | light |
| [`/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/DoNotDisturbServer`](System__Library__PrivateFrameworks__DoNotDisturbServer.framework__DoNotDisturbServer.md) | 511.2.7.0.1 | light |
| [`/System/Library/PrivateFrameworks/DockKitCore.framework/DockKitCore`](System__Library__PrivateFrameworks__DockKitCore.framework__DockKitCore.md) | 432.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DockKitMapping.framework/DockKitMapping`](System__Library__PrivateFrameworks__DockKitMapping.framework__DockKitMapping.md) | 432.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DockKitPerception.framework/DockKitPerception`](System__Library__PrivateFrameworks__DockKitPerception.framework__DockKitPerception.md) | 432.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) | 211.40.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/DocumentManager.framework/DocumentManager`](System__Library__PrivateFrameworks__DocumentManager.framework__DocumentManager.md) | 403.1.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/DocumentManagerCore.framework/DocumentManagerCore`](System__Library__PrivateFrameworks__DocumentManagerCore.framework__DocumentManagerCore.md) | 403.1.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/DocumentManagerExecutables.framework/DocumentManagerExecutables`](System__Library__PrivateFrameworks__DocumentManagerExecutables.framework__DocumentManagerExecutables.md) | 403.1.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/DocumentManagerUICore`](System__Library__PrivateFrameworks__DocumentManagerUICore.framework__DocumentManagerUICore.md) | 403.1.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/DocumentUnderstanding`](System__Library__PrivateFrameworks__DocumentUnderstanding.framework__DocumentUnderstanding.md) | 192.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DocumentUnderstandingClient.framework/DocumentUnderstandingClient`](System__Library__PrivateFrameworks__DocumentUnderstandingClient.framework__DocumentUnderstandingClient.md) | 192.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/Dormancy.framework/Dormancy`](System__Library__PrivateFrameworks__Dormancy.framework__Dormancy.md) | 27.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/DormancyCore.framework/DormancyCore`](System__Library__PrivateFrameworks__DormancyCore.framework__DormancyCore.md) | 27.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/DoubleAgent.framework/DoubleAgent`](System__Library__PrivateFrameworks__DoubleAgent.framework__DoubleAgent.md) | 46.40.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/DownloadAssertions.framework/DownloadAssertions`](System__Library__PrivateFrameworks__DownloadAssertions.framework__DownloadAssertions.md) | 4.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DownloadObtainer.framework/DownloadObtainer`](System__Library__PrivateFrameworks__DownloadObtainer.framework__DownloadObtainer.md) | 4.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DragUI.framework/DragUI`](System__Library__PrivateFrameworks__DragUI.framework__DragUI.md) | 9127.1.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/DrawingBoard.framework/DrawingBoard`](System__Library__PrivateFrameworks__DrawingBoard.framework__DrawingBoard.md) | 38.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/DrawingKit.framework/DrawingKit`](System__Library__PrivateFrameworks__DrawingKit.framework__DrawingKit.md) | 584.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/DropIn.framework/DropIn`](System__Library__PrivateFrameworks__DropIn.framework__DropIn.md) | 169.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DropInCore.framework/DropInCore`](System__Library__PrivateFrameworks__DropInCore.framework__DropInCore.md) | 169.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/DropletUI.framework/DropletUI`](System__Library__PrivateFrameworks__DropletUI.framework__DropletUI.md) | 104.100.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/EAFirmwareUpdater.framework/EAFirmwareUpdater`](System__Library__PrivateFrameworks__EAFirmwareUpdater.framework__EAFirmwareUpdater.md) | 1587.40.33.0.0 | light |
| [`/System/Library/PrivateFrameworks/EAP8021X.framework/EAP8021X`](System__Library__PrivateFrameworks__EAP8021X.framework__EAP8021X.md) | 389.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/EDPSecurity.framework/EDPSecurity`](System__Library__PrivateFrameworks__EDPSecurity.framework__EDPSecurity.md) | 18.0.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/EXDisplayPipe.framework/EXDisplayPipe`](System__Library__PrivateFrameworks__EXDisplayPipe.framework__EXDisplayPipe.md) | 9.2.10.5.0 | full |
| [`/System/Library/PrivateFrameworks/EXSurface.framework/EXSurface`](System__Library__PrivateFrameworks__EXSurface.framework__EXSurface.md) | 16.0.15.0.0 | light |
| [`/System/Library/PrivateFrameworks/EasyConfig.framework/EasyConfig`](System__Library__PrivateFrameworks__EasyConfig.framework__EasyConfig.md) | 910.31.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/EchoRelay.framework/EchoRelay`](System__Library__PrivateFrameworks__EchoRelay.framework__EchoRelay.md) | 99.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/EcosystemAnalytics`](System__Library__PrivateFrameworks__EcosystemAnalytics.framework__EcosystemAnalytics.md) | 39.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/EdgeLight.framework/EdgeLight`](System__Library__PrivateFrameworks__EdgeLight.framework__EdgeLight.md) | 560.40.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/EditScript.framework/EditScript`](System__Library__PrivateFrameworks__EditScript.framework__EditScript.md) | 4.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ElementRegistry.framework/ElementRegistry`](System__Library__PrivateFrameworks__ElementRegistry.framework__ElementRegistry.md) | 18.1.12.0.0 | light |
| [`/System/Library/PrivateFrameworks/ElementRegistryClient.framework/ElementRegistryClient`](System__Library__PrivateFrameworks__ElementRegistryClient.framework__ElementRegistryClient.md) | 18.1.12.0.0 | light |
| [`/System/Library/PrivateFrameworks/ElementRegistryFoundation.framework/ElementRegistryFoundation`](System__Library__PrivateFrameworks__ElementRegistryFoundation.framework__ElementRegistryFoundation.md) | 18.1.12.0.0 | light |
| [`/System/Library/PrivateFrameworks/EmailAddressing.framework/EmailAddressing`](System__Library__PrivateFrameworks__EmailAddressing.framework__EmailAddressing.md) | 3901.200.71.21.4 | light |
| [`/System/Library/PrivateFrameworks/EmbeddedDataReset.framework/EmbeddedDataReset`](System__Library__PrivateFrameworks__EmbeddedDataReset.framework__EmbeddedDataReset.md) | 2027.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/EmbeddingCore.framework/EmbeddingCore`](System__Library__PrivateFrameworks__EmbeddingCore.framework__EmbeddingCore.md) | 460.14.1.2.0 | light |
| [`/System/Library/PrivateFrameworks/EmbeddingService.framework/EmbeddingService`](System__Library__PrivateFrameworks__EmbeddingService.framework__EmbeddingService.md) | 3605.8.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/EmergencyAlerts.framework/EmergencyAlerts`](System__Library__PrivateFrameworks__EmergencyAlerts.framework__EmergencyAlerts.md) | 275.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/EmojiPosterFramework.framework/EmojiPosterFramework`](System__Library__PrivateFrameworks__EmojiPosterFramework.framework__EmojiPosterFramework.md) | 71.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/EncoreXPCService.framework/EncoreXPCService`](System__Library__PrivateFrameworks__EncoreXPCService.framework__EncoreXPCService.md) | 3605.22.1.11.1 | light |
| [`/System/Library/PrivateFrameworks/Engram.framework/Engram`](System__Library__PrivateFrameworks__Engram.framework__Engram.md) | 1138.200.21.0.0 | light |
| [`/System/Library/PrivateFrameworks/EnhancedLinkSecurityStore.framework/EnhancedLinkSecurityStore`](System__Library__PrivateFrameworks__EnhancedLinkSecurityStore.framework__EnhancedLinkSecurityStore.md) | 1491.200.101.21.5 | light |
| [`/System/Library/PrivateFrameworks/EnhancedLogging.framework/EnhancedLogging`](System__Library__PrivateFrameworks__EnhancedLogging.framework__EnhancedLogging.md) | 277.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/EnhancedLoggingState.framework/EnhancedLoggingState`](System__Library__PrivateFrameworks__EnhancedLoggingState.framework__EnhancedLoggingState.md) | 107.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/EntityService.framework/EntityService`](System__Library__PrivateFrameworks__EntityService.framework__EntityService.md) | 3605.22.501.11.0 | light |
| [`/System/Library/PrivateFrameworks/EventKitSyncServices.framework/EventKitSyncServices`](System__Library__PrivateFrameworks__EventKitSyncServices.framework__EventKitSyncServices.md) | 432.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/EventKitTCCUI.framework/EventKitTCCUI`](System__Library__PrivateFrameworks__EventKitTCCUI.framework__EventKitTCCUI.md) | 415.2.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/EventKitUICore.framework/EventKitUICore`](System__Library__PrivateFrameworks__EventKitUICore.framework__EventKitUICore.md) | 1573.2.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/EventMetaDataExtractor.framework/EventMetaDataExtractor`](System__Library__PrivateFrameworks__EventMetaDataExtractor.framework__EventMetaDataExtractor.md) | 17.0.1.2.0 | light |
| [`/System/Library/PrivateFrameworks/ExchangeSync.framework/ExchangeSync`](System__Library__PrivateFrameworks__ExchangeSync.framework__ExchangeSync.md) | 2079.200.41.0.0 | light |
| [`/System/Library/PrivateFrameworks/ExchangeSync.framework/Frameworks/DAEAS.framework/DAEAS`](System__Library__PrivateFrameworks__ExchangeSync.framework__Frameworks__DAEAS.framework__DAEAS.md) | 2079.200.41.0.0 | light |
| [`/System/Library/PrivateFrameworks/ExchangeSync.framework/Frameworks/ESDaemonSupport.framework/ESDaemonSupport`](System__Library__PrivateFrameworks__ExchangeSync.framework__Frameworks__ESDaemonSupport.framework__ESDaemonSupport.md) | 2079.200.41.0.0 | light |
| [`/System/Library/PrivateFrameworks/ExchangeSyncExpress.framework/ExchangeSyncExpress`](System__Library__PrivateFrameworks__ExchangeSyncExpress.framework__ExchangeSyncExpress.md) | 2079.200.41.0.0 | light |
| [`/System/Library/PrivateFrameworks/ExclaveFDRDecode.framework/ExclaveFDRDecode`](System__Library__PrivateFrameworks__ExclaveFDRDecode.framework__ExclaveFDRDecode.md) | 1636.40.11.0.0 | full |
| [`/System/Library/PrivateFrameworks/ExclavePolarisBufferService.framework/ExclavePolarisBufferService`](System__Library__PrivateFrameworks__ExclavePolarisBufferService.framework__ExclavePolarisBufferService.md) | 256.0.5.0.0 | full |
| [`/System/Library/PrivateFrameworks/ExclavesMessageQueueProducer.framework/ExclavesMessageQueueProducer`](System__Library__PrivateFrameworks__ExclavesMessageQueueProducer.framework__ExclavesMessageQueueProducer.md) | 66.40.15.0.0 | full |
| [`/System/Library/PrivateFrameworks/ExclavesMessageQueueTypes.framework/ExclavesMessageQueueTypes`](System__Library__PrivateFrameworks__ExclavesMessageQueueTypes.framework__ExclavesMessageQueueTypes.md) | 66.40.15.0.0 | full |
| [`/System/Library/PrivateFrameworks/ExclavesOutboxConsumer.framework/ExclavesOutboxConsumer`](System__Library__PrivateFrameworks__ExclavesOutboxConsumer.framework__ExclavesOutboxConsumer.md) | 66.40.15.0.0 | full |
| [`/System/Library/PrivateFrameworks/ExclavesOutboxListener.framework/ExclavesOutboxListener`](System__Library__PrivateFrameworks__ExclavesOutboxListener.framework__ExclavesOutboxListener.md) | 66.40.15.0.0 | full |
| [`/System/Library/PrivateFrameworks/ExposureNotificationDaemon.framework/ExposureNotificationDaemon`](System__Library__PrivateFrameworks__ExposureNotificationDaemon.framework__ExposureNotificationDaemon.md) | 2701.7.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/EyeRelief.framework/EyeRelief`](System__Library__PrivateFrameworks__EyeRelief.framework__EyeRelief.md) | 36.42.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/Eyedropper.framework/Eyedropper`](System__Library__PrivateFrameworks__Eyedropper.framework__Eyedropper.md) | 9127.0.81.0.0 | light |
| [`/System/Library/PrivateFrameworks/FATCommon.framework/FATCommon`](System__Library__PrivateFrameworks__FATCommon.framework__FATCommon.md) | 845.40.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/FMCore.framework/FMCore`](System__Library__PrivateFrameworks__FMCore.framework__FMCore.md) | 219.31.7.12.1 | light |
| [`/System/Library/PrivateFrameworks/FMCoreUI.framework/FMCoreUI`](System__Library__PrivateFrameworks__FMCoreUI.framework__FMCoreUI.md) | 196.31.6.16.2 | full |
| [`/System/Library/PrivateFrameworks/FMF.framework/FMF`](System__Library__PrivateFrameworks__FMF.framework__FMF.md) | 514.31.7.12.1 | light |
| [`/System/Library/PrivateFrameworks/FMFCore.framework/FMFCore`](System__Library__PrivateFrameworks__FMFCore.framework__FMFCore.md) | 470.31.6.16.46 | light |
| [`/System/Library/PrivateFrameworks/FMFUI.framework/FMFUI`](System__Library__PrivateFrameworks__FMFUI.framework__FMFUI.md) | 514.31.7.12.1 | light |
| [`/System/Library/PrivateFrameworks/FMFindingUI.framework/FMFindingUI`](System__Library__PrivateFrameworks__FMFindingUI.framework__FMFindingUI.md) | 104.31.6.16.16 | light |
| [`/System/Library/PrivateFrameworks/FMIPCore.framework/FMIPCore`](System__Library__PrivateFrameworks__FMIPCore.framework__FMIPCore.md) | 470.31.6.16.46 | light |
| [`/System/Library/PrivateFrameworks/FRC.framework/FRC`](System__Library__PrivateFrameworks__FRC.framework__FRC.md) | 263.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/FSEvents.framework/FSEvents`](System__Library__PrivateFrameworks__FSEvents.framework__FSEvents.md) | 1433.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/FSKit.framework/FSKit`](System__Library__PrivateFrameworks__FSKit.framework__FSKit.md) | 974.40.12.0.0 | light |
| [`/System/Library/PrivateFrameworks/FTAWD.framework/FTAWD`](System__Library__PrivateFrameworks__FTAWD.framework__FTAWD.md) | 1138.200.21.0.0 | light |
| [`/System/Library/PrivateFrameworks/FTClientServices.framework/FTClientServices`](System__Library__PrivateFrameworks__FTClientServices.framework__FTClientServices.md) | 2003.200.71.2.4 | light |
| [`/System/Library/PrivateFrameworks/FaceTimeFeatureControl.framework/FaceTimeFeatureControl`](System__Library__PrivateFrameworks__FaceTimeFeatureControl.framework__FaceTimeFeatureControl.md) | 158.200.81.21.9 | light |
| [`/System/Library/PrivateFrameworks/FaceTimeNameUtility.framework/FaceTimeNameUtility`](System__Library__PrivateFrameworks__FaceTimeNameUtility.framework__FaceTimeNameUtility.md) | 1628.200.81.21.4 | light |
| [`/System/Library/PrivateFrameworks/FaceTimeNotificationCore.framework/FaceTimeNotificationCore`](System__Library__PrivateFrameworks__FaceTimeNotificationCore.framework__FaceTimeNotificationCore.md) | 3079.200.81.21.2 | light |
| [`/System/Library/PrivateFrameworks/FaceTimeNotificationUI.framework/FaceTimeNotificationUI`](System__Library__PrivateFrameworks__FaceTimeNotificationUI.framework__FaceTimeNotificationUI.md) | 3079.200.81.21.2 | light |
| [`/System/Library/PrivateFrameworks/FacesKit.framework/FacesKit`](System__Library__PrivateFrameworks__FacesKit.framework__FacesKit.md) | 2483.561.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/FamilyControlsObjC.framework/FamilyControlsObjC`](System__Library__PrivateFrameworks__FamilyControlsObjC.framework__FamilyControlsObjC.md) | 1248.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/FamilyControlsSlotSupport.framework/FamilyControlsSlotSupport`](System__Library__PrivateFrameworks__FamilyControlsSlotSupport.framework__FamilyControlsSlotSupport.md) | 1248.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/FamilyNotification.framework/FamilyNotification`](System__Library__PrivateFrameworks__FamilyNotification.framework__FamilyNotification.md) | 291.125.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags`](System__Library__PrivateFrameworks__FeatureFlags.framework__FeatureFlags.md) | 111.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/FeatureFlagsSupport.framework/FeatureFlagsSupport`](System__Library__PrivateFrameworks__FeatureFlagsSupport.framework__FeatureFlagsSupport.md) | 111.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/FedStats.framework/FedStats`](System__Library__PrivateFrameworks__FedStats.framework__FedStats.md) | 85.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/FedStatsEncoder.framework/FedStatsEncoder`](System__Library__PrivateFrameworks__FedStatsEncoder.framework__FedStatsEncoder.md) | 47.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/FedStatsPlugin.framework/FedStatsPlugin`](System__Library__PrivateFrameworks__FedStatsPlugin.framework__FedStatsPlugin.md) | 47.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/Feedback.framework/Feedback`](System__Library__PrivateFrameworks__Feedback.framework__Feedback.md) | 242.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore`](System__Library__PrivateFrameworks__FeedbackCore.framework__FeedbackCore.md) | 242.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger`](System__Library__PrivateFrameworks__FeedbackLogger.framework__FeedbackLogger.md) | 3605.27.1.11.1 | light |
| [`/System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService`](System__Library__PrivateFrameworks__FeedbackService.framework__FeedbackService.md) | 242.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/FileDerivativeDaemon.framework/FileDerivativeDaemon`](System__Library__PrivateFrameworks__FileDerivativeDaemon.framework__FileDerivativeDaemon.md) | 63.40.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/FileProviderTelemetry.framework/FileProviderTelemetry`](System__Library__PrivateFrameworks__FileProviderTelemetry.framework__FileProviderTelemetry.md) | 4838.42.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/FilesActionsUI.framework/FilesActionsUI`](System__Library__PrivateFrameworks__FilesActionsUI.framework__FilesActionsUI.md) | 57.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/FinHealth.framework/FinHealth`](System__Library__PrivateFrameworks__FinHealth.framework__FinHealth.md) | 1.9.2.5.0 | light |
| [`/System/Library/PrivateFrameworks/FinHealthCore.framework/FinHealthCore`](System__Library__PrivateFrameworks__FinHealthCore.framework__FinHealthCore.md) | 1.9.2.5.0 | light |
| [`/System/Library/PrivateFrameworks/FinHealthInsights.framework/FinHealthInsights`](System__Library__PrivateFrameworks__FinHealthInsights.framework__FinHealthInsights.md) | 1.9.2.5.0 | light |
| [`/System/Library/PrivateFrameworks/FindMyCommon.framework/FindMyCommon`](System__Library__PrivateFrameworks__FindMyCommon.framework__FindMyCommon.md) | 106.31.6.16.7 | light |
| [`/System/Library/PrivateFrameworks/FindMyCore.framework/FindMyCore`](System__Library__PrivateFrameworks__FindMyCore.framework__FindMyCore.md) | 470.31.6.16.46 | light |
| [`/System/Library/PrivateFrameworks/FindMyCrypto.framework/FindMyCrypto`](System__Library__PrivateFrameworks__FindMyCrypto.framework__FindMyCrypto.md) | 106.31.6.16.7 | light |
| [`/System/Library/PrivateFrameworks/FindMyDeviceAccessories.framework/FindMyDeviceAccessories`](System__Library__PrivateFrameworks__FindMyDeviceAccessories.framework__FindMyDeviceAccessories.md) | 482.31.6.16.21 | light |
| [`/System/Library/PrivateFrameworks/FindMyDeviceUI.framework/FindMyDeviceUI`](System__Library__PrivateFrameworks__FindMyDeviceUI.framework__FindMyDeviceUI.md) | 146.31.7.12.2 | light |
| [`/System/Library/PrivateFrameworks/FindMyFeatureFlags.framework/FindMyFeatureFlags`](System__Library__PrivateFrameworks__FindMyFeatureFlags.framework__FindMyFeatureFlags.md) | 51.31.6.16.2 | light |
| [`/System/Library/PrivateFrameworks/FindMyLocateObjCWrapper.framework/FindMyLocateObjCWrapper`](System__Library__PrivateFrameworks__FindMyLocateObjCWrapper.framework__FindMyLocateObjCWrapper.md) | 141.31.6.16.22 | light |
| [`/System/Library/PrivateFrameworks/FindMyMessaging.framework/FindMyMessaging`](System__Library__PrivateFrameworks__FindMyMessaging.framework__FindMyMessaging.md) | 106.31.6.16.7 | light |
| [`/System/Library/PrivateFrameworks/FindMyPairing.framework/FindMyPairing`](System__Library__PrivateFrameworks__FindMyPairing.framework__FindMyPairing.md) | 106.31.6.16.7 | light |
| [`/System/Library/PrivateFrameworks/FindMyStorage.framework/FindMyStorage`](System__Library__PrivateFrameworks__FindMyStorage.framework__FindMyStorage.md) | 106.31.6.16.7 | light |
| [`/System/Library/PrivateFrameworks/FindMyUICore.framework/FindMyUICore`](System__Library__PrivateFrameworks__FindMyUICore.framework__FindMyUICore.md) | 470.31.6.16.46 | light |
| [`/System/Library/PrivateFrameworks/FindMyUnsafeAsyncBridging.framework/FindMyUnsafeAsyncBridging`](System__Library__PrivateFrameworks__FindMyUnsafeAsyncBridging.framework__FindMyUnsafeAsyncBridging.md) | 106.31.6.16.7 | light |
| [`/System/Library/PrivateFrameworks/FindingUI.framework/FindingUI`](System__Library__PrivateFrameworks__FindingUI.framework__FindingUI.md) | 104.31.6.16.16 | light |
| [`/System/Library/PrivateFrameworks/FitnessAwards.framework/FitnessAwards`](System__Library__PrivateFrameworks__FitnessAwards.framework__FitnessAwards.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessCoaching.framework/FitnessCoaching`](System__Library__PrivateFrameworks__FitnessCoaching.framework__FitnessCoaching.md) | 2027.1.15.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessCoachingCore.framework/FitnessCoachingCore`](System__Library__PrivateFrameworks__FitnessCoachingCore.framework__FitnessCoachingCore.md) | 2027.1.15.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessCoachingHealthServices.framework/FitnessCoachingHealthServices`](System__Library__PrivateFrameworks__FitnessCoachingHealthServices.framework__FitnessCoachingHealthServices.md) | 2027.1.15.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessCoachingServices.framework/FitnessCoachingServices`](System__Library__PrivateFrameworks__FitnessCoachingServices.framework__FitnessCoachingServices.md) | 2027.1.15.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessDesignLibrary.framework/FitnessDesignLibrary`](System__Library__PrivateFrameworks__FitnessDesignLibrary.framework__FitnessDesignLibrary.md) | 2027.1.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessFiltering.framework/FitnessFiltering`](System__Library__PrivateFrameworks__FitnessFiltering.framework__FitnessFiltering.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessIntelligenceFeedback.framework/FitnessIntelligenceFeedback`](System__Library__PrivateFrameworks__FitnessIntelligenceFeedback.framework__FitnessIntelligenceFeedback.md) | 2027.1.35.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessIntelligenceGLP.framework/FitnessIntelligenceGLP`](System__Library__PrivateFrameworks__FitnessIntelligenceGLP.framework__FitnessIntelligenceGLP.md) | 2027.1.35.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessIntelligenceInference.framework/FitnessIntelligenceInference`](System__Library__PrivateFrameworks__FitnessIntelligenceInference.framework__FitnessIntelligenceInference.md) | 2027.1.35.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessMachineServices.framework/FitnessMachineServices`](System__Library__PrivateFrameworks__FitnessMachineServices.framework__FitnessMachineServices.md) | 2027.1.63.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessOnboarding.framework/FitnessOnboarding`](System__Library__PrivateFrameworks__FitnessOnboarding.framework__FitnessOnboarding.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessProductDetail.framework/FitnessProductDetail`](System__Library__PrivateFrameworks__FitnessProductDetail.framework__FitnessProductDetail.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessRemoteBrowsing.framework/FitnessRemoteBrowsing`](System__Library__PrivateFrameworks__FitnessRemoteBrowsing.framework__FitnessRemoteBrowsing.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessSharePlaySession.framework/FitnessSharePlaySession`](System__Library__PrivateFrameworks__FitnessSharePlaySession.framework__FitnessSharePlaySession.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessSiriSession.framework/FitnessSiriSession`](System__Library__PrivateFrameworks__FitnessSiriSession.framework__FitnessSiriSession.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessTrainerTips.framework/FitnessTrainerTips`](System__Library__PrivateFrameworks__FitnessTrainerTips.framework__FitnessTrainerTips.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessUtilities.framework/FitnessUtilities`](System__Library__PrivateFrameworks__FitnessUtilities.framework__FitnessUtilities.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessWorkoutSession.framework/FitnessWorkoutSession`](System__Library__PrivateFrameworks__FitnessWorkoutSession.framework__FitnessWorkoutSession.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/FlexMusicKit.framework/FlexMusicKit`](System__Library__PrivateFrameworks__FlexMusicKit.framework__FlexMusicKit.md) | 18.82.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/FlightUtilities.framework/FlightUtilities`](System__Library__PrivateFrameworks__FlightUtilities.framework__FlightUtilities.md) | 185.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/FlightUtilitiesCore.framework/FlightUtilitiesCore`](System__Library__PrivateFrameworks__FlightUtilitiesCore.framework__FlightUtilitiesCore.md) | 185.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/FlowFrameKit.framework/FlowFrameKit`](System__Library__PrivateFrameworks__FlowFrameKit.framework__FlowFrameKit.md) | 3605.22.1.11.1 | light |
| [`/System/Library/PrivateFrameworks/FlowToolTypes.framework/FlowToolTypes`](System__Library__PrivateFrameworks__FlowToolTypes.framework__FlowToolTypes.md) | 3605.31.1.11.2 | light |
| [`/System/Library/PrivateFrameworks/FlowTools.framework/FlowTools`](System__Library__PrivateFrameworks__FlowTools.framework__FlowTools.md) | 3605.31.1.11.2 | light |
| [`/System/Library/PrivateFrameworks/FlowToolsRunner.framework/FlowToolsRunner`](System__Library__PrivateFrameworks__FlowToolsRunner.framework__FlowToolsRunner.md) | 3605.31.1.11.2 | light |
| [`/System/Library/PrivateFrameworks/FlowToolsRuntime.framework/FlowToolsRuntime`](System__Library__PrivateFrameworks__FlowToolsRuntime.framework__FlowToolsRuntime.md) | 3605.31.1.11.2 | light |
| [`/System/Library/PrivateFrameworks/FlowToolsShared.framework/FlowToolsShared`](System__Library__PrivateFrameworks__FlowToolsShared.framework__FlowToolsShared.md) | 3605.31.1.11.2 | light |
| [`/System/Library/PrivateFrameworks/FlowToolsSnippetService.framework/FlowToolsSnippetService`](System__Library__PrivateFrameworks__FlowToolsSnippetService.framework__FlowToolsSnippetService.md) | 3605.31.1.11.2 | light |
| [`/System/Library/PrivateFrameworks/Fluid.framework/Fluid`](System__Library__PrivateFrameworks__Fluid.framework__Fluid.md) | 68.101.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/Focus.framework/Focus`](System__Library__PrivateFrameworks__Focus.framework__Focus.md) | 511.2.7.0.1 | light |
| [`/System/Library/PrivateFrameworks/FocusSettingsUI.framework/FocusSettingsUI`](System__Library__PrivateFrameworks__FocusSettingsUI.framework__FocusSettingsUI.md) | 511.2.7.0.1 | light |
| [`/System/Library/PrivateFrameworks/FocusUI.framework/FocusUI`](System__Library__PrivateFrameworks__FocusUI.framework__FocusUI.md) | 511.2.7.0.1 | light |
| [`/System/Library/PrivateFrameworks/FontServices.framework/libGSFontCache.dylib`](System__Library__PrivateFrameworks__FontServices.framework__libGSFontCache.dylib.md) | 357.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/FontServices.framework/libType1Scaler.dylib`](System__Library__PrivateFrameworks__FontServices.framework__libType1Scaler.dylib.md) | 61.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/FoundInAppsPlugins.framework/FoundInAppsPlugins`](System__Library__PrivateFrameworks__FoundInAppsPlugins.framework__FoundInAppsPlugins.md) | 1354.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/FoundationODR.framework/FoundationODR`](System__Library__PrivateFrameworks__FoundationODR.framework__FoundationODR.md) | 13.1.17.0.0 | light |
| [`/System/Library/PrivateFrameworks/FramePacing.framework/FramePacing`](System__Library__PrivateFrameworks__FramePacing.framework__FramePacing.md) | 5.0.26.0.0 | light |
| [`/System/Library/PrivateFrameworks/FriendKit.framework/FriendKit`](System__Library__PrivateFrameworks__FriendKit.framework__FriendKit.md) | 31.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/FusionTracker.framework/FusionTracker`](System__Library__PrivateFrameworks__FusionTracker.framework__FusionTracker.md) | 560.40.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/Futhark.framework/Futhark`](System__Library__PrivateFrameworks__Futhark.framework__Futhark.md) | 121.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/GCoreFramework.framework/GCoreFramework`](System__Library__PrivateFrameworks__GCoreFramework.framework__GCoreFramework.md) | 1071.40.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/GESS.framework/GESS`](System__Library__PrivateFrameworks__GESS.framework__GESS.md) | 1.5.30.0.0 | light |
| [`/System/Library/PrivateFrameworks/GLTools.framework/GLTools`](System__Library__PrivateFrameworks__GLTools.framework__GLTools.md) | 310.8.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/GLToolsCore.framework/GLToolsCore`](System__Library__PrivateFrameworks__GLToolsCore.framework__GLToolsCore.md) | 310.8.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/libComposeFilters.dylib`](System__Library__PrivateFrameworks__GPUCompiler.framework__Versions__32023__Libraries__libComposeFilters.dylib.md) | 32023.922.4.0.0 | full |
| [`/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/libGPUCompiler.dylib`](System__Library__PrivateFrameworks__GPUCompiler.framework__Versions__32023__Libraries__libGPUCompiler.dylib.md) | 32023.922.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/libGPUCompilerImpl.dylib`](System__Library__PrivateFrameworks__GPUCompiler.framework__Versions__32023__Libraries__libGPUCompilerImpl.dylib.md) | 32023.922.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/libGPUCompilerUtils.dylib`](System__Library__PrivateFrameworks__GPUCompiler.framework__Versions__32023__Libraries__libGPUCompilerUtils.dylib.md) | 32023.922.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/libllvm-flatbuffers.dylib`](System__Library__PrivateFrameworks__GPUCompiler.framework__Versions__32023__Libraries__libllvm-flatbuffers.dylib.md) | 32023.922.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/libllvm-lmdb.dylib`](System__Library__PrivateFrameworks__GPUCompiler.framework__Versions__32023__Libraries__libllvm-lmdb.dylib.md) | 32023.922.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/GPURawCounter.framework/GPURawCounter`](System__Library__PrivateFrameworks__GPURawCounter.framework__GPURawCounter.md) | 35.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/GPUSupport.framework/libGPUSupportMercury.dylib`](System__Library__PrivateFrameworks__GPUSupport.framework__libGPUSupportMercury.dylib.md) | 24.0.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/GPUTools.framework/GPUTools`](System__Library__PrivateFrameworks__GPUTools.framework__GPUTools.md) | 310.8.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/GPUToolsCaptureODIE.framework/GPUToolsCaptureODIE`](System__Library__PrivateFrameworks__GPUToolsCaptureODIE.framework__GPUToolsCaptureODIE.md) | 2027.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/GPUToolsCore.framework/GPUToolsCore`](System__Library__PrivateFrameworks__GPUToolsCore.framework__GPUToolsCore.md) | 310.8.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/GPUToolsDeviceServices.framework/GPUToolsDeviceServices`](System__Library__PrivateFrameworks__GPUToolsDeviceServices.framework__GPUToolsDeviceServices.md) | 2027.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/GPUToolsPlayback.framework/GPUToolsPlayback`](System__Library__PrivateFrameworks__GPUToolsPlayback.framework__GPUToolsPlayback.md) | 310.8.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/GPUToolsReplay.framework/GPUToolsReplay`](System__Library__PrivateFrameworks__GPUToolsReplay.framework__GPUToolsReplay.md) | 2027.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/GPUToolsTransport.framework/GPUToolsTransport`](System__Library__PrivateFrameworks__GPUToolsTransport.framework__GPUToolsTransport.md) | 2027.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/GPUToolsiOS.framework/GPUToolsiOS`](System__Library__PrivateFrameworks__GPUToolsiOS.framework__GPUToolsiOS.md) | 310.8.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/GRPCCoreInternal.framework/GRPCCoreInternal`](System__Library__PrivateFrameworks__GRPCCoreInternal.framework__GRPCCoreInternal.md) | 2.1.2.201.0 | light |
| [`/System/Library/PrivateFrameworks/GRPCInProcessTransportInternal.framework/GRPCInProcessTransportInternal`](System__Library__PrivateFrameworks__GRPCInProcessTransportInternal.framework__GRPCInProcessTransportInternal.md) | 2.1.2.201.0 | light |
| [`/System/Library/PrivateFrameworks/GRPCProtobufInternal.framework/GRPCProtobufInternal`](System__Library__PrivateFrameworks__GRPCProtobufInternal.framework__GRPCProtobufInternal.md) | 2.0.0.1.0 | light |
| [`/System/Library/PrivateFrameworks/GRPCURLSessionTransportInternal.framework/GRPCURLSessionTransportInternal`](System__Library__PrivateFrameworks__GRPCURLSessionTransportInternal.framework__GRPCURLSessionTransportInternal.md) | 1.3.4.2.0 | light |
| [`/System/Library/PrivateFrameworks/GameCenterOverlayService.framework/GameCenterOverlayService`](System__Library__PrivateFrameworks__GameCenterOverlayService.framework__GameCenterOverlayService.md) | 821.1.16.2.1 | light |
| [`/System/Library/PrivateFrameworks/GameCenterServerClient.framework/GameCenterServerClient`](System__Library__PrivateFrameworks__GameCenterServerClient.framework__GameCenterServerClient.md) | 821.1.16.2.1 | light |
| [`/System/Library/PrivateFrameworks/GameCenterUICore.framework/GameCenterUICore`](System__Library__PrivateFrameworks__GameCenterUICore.framework__GameCenterUICore.md) | 821.1.16.2.1 | light |
| [`/System/Library/PrivateFrameworks/GameControllerIO.framework/GameControllerIO`](System__Library__PrivateFrameworks__GameControllerIO.framework__GameControllerIO.md) | 14.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/GameControllerServer.framework/GameControllerServer`](System__Library__PrivateFrameworks__GameControllerServer.framework__GameControllerServer.md) | 14.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/GameControllerSettings.framework/GameControllerSettings`](System__Library__PrivateFrameworks__GameControllerSettings.framework__GameControllerSettings.md) | 14.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/GameControllerSettingsUI.framework/GameControllerSettingsUI`](System__Library__PrivateFrameworks__GameControllerSettingsUI.framework__GameControllerSettingsUI.md) | 7.0.20.0.0 | light |
| [`/System/Library/PrivateFrameworks/GameControllerUI.framework/GameControllerUI`](System__Library__PrivateFrameworks__GameControllerUI.framework__GameControllerUI.md) | 14.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/GameKitServices.framework/GameKitServices`](System__Library__PrivateFrameworks__GameKitServices.framework__GameKitServices.md) | 2263.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/GamePolicyFoundation.framework/GamePolicyFoundation`](System__Library__PrivateFrameworks__GamePolicyFoundation.framework__GamePolicyFoundation.md) | 4.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/GamePolicyServices.framework/GamePolicyServices`](System__Library__PrivateFrameworks__GamePolicyServices.framework__GamePolicyServices.md) | 4.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage`](System__Library__PrivateFrameworks__GenerationalStorage.framework__GenerationalStorage.md) | 413.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/GenerativeAgents.framework/GenerativeAgents`](System__Library__PrivateFrameworks__GenerativeAgents.framework__GenerativeAgents.md) | 297.12.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/GenerativeAgentsEvaluation.framework/GenerativeAgentsEvaluation`](System__Library__PrivateFrameworks__GenerativeAgentsEvaluation.framework__GenerativeAgentsEvaluation.md) | 297.12.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/GenerativeAgentsTransportRuntime.framework/GenerativeAgentsTransportRuntime`](System__Library__PrivateFrameworks__GenerativeAgentsTransportRuntime.framework__GenerativeAgentsTransportRuntime.md) | 297.12.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/GenerativeAssistantActions`](System__Library__PrivateFrameworks__GenerativeAssistantActions.framework__GenerativeAssistantActions.md) | 3605.4.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/GenerativeAssistantCommon.framework/GenerativeAssistantCommon`](System__Library__PrivateFrameworks__GenerativeAssistantCommon.framework__GenerativeAssistantCommon.md) | 3605.4.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/GenerativeAssistantEnablementFlow.framework/GenerativeAssistantEnablementFlow`](System__Library__PrivateFrameworks__GenerativeAssistantEnablementFlow.framework__GenerativeAssistantEnablementFlow.md) | 3605.4.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/GenerativeAssistantUI.framework/GenerativeAssistantUI`](System__Library__PrivateFrameworks__GenerativeAssistantUI.framework__GenerativeAssistantUI.md) | 3605.4.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/GenerativeExperiences.framework/GenerativeExperiences`](System__Library__PrivateFrameworks__GenerativeExperiences.framework__GenerativeExperiences.md) | 297.12.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/GenerativeExperiencesUI.framework/GenerativeExperiencesUI`](System__Library__PrivateFrameworks__GenerativeExperiencesUI.framework__GenerativeExperiencesUI.md) | 297.12.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/GenerativeLearningPlatform.framework/GenerativeLearningPlatform`](System__Library__PrivateFrameworks__GenerativeLearningPlatform.framework__GenerativeLearningPlatform.md) | 73.3.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/GenerativeLearningPlatformFoundation.framework/GenerativeLearningPlatformFoundation`](System__Library__PrivateFrameworks__GenerativeLearningPlatformFoundation.framework__GenerativeLearningPlatformFoundation.md) | 73.3.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/GeoShifter.framework/GeoShifter`](System__Library__PrivateFrameworks__GeoShifter.framework__GeoShifter.md) | 3.0.0.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend24.dylib`](usr__lib__objc__libobjcMsgSend24.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/32023/Libraries/libGPUCompilerImplLazy.dylib`](System__Library__PrivateFrameworks__GPUCompiler.framework__Versions__32023__Libraries__libGPUCompilerImplLazy.dylib.md) | 32023.922.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/GameStoreKit.framework/GameStoreKit`](System__Library__PrivateFrameworks__GameStoreKit.framework__GameStoreKit.md) | 3.1.20.2.1 | light |
| [`/System/Library/PrivateFrameworks/GenerativeFunctions.framework/GenerativeFunctions`](System__Library__PrivateFrameworks__GenerativeFunctions.framework__GenerativeFunctions.md) | 297.12.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/GenerativePartnerServiceUI.framework/GenerativePartnerServiceUI`](System__Library__PrivateFrameworks__GenerativePartnerServiceUI.framework__GenerativePartnerServiceUI.md) | 297.12.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/GeoUIFramework.framework/GeoUIFramework`](System__Library__PrivateFrameworks__GeoUIFramework.framework__GeoUIFramework.md) | 3605.14.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/Geometry.framework/Geometry`](System__Library__PrivateFrameworks__Geometry.framework__Geometry.md) | 67.40.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/GeometryCompression.framework/GeometryCompression`](System__Library__PrivateFrameworks__GeometryCompression.framework__GeometryCompression.md) | 24.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/GradientPosterFramework.framework/GradientPosterFramework`](System__Library__PrivateFrameworks__GradientPosterFramework.framework__GradientPosterFramework.md) | 50.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/GraphComputeRT.framework/GraphComputeRT`](System__Library__PrivateFrameworks__GraphComputeRT.framework__GraphComputeRT.md) | 2.3.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/GraphVisualizer.framework/GraphVisualizer`](System__Library__PrivateFrameworks__GraphVisualizer.framework__GraphVisualizer.md) | 310.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/GridDataServices.framework/GridDataServices`](System__Library__PrivateFrameworks__GridDataServices.framework__GridDataServices.md) | 78.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/H10ISPServices.framework/H10ISPServices`](System__Library__PrivateFrameworks__H10ISPServices.framework__H10ISPServices.md) | 22.304.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/H16ISPServices.framework/H16ISPServices`](System__Library__PrivateFrameworks__H16ISPServices.framework__H16ISPServices.md) | 6.104.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/HDRProcessing.framework/HDRProcessing`](System__Library__PrivateFrameworks__HDRProcessing.framework__HDRProcessing.md) | 1.521.50.0.0 | light |
| [`/System/Library/PrivateFrameworks/HID.framework/HID`](System__Library__PrivateFrameworks__HID.framework__HID.md) | 2360.40.13.0.1 | full |
| [`/System/Library/PrivateFrameworks/HIDAnalytics.framework/HIDAnalytics`](System__Library__PrivateFrameworks__HIDAnalytics.framework__HIDAnalytics.md) | 2360.40.13.0.1 | full |
| [`/System/Library/PrivateFrameworks/HIDDisplay.framework/HIDDisplay`](System__Library__PrivateFrameworks__HIDDisplay.framework__HIDDisplay.md) | 2360.40.13.0.1 | full |
| [`/System/Library/PrivateFrameworks/HIDPreferences.framework/HIDPreferences`](System__Library__PrivateFrameworks__HIDPreferences.framework__HIDPreferences.md) | 2360.40.13.0.1 | full |
| [`/System/Library/PrivateFrameworks/HIDRMClientKit.framework/HIDRMClientKit`](System__Library__PrivateFrameworks__HIDRMClientKit.framework__HIDRMClientKit.md) | 49.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/HIDRMKit.framework/HIDRMKit`](System__Library__PrivateFrameworks__HIDRMKit.framework__HIDRMKit.md) | 49.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/HIDRMUI.framework/HIDRMUI`](System__Library__PrivateFrameworks__HIDRMUI.framework__HIDRMUI.md) | 95.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/HRTFEnrollment.framework/HRTFEnrollment`](System__Library__PrivateFrameworks__HRTFEnrollment.framework__HRTFEnrollment.md) | 41.7.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HRTFEnrollmentPlaceholder.framework/HRTFEnrollmentPlaceholder`](System__Library__PrivateFrameworks__HRTFEnrollmentPlaceholder.framework__HRTFEnrollmentPlaceholder.md) | 25.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HSAAuthentication.framework/HSAAuthentication`](System__Library__PrivateFrameworks__HSAAuthentication.framework__HSAAuthentication.md) | 1138.200.21.0.0 | light |
| [`/System/Library/PrivateFrameworks/HTTPTypesInternal.framework/HTTPTypesInternal`](System__Library__PrivateFrameworks__HTTPTypesInternal.framework__HTTPTypesInternal.md) | 6681.52.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/HWAdapter.framework/HWAdapter`](System__Library__PrivateFrameworks__HWAdapter.framework__HWAdapter.md) | 200.48.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/Hands.framework/Hands`](System__Library__PrivateFrameworks__Hands.framework__Hands.md) | 13.1.21.6.0 | light |
| [`/System/Library/PrivateFrameworks/HangTracerSettingsClient.framework/HangTracerSettingsClient`](System__Library__PrivateFrameworks__HangTracerSettingsClient.framework__HangTracerSettingsClient.md) | 430.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/Haptics.framework/Haptics`](System__Library__PrivateFrameworks__Haptics.framework__Haptics.md) | 37.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/HardwareDiagnostics.framework/HardwareDiagnostics`](System__Library__PrivateFrameworks__HardwareDiagnostics.framework__HardwareDiagnostics.md) | 33.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HeadGestures.framework/HeadGestures`](System__Library__PrivateFrameworks__HeadGestures.framework__HeadGestures.md) | 40.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HeadphoneAssets.framework/HeadphoneAssets`](System__Library__PrivateFrameworks__HeadphoneAssets.framework__HeadphoneAssets.md) | 41.7.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HeadphoneConfigs.framework/HeadphoneConfigs`](System__Library__PrivateFrameworks__HeadphoneConfigs.framework__HeadphoneConfigs.md) | 2701.4.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HeadphoneProxCardBuilder.framework/HeadphoneProxCardBuilder`](System__Library__PrivateFrameworks__HeadphoneProxCardBuilder.framework__HeadphoneProxCardBuilder.md) | 41.7.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HeadphoneProxFeatureService.framework/HeadphoneProxFeatureService`](System__Library__PrivateFrameworks__HeadphoneProxFeatureService.framework__HeadphoneProxFeatureService.md) | 41.7.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HeadphoneSettings.framework/HeadphoneSettings`](System__Library__PrivateFrameworks__HeadphoneSettings.framework__HeadphoneSettings.md) | 2701.4.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HealthAgents.framework/HealthAgents`](System__Library__PrivateFrameworks__HealthAgents.framework__HealthAgents.md) | 38.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HealthAgentsTestCommon.framework/HealthAgentsTestCommon`](System__Library__PrivateFrameworks__HealthAgentsTestCommon.framework__HealthAgentsTestCommon.md) | 38.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HealthAlgorithms.framework/HealthAlgorithms`](System__Library__PrivateFrameworks__HealthAlgorithms.framework__HealthAlgorithms.md) | 151.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HealthAppServices.framework/HealthAppServices`](System__Library__PrivateFrameworks__HealthAppServices.framework__HealthAppServices.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthAppServicesUI.framework/HealthAppServicesUI`](System__Library__PrivateFrameworks__HealthAppServicesUI.framework__HealthAppServicesUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthArticlesGeneration.framework/HealthArticlesGeneration`](System__Library__PrivateFrameworks__HealthArticlesGeneration.framework__HealthArticlesGeneration.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthArticlesUI.framework/HealthArticlesUI`](System__Library__PrivateFrameworks__HealthArticlesUI.framework__HealthArticlesUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthCharts.framework/HealthCharts`](System__Library__PrivateFrameworks__HealthCharts.framework__HealthCharts.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthChartsCore.framework/HealthChartsCore`](System__Library__PrivateFrameworks__HealthChartsCore.framework__HealthChartsCore.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthCoaching.framework/HealthCoaching`](System__Library__PrivateFrameworks__HealthCoaching.framework__HealthCoaching.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthContent.framework/HealthContent`](System__Library__PrivateFrameworks__HealthContent.framework__HealthContent.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthContentAppPlugin.framework/HealthContentAppPlugin`](System__Library__PrivateFrameworks__HealthContentAppPlugin.framework__HealthContentAppPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthContentGeneration.framework/HealthContentGeneration`](System__Library__PrivateFrameworks__HealthContentGeneration.framework__HealthContentGeneration.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthContentUI.framework/HealthContentUI`](System__Library__PrivateFrameworks__HealthContentUI.framework__HealthContentUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthDiagnosticExtensionCore.framework/HealthDiagnosticExtensionCore`](System__Library__PrivateFrameworks__HealthDiagnosticExtensionCore.framework__HealthDiagnosticExtensionCore.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthDomainsDaemon.framework/HealthDomainsDaemon`](System__Library__PrivateFrameworks__HealthDomainsDaemon.framework__HealthDomainsDaemon.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthDomainsTools.framework/HealthDomainsTools`](System__Library__PrivateFrameworks__HealthDomainsTools.framework__HealthDomainsTools.md) | 3605.11.1.11.1 | light |
| [`/System/Library/PrivateFrameworks/HealthDomainsUI.framework/HealthDomainsUI`](System__Library__PrivateFrameworks__HealthDomainsUI.framework__HealthDomainsUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthEvaluations.framework/HealthEvaluations`](System__Library__PrivateFrameworks__HealthEvaluations.framework__HealthEvaluations.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthEvaluationsHealthDaemon.framework/HealthEvaluationsHealthDaemon`](System__Library__PrivateFrameworks__HealthEvaluationsHealthDaemon.framework__HealthEvaluationsHealthDaemon.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthEvaluationsUI.framework/HealthEvaluationsUI`](System__Library__PrivateFrameworks__HealthEvaluationsUI.framework__HealthEvaluationsUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthEventsDaemonImplementation.framework/HealthEventsDaemonImplementation`](System__Library__PrivateFrameworks__HealthEventsDaemonImplementation.framework__HealthEventsDaemonImplementation.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthExperience.framework/HealthExperience`](System__Library__PrivateFrameworks__HealthExperience.framework__HealthExperience.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthExposureNotificationUI.framework/HealthExposureNotificationUI`](System__Library__PrivateFrameworks__HealthExposureNotificationUI.framework__HealthExposureNotificationUI.md) | 50.3.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HealthExpressions.framework/HealthExpressions`](System__Library__PrivateFrameworks__HealthExpressions.framework__HealthExpressions.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthFacts.framework/HealthFacts`](System__Library__PrivateFrameworks__HealthFacts.framework__HealthFacts.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthFactsDaemon.framework/HealthFactsDaemon`](System__Library__PrivateFrameworks__HealthFactsDaemon.framework__HealthFactsDaemon.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthFeatures.framework/HealthFeatures`](System__Library__PrivateFrameworks__HealthFeatures.framework__HealthFeatures.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthFoundationUI.framework/HealthFoundationUI`](System__Library__PrivateFrameworks__HealthFoundationUI.framework__HealthFoundationUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthHearing.framework/HealthHearing`](System__Library__PrivateFrameworks__HealthHearing.framework__HealthHearing.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthHearingDaemon.framework/HealthHearingDaemon`](System__Library__PrivateFrameworks__HealthHearingDaemon.framework__HealthHearingDaemon.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthHeartRateStream.framework/HealthHeartRateStream`](System__Library__PrivateFrameworks__HealthHeartRateStream.framework__HealthHeartRateStream.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthHistory.framework/HealthHistory`](System__Library__PrivateFrameworks__HealthHistory.framework__HealthHistory.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthHistoryTopics.framework/HealthHistoryTopics`](System__Library__PrivateFrameworks__HealthHistoryTopics.framework__HealthHistoryTopics.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthIntelligence.framework/HealthIntelligence`](System__Library__PrivateFrameworks__HealthIntelligence.framework__HealthIntelligence.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthIntents.framework/HealthIntents`](System__Library__PrivateFrameworks__HealthIntents.framework__HealthIntents.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthKitAdditions.framework/HealthKitAdditions`](System__Library__PrivateFrameworks__HealthKitAdditions.framework__HealthKitAdditions.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthKitOrchestrationAdditions.framework/HealthKitOrchestrationAdditions`](System__Library__PrivateFrameworks__HealthKitOrchestrationAdditions.framework__HealthKitOrchestrationAdditions.md) | 7027.1.56.6.5 | full |
| [`/System/Library/PrivateFrameworks/HealthLEHeartRate.framework/HealthLEHeartRate`](System__Library__PrivateFrameworks__HealthLEHeartRate.framework__HealthLEHeartRate.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthMedications.framework/HealthMedications`](System__Library__PrivateFrameworks__HealthMedications.framework__HealthMedications.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthMedicationsDaemonPlugin.framework/HealthMedicationsDaemonPlugin`](System__Library__PrivateFrameworks__HealthMedicationsDaemonPlugin.framework__HealthMedicationsDaemonPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthMedicationsVision.framework/HealthMedicationsVision`](System__Library__PrivateFrameworks__HealthMedicationsVision.framework__HealthMedicationsVision.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthMedicationsVisionUI.framework/HealthMedicationsVisionUI`](System__Library__PrivateFrameworks__HealthMedicationsVisionUI.framework__HealthMedicationsVisionUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthMedicationsWidgetUI.framework/HealthMedicationsWidgetUI`](System__Library__PrivateFrameworks__HealthMedicationsWidgetUI.framework__HealthMedicationsWidgetUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthMenstrualCycles.framework/HealthMenstrualCycles`](System__Library__PrivateFrameworks__HealthMenstrualCycles.framework__HealthMenstrualCycles.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthMenstrualCyclesUI.framework/HealthMenstrualCyclesUI`](System__Library__PrivateFrameworks__HealthMenstrualCyclesUI.framework__HealthMenstrualCyclesUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthMenstrualCyclesWidgetUI.framework/HealthMenstrualCyclesWidgetUI`](System__Library__PrivateFrameworks__HealthMenstrualCyclesWidgetUI.framework__HealthMenstrualCyclesWidgetUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthMobility.framework/HealthMobility`](System__Library__PrivateFrameworks__HealthMobility.framework__HealthMobility.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthMobilityDaemon.framework/HealthMobilityDaemon`](System__Library__PrivateFrameworks__HealthMobilityDaemon.framework__HealthMobilityDaemon.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthMobilityUI.framework/HealthMobilityUI`](System__Library__PrivateFrameworks__HealthMobilityUI.framework__HealthMobilityUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthOntologyDaemon.framework/HealthOntologyDaemon`](System__Library__PrivateFrameworks__HealthOntologyDaemon.framework__HealthOntologyDaemon.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthPlans.framework/HealthPlans`](System__Library__PrivateFrameworks__HealthPlans.framework__HealthPlans.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthPlansAppPlugin.framework/HealthPlansAppPlugin`](System__Library__PrivateFrameworks__HealthPlansAppPlugin.framework__HealthPlansAppPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthPlansUI.framework/HealthPlansUI`](System__Library__PrivateFrameworks__HealthPlansUI.framework__HealthPlansUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthPlatformCatalogUI.framework/HealthPlatformCatalogUI`](System__Library__PrivateFrameworks__HealthPlatformCatalogUI.framework__HealthPlatformCatalogUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthRecordServices.framework/HealthRecordServices`](System__Library__PrivateFrameworks__HealthRecordServices.framework__HealthRecordServices.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthRecordsExtraction.framework/HealthRecordsExtraction`](System__Library__PrivateFrameworks__HealthRecordsExtraction.framework__HealthRecordsExtraction.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthRecordsWalletSupport.framework/HealthRecordsWalletSupport`](System__Library__PrivateFrameworks__HealthRecordsWalletSupport.framework__HealthRecordsWalletSupport.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthReport.framework/HealthReport`](System__Library__PrivateFrameworks__HealthReport.framework__HealthReport.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthReportCoreUI.framework/HealthReportCoreUI`](System__Library__PrivateFrameworks__HealthReportCoreUI.framework__HealthReportCoreUI.md) | 7027.1.56.6.5 | full |
| [`/System/Library/PrivateFrameworks/HealthReportDiagnosticExtensionCore.framework/HealthReportDiagnosticExtensionCore`](System__Library__PrivateFrameworks__HealthReportDiagnosticExtensionCore.framework__HealthReportDiagnosticExtensionCore.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthReportPlatform.framework/HealthReportPlatform`](System__Library__PrivateFrameworks__HealthReportPlatform.framework__HealthReportPlatform.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthSettingsUI.framework/HealthSettingsUI`](System__Library__PrivateFrameworks__HealthSettingsUI.framework__HealthSettingsUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthTopics.framework/HealthTopics`](System__Library__PrivateFrameworks__HealthTopics.framework__HealthTopics.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthTopicsCore.framework/HealthTopicsCore`](System__Library__PrivateFrameworks__HealthTopicsCore.framework__HealthTopicsCore.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthUtilities.framework/HealthUtilities`](System__Library__PrivateFrameworks__HealthUtilities.framework__HealthUtilities.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HearingMLHelper.framework/HearingMLHelper`](System__Library__PrivateFrameworks__HearingMLHelper.framework__HearingMLHelper.md) | 543.2.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/HearingModeService.framework/HearingModeService`](System__Library__PrivateFrameworks__HearingModeService.framework__HearingModeService.md) | 41.7.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HearingModeService_Private.framework/HearingModeService_Private`](System__Library__PrivateFrameworks__HearingModeService_Private.framework__HearingModeService_Private.md) | 41.7.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HearingModeSettingsUI.framework/HearingModeSettingsUI`](System__Library__PrivateFrameworks__HearingModeSettingsUI.framework__HearingModeSettingsUI.md) | 41.7.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HearingModeUI.framework/HearingModeUI`](System__Library__PrivateFrameworks__HearingModeUI.framework__HearingModeUI.md) | 41.7.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HearingTest.framework/HearingTest`](System__Library__PrivateFrameworks__HearingTest.framework__HearingTest.md) | 400.40.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HearingTestUI.framework/HearingTestUI`](System__Library__PrivateFrameworks__HearingTestUI.framework__HearingTestUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HearingUI.framework/HearingUI`](System__Library__PrivateFrameworks__HearingUI.framework__HearingUI.md) | 543.2.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/HeartHealth.framework/HeartHealth`](System__Library__PrivateFrameworks__HeartHealth.framework__HeartHealth.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HeartHealthDaemon.framework/HeartHealthDaemon`](System__Library__PrivateFrameworks__HeartHealthDaemon.framework__HeartHealthDaemon.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HeartHealthUI.framework/HeartHealthUI`](System__Library__PrivateFrameworks__HeartHealthUI.framework__HeartHealthUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HeartRateCoordinator.framework/HeartRateCoordinator`](System__Library__PrivateFrameworks__HeartRateCoordinator.framework__HeartRateCoordinator.md) | 42.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HeartRhythmUI.framework/HeartRhythmUI`](System__Library__PrivateFrameworks__HeartRhythmUI.framework__HeartRhythmUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/Heimdal.framework/Heimdal`](System__Library__PrivateFrameworks__Heimdal.framework__Heimdal.md) | 725.40.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/HelpKit.framework/HelpKit`](System__Library__PrivateFrameworks__HelpKit.framework__HelpKit.md) | 208.2.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/HeroDataClient.framework/HeroDataClient`](System__Library__PrivateFrameworks__HeroDataClient.framework__HeroDataClient.md) | 678.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/Highlights.framework/Highlights`](System__Library__PrivateFrameworks__Highlights.framework__Highlights.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/Home.framework/Home`](System__Library__PrivateFrameworks__Home.framework__Home.md) | 1269.2.5.6.6 | light |
| [`/System/Library/PrivateFrameworks/HomeAI.framework/HomeAI`](System__Library__PrivateFrameworks__HomeAI.framework__HomeAI.md) | 382.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HomeAccessoryControlUI.framework/HomeAccessoryControlUI`](System__Library__PrivateFrameworks__HomeAccessoryControlUI.framework__HomeAccessoryControlUI.md) | 1269.2.5.6.6 | full |
| [`/System/Library/PrivateFrameworks/HomeAppIntents.framework/HomeAppIntents`](System__Library__PrivateFrameworks__HomeAppIntents.framework__HomeAppIntents.md) | 1269.2.5.6.6 | light |
| [`/System/Library/PrivateFrameworks/HomeAutomationUIFramework.framework/HomeAutomationUIFramework`](System__Library__PrivateFrameworks__HomeAutomationUIFramework.framework__HomeAutomationUIFramework.md) | 3605.13.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/HomeCommunicationUIFramework.framework/HomeCommunicationUIFramework`](System__Library__PrivateFrameworks__HomeCommunicationUIFramework.framework__HomeCommunicationUIFramework.md) | 3605.8.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup`](System__Library__PrivateFrameworks__HomeDeviceSetup.framework__HomeDeviceSetup.md) | 405.10.36.0.0 | light |
| [`/System/Library/PrivateFrameworks/HomeKitClips.framework/HomeKitClips`](System__Library__PrivateFrameworks__HomeKitClips.framework__HomeKitClips.md) | 1520.2.7.1.3 | light |
| [`/System/Library/PrivateFrameworks/HomeKitCore.framework/HomeKitCore`](System__Library__PrivateFrameworks__HomeKitCore.framework__HomeKitCore.md) | 1520.2.7.1.3 | light |
| [`/System/Library/PrivateFrameworks/HomeKitDaemonShared.framework/HomeKitDaemonShared`](System__Library__PrivateFrameworks__HomeKitDaemonShared.framework__HomeKitDaemonShared.md) | 1520.2.7.1.3 | light |
| [`/usr/lib/objc/libobjcMsgSend25.dylib`](usr__lib__objc__libobjcMsgSend25.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/HomeAutomationInternal`](System__Library__PrivateFrameworks__HomeAutomationInternal.framework__HomeAutomationInternal.md) | 3605.13.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/HomeKitDaemonFoundation.framework/HomeKitDaemonFoundation`](System__Library__PrivateFrameworks__HomeKitDaemonFoundation.framework__HomeKitDaemonFoundation.md) | 1520.2.7.1.3 | light |
| [`/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy`](System__Library__PrivateFrameworks__HomeKitDaemonLegacy.framework__HomeKitDaemonLegacy.md) | 1520.2.7.1.3 | light |
| [`/System/Library/PrivateFrameworks/HomeMessagingUtils.framework/HomeMessagingUtils`](System__Library__PrivateFrameworks__HomeMessagingUtils.framework__HomeMessagingUtils.md) | 340.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/HomePlatformSettingsUI`](System__Library__PrivateFrameworks__HomePlatformSettingsUI.framework__HomePlatformSettingsUI.md) | 76.10.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/HomePodSettings.framework/HomePodSettings`](System__Library__PrivateFrameworks__HomePodSettings.framework__HomePodSettings.md) | 346.10.26.0.0 | light |
| [`/System/Library/PrivateFrameworks/HomeRecommendationEngine.framework/HomeRecommendationEngine`](System__Library__PrivateFrameworks__HomeRecommendationEngine.framework__HomeRecommendationEngine.md) | 1269.2.5.6.6 | light |
| [`/System/Library/PrivateFrameworks/HomeSharing.framework/HomeSharing`](System__Library__PrivateFrameworks__HomeSharing.framework__HomeSharing.md) | 4026.200.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/HomeUtilityServices.framework/HomeUtilityServices`](System__Library__PrivateFrameworks__HomeUtilityServices.framework__HomeUtilityServices.md) | 510.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HomeWidgetIntents.framework/HomeWidgetIntents`](System__Library__PrivateFrameworks__HomeWidgetIntents.framework__HomeWidgetIntents.md) | 1269.2.5.6.6 | light |
| [`/System/Library/PrivateFrameworks/HoverTextServices.framework/HoverTextServices`](System__Library__PrivateFrameworks__HoverTextServices.framework__HoverTextServices.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/HoverTextUI.framework/HoverTextUI`](System__Library__PrivateFrameworks__HoverTextUI.framework__HoverTextUI.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/Human.framework/Human`](System__Library__PrivateFrameworks__Human.framework__Human.md) | 75.40.4.0.1 | light |
| [`/System/Library/PrivateFrameworks/HumanUnderstandingEvidence.framework/HumanUnderstandingEvidence`](System__Library__PrivateFrameworks__HumanUnderstandingEvidence.framework__HumanUnderstandingEvidence.md) | 194.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HumanUnderstandingFoundation.framework/HumanUnderstandingFoundation`](System__Library__PrivateFrameworks__HumanUnderstandingFoundation.framework__HumanUnderstandingFoundation.md) | 194.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/IAPAuthentication.framework/IAPAuthentication`](System__Library__PrivateFrameworks__IAPAuthentication.framework__IAPAuthentication.md) | 2186.40.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/IDSBlastDoorSupport`](System__Library__PrivateFrameworks__IDSBlastDoorSupport.framework__IDSBlastDoorSupport.md) | 331.200.71.0.0 | light |
| [`/System/Library/PrivateFrameworks/IDSHashPersistence.framework/IDSHashPersistence`](System__Library__PrivateFrameworks__IDSHashPersistence.framework__IDSHashPersistence.md) | 2003.200.71.2.4 | light |
| [`/System/Library/PrivateFrameworks/IDSKVStore.framework/IDSKVStore`](System__Library__PrivateFrameworks__IDSKVStore.framework__IDSKVStore.md) | 2003.200.71.2.4 | light |
| [`/System/Library/PrivateFrameworks/IMAVCore.framework/IMAVCore`](System__Library__PrivateFrameworks__IMAVCore.framework__IMAVCore.md) | 692.100.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/IMAssistantCore.framework/IMAssistantCore`](System__Library__PrivateFrameworks__IMAssistantCore.framework__IMAssistantCore.md) | 1491.200.101.21.5 | light |
| [`/System/Library/PrivateFrameworks/IMCorePipeline.framework/IMCorePipeline`](System__Library__PrivateFrameworks__IMCorePipeline.framework__IMCorePipeline.md) | 1491.200.101.21.5 | light |
| [`/System/Library/PrivateFrameworks/IMDMessageServices.framework/IMDMessageServices`](System__Library__PrivateFrameworks__IMDMessageServices.framework__IMDMessageServices.md) | 1491.200.101.21.5 | light |
| [`/System/Library/PrivateFrameworks/IMRCSTransfer.framework/IMRCSTransfer`](System__Library__PrivateFrameworks__IMRCSTransfer.framework__IMRCSTransfer.md) | 1491.200.101.21.5 | light |
| [`/System/Library/PrivateFrameworks/IMSharedUI.framework/IMSharedUI`](System__Library__PrivateFrameworks__IMSharedUI.framework__IMSharedUI.md) | 1491.200.101.21.5 | light |
| [`/System/Library/PrivateFrameworks/IMTranscoderAgent.framework/IMTranscoderAgent`](System__Library__PrivateFrameworks__IMTranscoderAgent.framework__IMTranscoderAgent.md) | 1491.200.101.21.5 | light |
| [`/System/Library/PrivateFrameworks/IMTranscoding.framework/IMTranscoding`](System__Library__PrivateFrameworks__IMTranscoding.framework__IMTranscoding.md) | 1491.200.101.21.5 | light |
| [`/System/Library/PrivateFrameworks/IMTransferAgent.framework/IMTransferAgent`](System__Library__PrivateFrameworks__IMTransferAgent.framework__IMTransferAgent.md) | 1491.200.101.21.5 | light |
| [`/System/Library/PrivateFrameworks/IMTransferAgentClient.framework/IMTransferAgentClient`](System__Library__PrivateFrameworks__IMTransferAgentClient.framework__IMTransferAgentClient.md) | 1491.200.101.21.5 | light |
| [`/System/Library/PrivateFrameworks/IMTransferServices.framework/IMTransferServices`](System__Library__PrivateFrameworks__IMTransferServices.framework__IMTransferServices.md) | 1138.200.21.0.0 | light |
| [`/System/Library/PrivateFrameworks/IO80211.framework/IO80211`](System__Library__PrivateFrameworks__IO80211.framework__IO80211.md) | 1582.13.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/IOAccelMemoryInfo.framework/IOAccelMemoryInfo`](System__Library__PrivateFrameworks__IOAccelMemoryInfo.framework__IOAccelMemoryInfo.md) | 491.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/IOAccelerator.framework/IOAccelerator`](System__Library__PrivateFrameworks__IOAccelerator.framework__IOAccelerator.md) | 491.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/IOAccessoryManager.framework/IOAccessoryManager`](System__Library__PrivateFrameworks__IOAccessoryManager.framework__IOAccessoryManager.md) | 1068.40.6.0.0 | full |
| [`/System/Library/PrivateFrameworks/IOCEC.framework/IOCEC`](System__Library__PrivateFrameworks__IOCEC.framework__IOCEC.md) | 69.0.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/IOFastPath.framework/IOFastPath`](System__Library__PrivateFrameworks__IOFastPath.framework__IOFastPath.md) | 2360.40.13.0.1 | light |
| [`/System/Library/PrivateFrameworks/IOImageLoader.framework/IOImageLoader`](System__Library__PrivateFrameworks__IOImageLoader.framework__IOImageLoader.md) | 340.2.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/IOKitten.framework/IOKitten`](System__Library__PrivateFrameworks__IOKitten.framework__IOKitten.md) | 500.2.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator`](System__Library__PrivateFrameworks__IOSurfaceAccelerator.framework__IOSurfaceAccelerator.md) | 200.69.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost`](System__Library__PrivateFrameworks__IOUSBHost.framework__IOUSBHost.md) | 1617.40.10.0.0 | full |
| [`/System/Library/PrivateFrameworks/IPConfiguration.framework/IPConfiguration`](System__Library__PrivateFrameworks__IPConfiguration.framework__IPConfiguration.md) | 557.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ISPExclaveKitServices.framework/ISPExclaveKitServices`](System__Library__PrivateFrameworks__ISPExclaveKitServices.framework__ISPExclaveKitServices.md) | 6.104.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) | 20.112.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/ISPServices.framework/ISPServices`](System__Library__PrivateFrameworks__ISPServices.framework__ISPServices.md) | 20.112.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/IVRConversationAssistant.framework/IVRConversationAssistant`](System__Library__PrivateFrameworks__IVRConversationAssistant.framework__IVRConversationAssistant.md) | 2.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/IXATestAppRelay.framework/IXATestAppRelay`](System__Library__PrivateFrameworks__IXATestAppRelay.framework__IXATestAppRelay.md) | 3568.1.8.600.0 | light |
| [`/System/Library/PrivateFrameworks/IdleTimerHosting.framework/IdleTimerHosting`](System__Library__PrivateFrameworks__IdleTimerHosting.framework__IdleTimerHosting.md) | 41.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/IdleTimerServices.framework/IdleTimerServices`](System__Library__PrivateFrameworks__IdleTimerServices.framework__IdleTimerServices.md) | 41.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ImageCaptureDevices.framework/ImageCaptureDevices`](System__Library__PrivateFrameworks__ImageCaptureDevices.framework__ImageCaptureDevices.md) | 2118.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ImageHarmonizationKit.framework/ImageHarmonizationKit`](System__Library__PrivateFrameworks__ImageHarmonizationKit.framework__ImageHarmonizationKit.md) | 98.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ImagePlaygroundInternal.framework/ImagePlaygroundInternal`](System__Library__PrivateFrameworks__ImagePlaygroundInternal.framework__ImagePlaygroundInternal.md) | 198.2.12.600.0 | light |
| [`/System/Library/PrivateFrameworks/ImagePlaygroundPosterFramework.framework/ImagePlaygroundPosterFramework`](System__Library__PrivateFrameworks__ImagePlaygroundPosterFramework.framework__ImagePlaygroundPosterFramework.md) | 198.2.12.600.0 | light |
| [`/System/Library/PrivateFrameworks/InAppFeedback.framework/InAppFeedback`](System__Library__PrivateFrameworks__InAppFeedback.framework__InAppFeedback.md) | 1.4.18.0.0 | light |
| [`/System/Library/PrivateFrameworks/InAppMessages.framework/InAppMessages`](System__Library__PrivateFrameworks__InAppMessages.framework__InAppMessages.md) | 4024.100.3.1.0 | light |
| [`/System/Library/PrivateFrameworks/InAppMessagesCore.framework/InAppMessagesCore`](System__Library__PrivateFrameworks__InAppMessagesCore.framework__InAppMessagesCore.md) | 4024.100.3.1.0 | light |
| [`/System/Library/PrivateFrameworks/IncomingCallFilter.framework/IncomingCallFilter`](System__Library__PrivateFrameworks__IncomingCallFilter.framework__IncomingCallFilter.md) | 196.200.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/InertiaCam.framework/InertiaCam`](System__Library__PrivateFrameworks__InertiaCam.framework__InertiaCam.md) | 50.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/InfieldCompensation.framework/InfieldCompensation`](System__Library__PrivateFrameworks__InfieldCompensation.framework__InfieldCompensation.md) | 9.26.5.12.5 | light |
| [`/System/Library/PrivateFrameworks/InfoQueryPersonalizationFeatures.framework/InfoQueryPersonalizationFeatures`](System__Library__PrivateFrameworks__InfoQueryPersonalizationFeatures.framework__InfoQueryPersonalizationFeatures.md) | 3605.24.1.11.2 | light |
| [`/System/Library/PrivateFrameworks/InputAccessoriesSettings.framework/InputAccessoriesSettings`](System__Library__PrivateFrameworks__InputAccessoriesSettings.framework__InputAccessoriesSettings.md) | 2027.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/InputContext.framework/InputContext`](System__Library__PrivateFrameworks__InputContext.framework__InputContext.md) | 137.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/InputTestFoundation.framework/InputTestFoundation`](System__Library__PrivateFrameworks__InputTestFoundation.framework__InputTestFoundation.md) | 42.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/InputToolKit.framework/InputToolKit`](System__Library__PrivateFrameworks__InputToolKit.framework__InputToolKit.md) | 41.3.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/InputToolKitUI.framework/InputToolKitUI`](System__Library__PrivateFrameworks__InputToolKitUI.framework__InputToolKitUI.md) | 41.3.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/InputTranscoder.framework/InputTranscoder`](System__Library__PrivateFrameworks__InputTranscoder.framework__InputTranscoder.md) | 110.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/InstallProgress.framework/InstallProgress`](System__Library__PrivateFrameworks__InstallProgress.framework__InstallProgress.md) | 13.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligenceEngine.framework/IntelligenceEngine`](System__Library__PrivateFrameworks__IntelligenceEngine.framework__IntelligenceEngine.md) | 3500.3.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligenceFlowAppIntentsPreviewToolSupport.framework/IntelligenceFlowAppIntentsPreviewToolSupport`](System__Library__PrivateFrameworks__IntelligenceFlowAppIntentsPreviewToolSupport.framework__IntelligenceFlowAppIntentsPreviewToolSupport.md) | 3605.22.501.11.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligenceFlowContext.framework/IntelligenceFlowContext`](System__Library__PrivateFrameworks__IntelligenceFlowContext.framework__IntelligenceFlowContext.md) | 3605.22.501.11.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligenceFlowConversationRuntime.framework/IntelligenceFlowConversationRuntime`](System__Library__PrivateFrameworks__IntelligenceFlowConversationRuntime.framework__IntelligenceFlowConversationRuntime.md) | 3605.22.501.11.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligenceFlowErrorTypes.framework/IntelligenceFlowErrorTypes`](System__Library__PrivateFrameworks__IntelligenceFlowErrorTypes.framework__IntelligenceFlowErrorTypes.md) | 3605.22.501.11.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/IntelligencePlatformCompute`](System__Library__PrivateFrameworks__IntelligencePlatformCompute.framework__IntelligencePlatformCompute.md) | 259.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligencePlatformDataActions.framework/IntelligencePlatformDataActions`](System__Library__PrivateFrameworks__IntelligencePlatformDataActions.framework__IntelligencePlatformDataActions.md) | 194.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligencePlatformQuery.framework/IntelligencePlatformQuery`](System__Library__PrivateFrameworks__IntelligencePlatformQuery.framework__IntelligencePlatformQuery.md) | 259.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligenceSimulation.framework/IntelligenceSimulation`](System__Library__PrivateFrameworks__IntelligenceSimulation.framework__IntelligenceSimulation.md) | 3605.12.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligenceTasks.framework/IntelligenceTasks`](System__Library__PrivateFrameworks__IntelligenceTasks.framework__IntelligenceTasks.md) | 259.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligentRouting.framework/IntelligentRouting`](System__Library__PrivateFrameworks__IntelligentRouting.framework__IntelligentRouting.md) | 125.1.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligentRoutingServices.framework/IntelligentRoutingServices`](System__Library__PrivateFrameworks__IntelligentRoutingServices.framework__IntelligentRoutingServices.md) | 125.1.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntelligentTrackingCore.framework/IntelligentTrackingCore`](System__Library__PrivateFrameworks__IntelligentTrackingCore.framework__IntelligentTrackingCore.md) | 432.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntentRecommend.framework/IntentRecommend`](System__Library__PrivateFrameworks__IntentRecommend.framework__IntentRecommend.md) | 99.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntentRecommendRuntime.framework/IntentRecommendRuntime`](System__Library__PrivateFrameworks__IntentRecommendRuntime.framework__IntentRecommendRuntime.md) | 99.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntentRecommendShared.framework/IntentRecommendShared`](System__Library__PrivateFrameworks__IntentRecommendShared.framework__IntentRecommendShared.md) | 99.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntentsCore.framework/IntentsCore`](System__Library__PrivateFrameworks__IntentsCore.framework__IntentsCore.md) | 4016.1.16.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntentsFoundation.framework/IntentsFoundation`](System__Library__PrivateFrameworks__IntentsFoundation.framework__IntentsFoundation.md) | 4016.1.16.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntentsServices.framework/IntentsServices`](System__Library__PrivateFrameworks__IntentsServices.framework__IntentsServices.md) | 4016.1.16.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntentsUICardKitProviderSupport.framework/IntentsUICardKitProviderSupport`](System__Library__PrivateFrameworks__IntentsUICardKitProviderSupport.framework__IntentsUICardKitProviderSupport.md) | 3520.8.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/InternationalTextSearch.framework/InternationalTextSearch`](System__Library__PrivateFrameworks__InternationalTextSearch.framework__InternationalTextSearch.md) | 1027.200.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/IntlPreferencesUI.framework/IntlPreferencesUI`](System__Library__PrivateFrameworks__IntlPreferencesUI.framework__IntlPreferencesUI.md) | 500.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient`](System__Library__PrivateFrameworks__IsolatedCoreAudioClient.framework__IsolatedCoreAudioClient.md) | 7.49.200.0.0 | full |
| [`/System/Library/PrivateFrameworks/JITAppKit.framework/JITAppKit`](System__Library__PrivateFrameworks__JITAppKit.framework__JITAppKit.md) | 1.0.27.0.0 | light |
| [`/System/Library/PrivateFrameworks/Jet.framework/Jet`](System__Library__PrivateFrameworks__Jet.framework__Jet.md) | 14.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/JetFoundation.framework/JetFoundation`](System__Library__PrivateFrameworks__JetFoundation.framework__JetFoundation.md) | 10.1.11.0.0 | light |
| [`/System/Library/PrivateFrameworks/JetPack.framework/JetPack`](System__Library__PrivateFrameworks__JetPack.framework__JetPack.md) | 10.1.11.0.0 | light |
| [`/System/Library/PrivateFrameworks/JetsamProperties.framework/JetsamProperties`](System__Library__PrivateFrameworks__JetsamProperties.framework__JetsamProperties.md) | 3015.52.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/JoinRequests.framework/JoinRequests`](System__Library__PrivateFrameworks__JoinRequests.framework__JoinRequests.md) | 309.200.71.21.1 | light |
| [`/System/Library/PrivateFrameworks/JournalShared.framework/JournalShared`](System__Library__PrivateFrameworks__JournalShared.framework__JournalShared.md) | 113.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/JournalUI.framework/JournalUI`](System__Library__PrivateFrameworks__JournalUI.framework__JournalUI.md) | 113.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/KRExperiments.framework/KRExperiments`](System__Library__PrivateFrameworks__KRExperiments.framework__KRExperiments.md) | 233.52.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/KernelManagerLibrary.framework/KernelManagerLibrary`](System__Library__PrivateFrameworks__KernelManagerLibrary.framework__KernelManagerLibrary.md) | 71.5.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/KeyboardServices.framework/KeyboardServices`](System__Library__PrivateFrameworks__KeyboardServices.framework__KeyboardServices.md) | 161.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/KeyboardSettings.framework/KeyboardSettings`](System__Library__PrivateFrameworks__KeyboardSettings.framework__KeyboardSettings.md) | 148.1.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/KeyboardSettingsFeedback.framework/KeyboardSettingsFeedback`](System__Library__PrivateFrameworks__KeyboardSettingsFeedback.framework__KeyboardSettingsFeedback.md) | 9127.1.13.7.0 | light |
| [`/System/Library/PrivateFrameworks/KnowledgeGraphKit.framework/KnowledgeGraphKit`](System__Library__PrivateFrameworks__KnowledgeGraphKit.framework__KnowledgeGraphKit.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/KnowledgeMonitor.framework/KnowledgeMonitor`](System__Library__PrivateFrameworks__KnowledgeMonitor.framework__KnowledgeMonitor.md) | 480.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/KoaMapper.framework/KoaMapper`](System__Library__PrivateFrameworks__KoaMapper.framework__KoaMapper.md) | 3600.13.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/LACC.framework/LACC`](System__Library__PrivateFrameworks__LACC.framework__LACC.md) | 8.2.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/LLMCache.framework/LLMCache`](System__Library__PrivateFrameworks__LLMCache.framework__LLMCache.md) | 3500.5.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/LabKit.framework/LabKit`](System__Library__PrivateFrameworks__LabKit.framework__LabKit.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/LabKitDaemon.framework/LabKitDaemon`](System__Library__PrivateFrameworks__LabKitDaemon.framework__LabKitDaemon.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/LabKitUI.framework/LabKitUI`](System__Library__PrivateFrameworks__LabKitUI.framework__LabKitUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/LatentSemanticMapping.framework/LatentSemanticMapping`](System__Library__PrivateFrameworks__LatentSemanticMapping.framework__LatentSemanticMapping.md) | 3.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/LearnedFeatures.framework/LearnedFeatures`](System__Library__PrivateFrameworks__LearnedFeatures.framework__LearnedFeatures.md) | 9.26.7.9.0 | light |
| [`/System/Library/PrivateFrameworks/LegacyGameKit.framework/LegacyGameKit`](System__Library__PrivateFrameworks__LegacyGameKit.framework__LegacyGameKit.md) | 821.1.16.2.1 | light |
| [`/System/Library/PrivateFrameworks/LegalAndRegulatorySettingsSupport.framework/LegalAndRegulatorySettingsSupport`](System__Library__PrivateFrameworks__LegalAndRegulatorySettingsSupport.framework__LegalAndRegulatorySettingsSupport.md) | 2027.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/LiftUI.framework/LiftUI`](System__Library__PrivateFrameworks__LiftUI.framework__LiftUI.md) | 301.24.1.2.0 | light |
| [`/System/Library/PrivateFrameworks/LightSourceSupport.framework/LightSourceSupport`](System__Library__PrivateFrameworks__LightSourceSupport.framework__LightSourceSupport.md) | 8.1.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/LighthouseAV.framework/LighthouseAV`](System__Library__PrivateFrameworks__LighthouseAV.framework__LighthouseAV.md) | 32.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/LighthouseBitacoraFramework.framework/LighthouseBitacoraFramework`](System__Library__PrivateFrameworks__LighthouseBitacoraFramework.framework__LighthouseBitacoraFramework.md) | 3.7.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/LighthouseCoreMLFeatureStore.framework/LighthouseCoreMLFeatureStore`](System__Library__PrivateFrameworks__LighthouseCoreMLFeatureStore.framework__LighthouseCoreMLFeatureStore.md) | 3.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/LighthouseCoreMLModelAnalysis.framework/LighthouseCoreMLModelAnalysis`](System__Library__PrivateFrameworks__LighthouseCoreMLModelAnalysis.framework__LighthouseCoreMLModelAnalysis.md) | 3.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/LighthouseCoreMLModelStore.framework/LighthouseCoreMLModelStore`](System__Library__PrivateFrameworks__LighthouseCoreMLModelStore.framework__LighthouseCoreMLModelStore.md) | 3.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/LighthouseDataProcessor.framework/LighthouseDataProcessor`](System__Library__PrivateFrameworks__LighthouseDataProcessor.framework__LighthouseDataProcessor.md) | 2.4.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/LighthouseInference.framework/LighthouseInference`](System__Library__PrivateFrameworks__LighthouseInference.framework__LighthouseInference.md) | 3605.17.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/LighthouseQuartz.framework/LighthouseQuartz`](System__Library__PrivateFrameworks__LighthouseQuartz.framework__LighthouseQuartz.md) | 1.1.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/LighthouseServicesAnalyticsFramework.framework/LighthouseServicesAnalyticsFramework`](System__Library__PrivateFrameworks__LighthouseServicesAnalyticsFramework.framework__LighthouseServicesAnalyticsFramework.md) | 1.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/LimitAdTracking.framework/LimitAdTracking`](System__Library__PrivateFrameworks__LimitAdTracking.framework__LimitAdTracking.md) | 638.2.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/LinguisticData.framework/LinguisticData`](System__Library__PrivateFrameworks__LinguisticData.framework__LinguisticData.md) | 692.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/LinkPresentationMessagesSupport.framework/LinkPresentationMessagesSupport`](System__Library__PrivateFrameworks__LinkPresentationMessagesSupport.framework__LinkPresentationMessagesSupport.md) | 317.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/LinkPresentationStyleSheetParsing.framework/LinkPresentationStyleSheetParsing`](System__Library__PrivateFrameworks__LinkPresentationStyleSheetParsing.framework__LinkPresentationStyleSheetParsing.md) | 317.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/LiveExecutionResultsFoundation.framework/LiveExecutionResultsFoundation`](System__Library__PrivateFrameworks__LiveExecutionResultsFoundation.framework__LiveExecutionResultsFoundation.md) | 701.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/LiveExecutionResultsProbe.framework/LiveExecutionResultsProbe`](System__Library__PrivateFrameworks__LiveExecutionResultsProbe.framework__LiveExecutionResultsProbe.md) | 701.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/LiveExecutionResultsRuntime.framework/LiveExecutionResultsRuntime`](System__Library__PrivateFrameworks__LiveExecutionResultsRuntime.framework__LiveExecutionResultsRuntime.md) | 701.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/LiveFS.framework/LiveFS`](System__Library__PrivateFrameworks__LiveFS.framework__LiveFS.md) | 974.40.12.0.0 | light |
| [`/System/Library/PrivateFrameworks/LiveFSFPHelper.framework/LiveFSFPHelper`](System__Library__PrivateFrameworks__LiveFSFPHelper.framework__LiveFSFPHelper.md) | 974.40.12.0.0 | light |
| [`/System/Library/PrivateFrameworks/LiveSpeechServices.framework/LiveSpeechServices`](System__Library__PrivateFrameworks__LiveSpeechServices.framework__LiveSpeechServices.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/LiveSpeechUI.framework/LiveSpeechUI`](System__Library__PrivateFrameworks__LiveSpeechUI.framework__LiveSpeechUI.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI`](System__Library__PrivateFrameworks__LocalAuthenticationCoreUI.framework__LocalAuthenticationCoreUI.md) | 2319.52.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/LocalAuthenticationCredentialServices.framework/LocalAuthenticationCredentialServices`](System__Library__PrivateFrameworks__LocalAuthenticationCredentialServices.framework__LocalAuthenticationCredentialServices.md) | 2319.52.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/LocalAuthenticationPreboard.framework/LocalAuthenticationPreboard`](System__Library__PrivateFrameworks__LocalAuthenticationPreboard.framework__LocalAuthenticationPreboard.md) | 2319.52.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/LocalSpeechRecognitionBridge.framework/LocalSpeechRecognitionBridge`](System__Library__PrivateFrameworks__LocalSpeechRecognitionBridge.framework__LocalSpeechRecognitionBridge.md) | 3605.32.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/LocationAccessStore.framework/LocationAccessStore`](System__Library__PrivateFrameworks__LocationAccessStore.framework__LocationAccessStore.md) | 3187.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/LocationAuthorizationXPC.framework/LocationAuthorizationXPC`](System__Library__PrivateFrameworks__LocationAuthorizationXPC.framework__LocationAuthorizationXPC.md) | 3187.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/LocationLogEncryption.framework/LocationLogEncryption`](System__Library__PrivateFrameworks__LocationLogEncryption.framework__LocationLogEncryption.md) | 3187.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/LockdownModeUI.framework/LockdownModeUI`](System__Library__PrivateFrameworks__LockdownModeUI.framework__LockdownModeUI.md) | 128.40.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/LockedContentServices.framework/LockedContentServices`](System__Library__PrivateFrameworks__LockedContentServices.framework__LockedContentServices.md) | 159.2.5.0.6 | light |
| [`/System/Library/PrivateFrameworks/LockoutUI.framework/LockoutUI`](System__Library__PrivateFrameworks__LockoutUI.framework__LockoutUI.md) | 1.0.11.0.0 | light |
| [`/System/Library/PrivateFrameworks/LoginKit.framework/LoginKit`](System__Library__PrivateFrameworks__LoginKit.framework__LoginKit.md) | 3034.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/LoginPerformanceKit.framework/LoginPerformanceKit`](System__Library__PrivateFrameworks__LoginPerformanceKit.framework__LoginPerformanceKit.md) | 3034.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/LoginUILogViewer.framework/LoginUILogViewer`](System__Library__PrivateFrameworks__LoginUILogViewer.framework__LoginUILogViewer.md) | 3034.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/LowPowerMode.framework/LowPowerMode`](System__Library__PrivateFrameworks__LowPowerMode.framework__LowPowerMode.md) | 2043.40.52.0.2 | light |
| [`/System/Library/PrivateFrameworks/MCCFoundation.framework/MCCFoundation`](System__Library__PrivateFrameworks__MCCFoundation.framework__MCCFoundation.md) | 2027.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/MCCKitCategorization.framework/MCCKitCategorization`](System__Library__PrivateFrameworks__MCCKitCategorization.framework__MCCKitCategorization.md) | 2027.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/MDM.framework/MDM`](System__Library__PrivateFrameworks__MDM.framework__MDM.md) | 113.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication`](System__Library__PrivateFrameworks__MFAAuthentication.framework__MFAAuthentication.md) | 1219.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/MIL.framework/MIL`](System__Library__PrivateFrameworks__MIL.framework__MIL.md) | 3605.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/MLCompilerRuntime.framework/MLCompilerRuntime`](System__Library__PrivateFrameworks__MLCompilerRuntime.framework__MLCompilerRuntime.md) | 3600.11.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/MLCompilerServices.framework/MLCompilerServices`](System__Library__PrivateFrameworks__MLCompilerServices.framework__MLCompilerServices.md) | 3600.11.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/MLKit.framework/MLKit`](System__Library__PrivateFrameworks__MLKit.framework__MLKit.md) | 158.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MLModelAsset.framework/MLModelAsset`](System__Library__PrivateFrameworks__MLModelAsset.framework__MLModelAsset.md) | 3605.6.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/MLModelCache.framework/MLModelCache`](System__Library__PrivateFrameworks__MLModelCache.framework__MLModelCache.md) | 3605.6.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/MLModelSpecification.framework/MLModelSpecification`](System__Library__PrivateFrameworks__MLModelSpecification.framework__MLModelSpecification.md) | 107.40.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/MLRuntime.framework/MLRuntime`](System__Library__PrivateFrameworks__MLRuntime.framework__MLRuntime.md) | 113.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MMCS.framework/MMCS`](System__Library__PrivateFrameworks__MMCS.framework__MMCS.md) | 2700.112.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MMCSServices.framework/MMCSServices`](System__Library__PrivateFrameworks__MMCSServices.framework__MMCSServices.md) | 1491.200.101.21.5 | light |
| [`/System/Library/PrivateFrameworks/MOVStreamIO.framework/MOVStreamIO`](System__Library__PrivateFrameworks__MOVStreamIO.framework__MOVStreamIO.md) | 3.40.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/MPUFoundation.framework/MPUFoundation`](System__Library__PrivateFrameworks__MPUFoundation.framework__MPUFoundation.md) | 4026.100.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/MSGExternalSync.framework/MSGExternalSync`](System__Library__PrivateFrameworks__MSGExternalSync.framework__MSGExternalSync.md) | 420.0.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor`](System__Library__PrivateFrameworks__MSUDataAccessor.framework__MSUDataAccessor.md) | 3696.40.14.0.1 | light |
| [`/System/Library/PrivateFrameworks/MTL3On4.framework/MTL3On4`](System__Library__PrivateFrameworks__MTL3On4.framework__MTL3On4.md) | 383.1.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/MTLCompiler.framework/Versions/32023/MTLCompiler`](System__Library__PrivateFrameworks__MTLCompiler.framework__Versions__32023__MTLCompiler.md) | 383.1.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/MTLCompiler.framework/Versions/32024/MTLCompiler`](System__Library__PrivateFrameworks__MTLCompiler.framework__Versions__32024__MTLCompiler.md) | 383.1.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/MTLCompiler.framework/libMTLCompilerHelper.dylib`](System__Library__PrivateFrameworks__MTLCompiler.framework__libMTLCompilerHelper.dylib.md) | 383.1.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/MTLToolsDeviceSupport.framework/MTLToolsDeviceSupport`](System__Library__PrivateFrameworks__MTLToolsDeviceSupport.framework__MTLToolsDeviceSupport.md) | 310.8.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/MXI.framework/MXI`](System__Library__PrivateFrameworks__MXI.framework__MXI.md) | 48.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/MXUIService.framework/MXUIService`](System__Library__PrivateFrameworks__MXUIService.framework__MXUIService.md) | 385.10.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/MXUIServiceClient.framework/MXUIServiceClient`](System__Library__PrivateFrameworks__MXUIServiceClient.framework__MXUIServiceClient.md) | 385.10.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/MacinTalk.framework/MacinTalk`](System__Library__PrivateFrameworks__MacinTalk.framework__MacinTalk.md) | 108.2.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/MacinTalkCore.framework/MacinTalkCore`](System__Library__PrivateFrameworks__MacinTalkCore.framework__MacinTalkCore.md) | 108.2.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/MagnifierServices.framework/MagnifierServices`](System__Library__PrivateFrameworks__MagnifierServices.framework__MagnifierServices.md) | 291.4.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/MagnifierSupport.framework/MagnifierSupport`](System__Library__PrivateFrameworks__MagnifierSupport.framework__MagnifierSupport.md) | 291.4.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/MailKit.framework/MailKit`](System__Library__PrivateFrameworks__MailKit.framework__MailKit.md) | 3901.200.71.21.4 | light |
| [`/System/Library/PrivateFrameworks/MailSearchSchemaManifest.framework/MailSearchSchemaManifest`](System__Library__PrivateFrameworks__MailSearchSchemaManifest.framework__MailSearchSchemaManifest.md) | 2.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/MailServices.framework/MailServices`](System__Library__PrivateFrameworks__MailServices.framework__MailServices.md) | 3901.200.71.21.4 | light |
| [`/System/Library/PrivateFrameworks/MailWebProcessSupport.framework/MailWebProcessSupport`](System__Library__PrivateFrameworks__MailWebProcessSupport.framework__MailWebProcessSupport.md) | 3901.200.71.21.4 | light |
| [`/System/Library/PrivateFrameworks/ManagedAppsCore.framework/ManagedAppsCore`](System__Library__PrivateFrameworks__ManagedAppsCore.framework__ManagedAppsCore.md) | 113.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ManagedAppsInterface.framework/ManagedAppsInterface`](System__Library__PrivateFrameworks__ManagedAppsInterface.framework__ManagedAppsInterface.md) | 113.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ManagedAssets.framework/ManagedAssets`](System__Library__PrivateFrameworks__ManagedAssets.framework__ManagedAssets.md) | 279.0.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/ManagedBackgroundAssets`](System__Library__PrivateFrameworks__ManagedBackgroundAssets.framework__ManagedBackgroundAssets.md) | 2.1.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/ManagedBackgroundAssetsHelperFetching.framework/ManagedBackgroundAssetsHelperFetching`](System__Library__PrivateFrameworks__ManagedBackgroundAssetsHelperFetching.framework__ManagedBackgroundAssetsHelperFetching.md) | 2.1.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/ManagedConfigurationUI.framework/ManagedConfigurationUI`](System__Library__PrivateFrameworks__ManagedConfigurationUI.framework__ManagedConfigurationUI.md) | 113.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ManagedDevice.framework/ManagedDevice`](System__Library__PrivateFrameworks__ManagedDevice.framework__ManagedDevice.md) | 31.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ManagedOrganizationContacts.framework/ManagedOrganizationContacts`](System__Library__PrivateFrameworks__ManagedOrganizationContacts.framework__ManagedOrganizationContacts.md) | 152.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ManagedSettingsSupport.framework/ManagedSettingsSupport`](System__Library__PrivateFrameworks__ManagedSettingsSupport.framework__ManagedSettingsSupport.md) | 319.40.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/MapsBlastDoorSupport.framework/MapsBlastDoorSupport`](System__Library__PrivateFrameworks__MapsBlastDoorSupport.framework__MapsBlastDoorSupport.md) | 331.200.71.0.0 | light |
| [`/System/Library/PrivateFrameworks/MapsIntelligence.framework/MapsIntelligence`](System__Library__PrivateFrameworks__MapsIntelligence.framework__MapsIntelligence.md) | 2972.31.6.17.137 | light |
| [`/System/Library/PrivateFrameworks/Marco.framework/Marco`](System__Library__PrivateFrameworks__Marco.framework__Marco.md) | 1138.200.21.0.0 | light |
| [`/System/Library/PrivateFrameworks/MarkupUI.framework/MarkupUI`](System__Library__PrivateFrameworks__MarkupUI.framework__MarkupUI.md) | 584.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/MathTypesetting.framework/MathTypesetting`](System__Library__PrivateFrameworks__MathTypesetting.framework__MathTypesetting.md) | 8.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/MatterPlugin.framework/MatterPlugin`](System__Library__PrivateFrameworks__MatterPlugin.framework__MatterPlugin.md) | 89.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MeasureFoundation.framework/MeasureFoundation`](System__Library__PrivateFrameworks__MeasureFoundation.framework__MeasureFoundation.md) | 196.40.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/MediaAnalysisBlastDoorSupport.framework/MediaAnalysisBlastDoorSupport`](System__Library__PrivateFrameworks__MediaAnalysisBlastDoorSupport.framework__MediaAnalysisBlastDoorSupport.md) | 331.200.71.0.0 | light |
| [`/System/Library/PrivateFrameworks/MediaAnalysisCore.framework/MediaAnalysisCore`](System__Library__PrivateFrameworks__MediaAnalysisCore.framework__MediaAnalysisCore.md) | 460.14.1.2.0 | light |
| [`/System/Library/PrivateFrameworks/MediaAnalysisGeneration.framework/MediaAnalysisGeneration`](System__Library__PrivateFrameworks__MediaAnalysisGeneration.framework__MediaAnalysisGeneration.md) | 460.14.1.2.0 | light |
| [`/System/Library/PrivateFrameworks/MediaAnalysisPhotosServices.framework/MediaAnalysisPhotosServices`](System__Library__PrivateFrameworks__MediaAnalysisPhotosServices.framework__MediaAnalysisPhotosServices.md) | 460.14.1.2.0 | full |
| [`/System/Library/PrivateFrameworks/MediaContinuityKit.framework/MediaContinuityKit`](System__Library__PrivateFrameworks__MediaContinuityKit.framework__MediaContinuityKit.md) | 125.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MediaControlReceiver.framework/MediaControlReceiver`](System__Library__PrivateFrameworks__MediaControlReceiver.framework__MediaControlReceiver.md) | 1005.13.1.1.0 | light |
| [`/System/Library/PrivateFrameworks/MediaControlSender.framework/MediaControlSender`](System__Library__PrivateFrameworks__MediaControlSender.framework__MediaControlSender.md) | 1005.13.1.1.0 | light |
| [`/System/Library/PrivateFrameworks/MediaControlUI.framework/MediaControlUI`](System__Library__PrivateFrameworks__MediaControlUI.framework__MediaControlUI.md) | 4026.210.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/MediaFoundation.framework/MediaFoundation`](System__Library__PrivateFrameworks__MediaFoundation.framework__MediaFoundation.md) | 4026.200.17.0.0 | light |
| [`/System/Library/PrivateFrameworks/MediaIntentsAISBridge.framework/MediaIntentsAISBridge`](System__Library__PrivateFrameworks__MediaIntentsAISBridge.framework__MediaIntentsAISBridge.md) | 3605.14.1.11.1 | light |
| [`/System/Library/PrivateFrameworks/MediaIntentsSnippetModels.framework/MediaIntentsSnippetModels`](System__Library__PrivateFrameworks__MediaIntentsSnippetModels.framework__MediaIntentsSnippetModels.md) | 3605.14.1.11.1 | light |
| [`/System/Library/PrivateFrameworks/MediaKit.framework/MediaKit`](System__Library__PrivateFrameworks__MediaKit.framework__MediaKit.md) | 944.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MediaLibraryCore.framework/MediaLibraryCore`](System__Library__PrivateFrameworks__MediaLibraryCore.framework__MediaLibraryCore.md) | 4026.200.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/MediaML.framework/MediaML`](System__Library__PrivateFrameworks__MediaML.framework__MediaML.md) | 124.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MediaMLServices.framework/MediaMLServices`](System__Library__PrivateFrameworks__MediaMLServices.framework__MediaMLServices.md) | 124.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MediaMiningKit.framework/MediaMiningKit`](System__Library__PrivateFrameworks__MediaMiningKit.framework__MediaMiningKit.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/MediaPlatform.framework/MediaPlatform`](System__Library__PrivateFrameworks__MediaPlatform.framework__MediaPlatform.md) | 4026.200.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/MediaPlayerUI.framework/MediaPlayerUI`](System__Library__PrivateFrameworks__MediaPlayerUI.framework__MediaPlayerUI.md) | 4026.100.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/MediaRemoteDaemonServices.framework/MediaRemoteDaemonServices`](System__Library__PrivateFrameworks__MediaRemoteDaemonServices.framework__MediaRemoteDaemonServices.md) | 4026.210.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/MediaSafetyNet.framework/MediaSafetyNet`](System__Library__PrivateFrameworks__MediaSafetyNet.framework__MediaSafetyNet.md) | 74.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MediaServicesBroker.framework/MediaServicesBroker`](System__Library__PrivateFrameworks__MediaServicesBroker.framework__MediaServicesBroker.md) | 261.10.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/MediaSuggester.framework/MediaSuggester`](System__Library__PrivateFrameworks__MediaSuggester.framework__MediaSuggester.md) | 99.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MediaTokens.framework/MediaTokens`](System__Library__PrivateFrameworks__MediaTokens.framework__MediaTokens.md) | 158.200.81.21.9 | light |
| [`/System/Library/PrivateFrameworks/MedicalIDDaemon.framework/MedicalIDDaemon`](System__Library__PrivateFrameworks__MedicalIDDaemon.framework__MedicalIDDaemon.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/MedicalIDUI.framework/MedicalIDUI`](System__Library__PrivateFrameworks__MedicalIDUI.framework__MedicalIDUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/MemoryAccounting.framework/MemoryAccounting`](System__Library__PrivateFrameworks__MemoryAccounting.framework__MemoryAccounting.md) | 10.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MemoryDiagnostics.framework/MemoryDiagnostics`](System__Library__PrivateFrameworks__MemoryDiagnostics.framework__MemoryDiagnostics.md) | 369.40.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/MenstrualAlgorithmsInternal.framework/MenstrualAlgorithmsInternal`](System__Library__PrivateFrameworks__MenstrualAlgorithmsInternal.framework__MenstrualAlgorithmsInternal.md) | 151.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MentalHealth.framework/MentalHealth`](System__Library__PrivateFrameworks__MentalHealth.framework__MentalHealth.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/MentalHealthDaemon.framework/MentalHealthDaemon`](System__Library__PrivateFrameworks__MentalHealthDaemon.framework__MentalHealthDaemon.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/MentalHealthUI.framework/MentalHealthUI`](System__Library__PrivateFrameworks__MentalHealthUI.framework__MentalHealthUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/MentalHealthWidgetUI.framework/MentalHealthWidgetUI`](System__Library__PrivateFrameworks__MentalHealthWidgetUI.framework__MentalHealthWidgetUI.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/Message.framework/MailServices/IMAP.framework/IMAP`](System__Library__PrivateFrameworks__Message.framework__MailServices__IMAP.framework__IMAP.md) | 3901.200.71.21.4 | light |
| [`/System/Library/PrivateFrameworks/Message.framework/MailServices/POP.framework/POP`](System__Library__PrivateFrameworks__Message.framework__MailServices__POP.framework__POP.md) | 3901.200.71.21.4 | light |
| [`/System/Library/PrivateFrameworks/MessageDispatchCore.framework/MessageDispatchCore`](System__Library__PrivateFrameworks__MessageDispatchCore.framework__MessageDispatchCore.md) | 2027.1.4.0.0 | full |
| [`/System/Library/PrivateFrameworks/MessageLegacy.framework/MailServices/IMAP.framework/IMAP`](System__Library__PrivateFrameworks__MessageLegacy.framework__MailServices__IMAP.framework__IMAP.md) | 24.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MessageLegacy.framework/MessageLegacy`](System__Library__PrivateFrameworks__MessageLegacy.framework__MessageLegacy.md) | 24.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MessageProtection.framework/MessageProtection`](System__Library__PrivateFrameworks__MessageProtection.framework__MessageProtection.md) | 398.40.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/MessagesEscrow.framework/MessagesEscrow`](System__Library__PrivateFrameworks__MessagesEscrow.framework__MessagesEscrow.md) | 1491.200.101.21.5 | light |
| [`/System/Library/PrivateFrameworks/MessagesSettingsUI.framework/MessagesSettingsUI`](System__Library__PrivateFrameworks__MessagesSettingsUI.framework__MessagesSettingsUI.md) | 1491.200.101.21.5 | light |
| [`/System/Library/PrivateFrameworks/MessagesSupport.framework/MessagesSupport`](System__Library__PrivateFrameworks__MessagesSupport.framework__MessagesSupport.md) | 1491.200.101.21.5 | light |
| [`/System/Library/PrivateFrameworks/MetalMetrics.framework/MetalMetrics`](System__Library__PrivateFrameworks__MetalMetrics.framework__MetalMetrics.md) | 5.0.26.0.0 | full |
| [`/System/Library/PrivateFrameworks/MetricKitCore.framework/MetricKitCore`](System__Library__PrivateFrameworks__MetricKitCore.framework__MetricKitCore.md) | 369.40.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/MetricKitServices.framework/MetricKitServices`](System__Library__PrivateFrameworks__MetricKitServices.framework__MetricKitServices.md) | 369.40.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/MetricKitSource.framework/MetricKitSource`](System__Library__PrivateFrameworks__MetricKitSource.framework__MetricKitSource.md) | 369.40.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/MetricMeasurement.framework/MetricMeasurement`](System__Library__PrivateFrameworks__MetricMeasurement.framework__MetricMeasurement.md) | 369.40.2.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend26.dylib`](usr__lib__objc__libobjcMsgSend26.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MLIR_ML.framework/MLIR_ML`](System__Library__PrivateFrameworks__MLIR_ML.framework__MLIR_ML.md) | 7.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync`](System__Library__PrivateFrameworks__MessagesCloudSync.framework__MessagesCloudSync.md) | 1491.200.101.21.5 | light |
| [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) | 383.1.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/MetricsKit.framework/MetricsKit`](System__Library__PrivateFrameworks__MetricsKit.framework__MetricsKit.md) | 2.8.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/MicroFindMy.framework/MicroFindMy`](System__Library__PrivateFrameworks__MicroFindMy.framework__MicroFindMy.md) | 12.31.7.12.3 | light |
| [`/System/Library/PrivateFrameworks/MicroLocation.framework/MicroLocation`](System__Library__PrivateFrameworks__MicroLocation.framework__MicroLocation.md) | 117.0.1.1.8 | light |
| [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) | 117.0.1.1.8 | full |
| [`/System/Library/PrivateFrameworks/MicroLocationKit.framework/MicroLocationKit`](System__Library__PrivateFrameworks__MicroLocationKit.framework__MicroLocationKit.md) | 117.0.1.1.8 | light |
| [`/System/Library/PrivateFrameworks/MicroLocationUtilities.framework/MicroLocationUtilities`](System__Library__PrivateFrameworks__MicroLocationUtilities.framework__MicroLocationUtilities.md) | 117.0.1.1.8 | light |
| [`/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit`](System__Library__PrivateFrameworks__MigrationKit.framework__MigrationKit.md) | 1441.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/MilAneflow.framework/MilAneflow`](System__Library__PrivateFrameworks__MilAneflow.framework__MilAneflow.md) | 1.104.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/MobileAccessoryUpdater`](System__Library__PrivateFrameworks__MobileAccessoryUpdater.framework__MobileAccessoryUpdater.md) | 1587.40.33.0.0 | full |
| [`/System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation`](System__Library__PrivateFrameworks__MobileActivation.framework__MobileActivation.md) | 1145.40.5.0.4 | light |
| [`/System/Library/PrivateFrameworks/MobileAssetExclaveServices.framework/MobileAssetExclaveServices`](System__Library__PrivateFrameworks__MobileAssetExclaveServices.framework__MobileAssetExclaveServices.md) | 2215.52.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/MobileAssetUpdater.framework/MobileAssetUpdater`](System__Library__PrivateFrameworks__MobileAssetUpdater.framework__MobileAssetUpdater.md) | 1587.40.33.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileContainerManager.framework/MobileContainerManager`](System__Library__PrivateFrameworks__MobileContainerManager.framework__MobileContainerManager.md) | 833.40.18.0.1 | light |
| [`/System/Library/PrivateFrameworks/MobileDeviceLink.framework/MobileDeviceLink`](System__Library__PrivateFrameworks__MobileDeviceLink.framework__MobileDeviceLink.md) | 307.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileIcons.framework/MobileIcons`](System__Library__PrivateFrameworks__MobileIcons.framework__MobileIcons.md) | 793.1.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileIdentityServiceUI.framework/MobileIdentityServiceUI`](System__Library__PrivateFrameworks__MobileIdentityServiceUI.framework__MobileIdentityServiceUI.md) | 487.0.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate`](System__Library__PrivateFrameworks__MobileInBoxUpdate.framework__MobileInBoxUpdate.md) | 274.40.17.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileLookup.framework/MobileLookup`](System__Library__PrivateFrameworks__MobileLookup.framework__MobileLookup.md) | 22.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileMailUI.framework/MobileMailUI`](System__Library__PrivateFrameworks__MobileMailUI.framework__MobileMailUI.md) | 3901.200.71.21.4 | light |
| [`/System/Library/PrivateFrameworks/MobileMulticastTransfer.framework/MobileMulticastTransfer`](System__Library__PrivateFrameworks__MobileMulticastTransfer.framework__MobileMulticastTransfer.md) | 274.40.17.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileObliteration.framework/MobileObliteration`](System__Library__PrivateFrameworks__MobileObliteration.framework__MobileObliteration.md) | 402.40.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileSafari.framework/PlugIns/Safari.wkbundle/Safari`](System__Library__PrivateFrameworks__MobileSafari.framework__PlugIns__Safari.wkbundle__Safari.md) | 7625.2.8.21.6 | light |
| [`/System/Library/PrivateFrameworks/MobileStorage.framework/MobileStorage`](System__Library__PrivateFrameworks__MobileStorage.framework__MobileStorage.md) | 352.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit`](System__Library__PrivateFrameworks__MobileStoreDemoKit.framework__MobileStoreDemoKit.md) | 1871.52.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileStoreDemoSetupUI.framework/MobileStoreDemoSetupUI`](System__Library__PrivateFrameworks__MobileStoreDemoSetupUI.framework__MobileStoreDemoSetupUI.md) | 1871.52.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileStoreUI.framework/MobileStoreUI`](System__Library__PrivateFrameworks__MobileStoreUI.framework__MobileStoreUI.md) | 1203.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileSync.framework/MobileSync`](System__Library__PrivateFrameworks__MobileSync.framework__MobileSync.md) | 1025.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices`](System__Library__PrivateFrameworks__MobileSystemServices.framework__MobileSystemServices.md) | 24.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileTimerUI.framework/MobileTimerUI`](System__Library__PrivateFrameworks__MobileTimerUI.framework__MobileTimerUI.md) | 2333.2.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileTimerUISupport.framework/MobileTimerUISupport`](System__Library__PrivateFrameworks__MobileTimerUISupport.framework__MobileTimerUISupport.md) | 2333.2.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi`](System__Library__PrivateFrameworks__MobileWiFi.framework__MobileWiFi.md) | 2029.9.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/ModelInterfaces.framework/ModelInterfaces`](System__Library__PrivateFrameworks__ModelInterfaces.framework__ModelInterfaces.md) | 441.26.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/ModelManagerExclaveInternal.framework/ModelManagerExclaveInternal`](System__Library__PrivateFrameworks__ModelManagerExclaveInternal.framework__ModelManagerExclaveInternal.md) | 714.40.86.0.0 | full |
| [`/System/Library/PrivateFrameworks/ModelMonitoringLighthouse.framework/ModelMonitoringLighthouse`](System__Library__PrivateFrameworks__ModelMonitoringLighthouse.framework__ModelMonitoringLighthouse.md) | 99.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/Moments.framework/Moments`](System__Library__PrivateFrameworks__Moments.framework__Moments.md) | 502.0.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/MomentsData.framework/MomentsData`](System__Library__PrivateFrameworks__MomentsData.framework__MomentsData.md) | 502.0.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/MomentsIntelligence.framework/MomentsIntelligence`](System__Library__PrivateFrameworks__MomentsIntelligence.framework__MomentsIntelligence.md) | 502.0.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/MomentsOnboardingAndSettings.framework/MomentsOnboardingAndSettings`](System__Library__PrivateFrameworks__MomentsOnboardingAndSettings.framework__MomentsOnboardingAndSettings.md) | 502.0.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/Morpheus.framework/Morpheus`](System__Library__PrivateFrameworks__Morpheus.framework__Morpheus.md) | 47.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MorpheusExtensions.framework/MorpheusExtensions`](System__Library__PrivateFrameworks__MorpheusExtensions.framework__MorpheusExtensions.md) | 47.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MorphunSwift.framework/MorphunSwift`](System__Library__PrivateFrameworks__MorphunSwift.framework__MorphunSwift.md) | 3600.36.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/MotionHealthAlgorithms.framework/MotionHealthAlgorithms`](System__Library__PrivateFrameworks__MotionHealthAlgorithms.framework__MotionHealthAlgorithms.md) | 3187.0.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/MotionSensorLogging.framework/MotionSensorLogging`](System__Library__PrivateFrameworks__MotionSensorLogging.framework__MotionSensorLogging.md) | 3187.0.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/MultitouchSessionFilterSupport.framework/MultitouchSessionFilterSupport`](System__Library__PrivateFrameworks__MultitouchSessionFilterSupport.framework__MultitouchSessionFilterSupport.md) | 10110.4.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MultitouchSupport.framework/MultitouchSupport`](System__Library__PrivateFrameworks__MultitouchSupport.framework__MultitouchSupport.md) | 10110.4.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/MusicCarDisplayUI.framework/MusicCarDisplayUI`](System__Library__PrivateFrameworks__MusicCarDisplayUI.framework__MusicCarDisplayUI.md) | 4026.210.2.3.0 | full |
| [`/System/Library/PrivateFrameworks/MusicKitPlaybackSupport.framework/MusicKitPlaybackSupport`](System__Library__PrivateFrameworks__MusicKitPlaybackSupport.framework__MusicKitPlaybackSupport.md) | 4026.210.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/MusicSettingsSupport.framework/MusicSettingsSupport`](System__Library__PrivateFrameworks__MusicSettingsSupport.framework__MusicSettingsSupport.md) | 4026.210.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/MusicStoreUI.framework/MusicStoreUI`](System__Library__PrivateFrameworks__MusicStoreUI.framework__MusicStoreUI.md) | 1203.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/NANDFileAlignment.framework/NANDFileAlignment`](System__Library__PrivateFrameworks__NANDFileAlignment.framework__NANDFileAlignment.md) | 849.40.17.0.0 | light |
| [`/System/Library/PrivateFrameworks/NANDInfo.framework/NANDInfo`](System__Library__PrivateFrameworks__NANDInfo.framework__NANDInfo.md) | 849.40.17.0.0 | light |
| [`/System/Library/PrivateFrameworks/NCLaunchStats.framework/NCLaunchStats`](System__Library__PrivateFrameworks__NCLaunchStats.framework__NCLaunchStats.md) | 2467.52.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/NDOUI.framework/NDOUI`](System__Library__PrivateFrameworks__NDOUI.framework__NDOUI.md) | 624.40.22.0.0 | light |
| [`/System/Library/PrivateFrameworks/NLP.framework/NLP`](System__Library__PrivateFrameworks__NLP.framework__NLP.md) | 237.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NLPLearner.framework/NLPLearner`](System__Library__PrivateFrameworks__NLPLearner.framework__NLPLearner.md) | 70.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NPTKit.framework/NPTKit`](System__Library__PrivateFrameworks__NPTKit.framework__NPTKit.md) | 202.26.4.2.0 | light |
| [`/System/Library/PrivateFrameworks/NSPredicateSecurityPolicy.framework/NSPredicateSecurityPolicy`](System__Library__PrivateFrameworks__NSPredicateSecurityPolicy.framework__NSPredicateSecurityPolicy.md) | 10.40.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/NTKUltraBezel.framework/NTKUltraBezel`](System__Library__PrivateFrameworks__NTKUltraBezel.framework__NTKUltraBezel.md) | 2483.561.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/NameRecognition.framework/NameRecognition`](System__Library__PrivateFrameworks__NameRecognition.framework__NameRecognition.md) | 3245.8.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoAppRegistry.framework/NanoAppRegistry`](System__Library__PrivateFrameworks__NanoAppRegistry.framework__NanoAppRegistry.md) | 71.0.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoAudioControl.framework/NanoAudioControl`](System__Library__PrivateFrameworks__NanoAudioControl.framework__NanoAudioControl.md) | 2024.200.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoBackup.framework/NanoBackup`](System__Library__PrivateFrameworks__NanoBackup.framework__NanoBackup.md) | 135.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoComplicationSettings.framework/NanoComplicationSettings`](System__Library__PrivateFrameworks__NanoComplicationSettings.framework__NanoComplicationSettings.md) | 19.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoControlCenter.framework/NanoControlCenter`](System__Library__PrivateFrameworks__NanoControlCenter.framework__NanoControlCenter.md) | 104.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoFaceGallery.framework/NanoFaceGallery`](System__Library__PrivateFrameworks__NanoFaceGallery.framework__NanoFaceGallery.md) | 2483.561.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoHomeIntents.framework/NanoHomeIntents`](System__Library__PrivateFrameworks__NanoHomeIntents.framework__NanoHomeIntents.md) | 961.2.12.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoHomeScreenServices.framework/NanoHomeScreenServices`](System__Library__PrivateFrameworks__NanoHomeScreenServices.framework__NanoHomeScreenServices.md) | 350.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoHomeScreenUIServices.framework/NanoHomeScreenUIServices`](System__Library__PrivateFrameworks__NanoHomeScreenUIServices.framework__NanoHomeScreenUIServices.md) | 350.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoLeash.framework/NanoLeash`](System__Library__PrivateFrameworks__NanoLeash.framework__NanoLeash.md) | 142.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoMailCompanionUI.framework/NanoMailCompanionUI`](System__Library__PrivateFrameworks__NanoMailCompanionUI.framework__NanoMailCompanionUI.md) | 867.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoMailKitServer.framework/NanoMailKitServer`](System__Library__PrivateFrameworks__NanoMailKitServer.framework__NanoMailKitServer.md) | 867.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoMediaAPI.framework/NanoMediaAPI`](System__Library__PrivateFrameworks__NanoMediaAPI.framework__NanoMediaAPI.md) | 2024.200.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoMediaBridgeUI.framework/NanoMediaBridgeUI`](System__Library__PrivateFrameworks__NanoMediaBridgeUI.framework__NanoMediaBridgeUI.md) | 2024.200.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoMediaRemote.framework/NanoMediaRemote`](System__Library__PrivateFrameworks__NanoMediaRemote.framework__NanoMediaRemote.md) | 2024.200.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoMusicSync.framework/NanoMusicSync`](System__Library__PrivateFrameworks__NanoMusicSync.framework__NanoMusicSync.md) | 2024.200.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoNetAppsUI.framework/NanoNetAppsUI`](System__Library__PrivateFrameworks__NanoNetAppsUI.framework__NanoNetAppsUI.md) | 8.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit`](System__Library__PrivateFrameworks__NanoPassKit.framework__NanoPassKit.md) | 1355.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoPassKitUI.framework/NanoPassKitUI`](System__Library__PrivateFrameworks__NanoPassKitUI.framework__NanoPassKitUI.md) | 1355.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoPhotosCore.framework/NanoPhotosCore`](System__Library__PrivateFrameworks__NanoPhotosCore.framework__NanoPhotosCore.md) | 2024.100.17.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoResourceGrabber.framework/NanoResourceGrabber`](System__Library__PrivateFrameworks__NanoResourceGrabber.framework__NanoResourceGrabber.md) | 118.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoSmartStackControlUI.framework/NanoSmartStackControlUI`](System__Library__PrivateFrameworks__NanoSmartStackControlUI.framework__NanoSmartStackControlUI.md) | 350.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoSmartStackProactiveSuggestions.framework/NanoSmartStackProactiveSuggestions`](System__Library__PrivateFrameworks__NanoSmartStackProactiveSuggestions.framework__NanoSmartStackProactiveSuggestions.md) | 350.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoSystemSettings.framework/NanoSystemSettings`](System__Library__PrivateFrameworks__NanoSystemSettings.framework__NanoSystemSettings.md) | 383.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoTimeKitCompanion.framework/NanoTimeKitCompanion`](System__Library__PrivateFrameworks__NanoTimeKitCompanion.framework__NanoTimeKitCompanion.md) | 2483.561.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoUniverse.framework/NanoUniverse`](System__Library__PrivateFrameworks__NanoUniverse.framework__NanoUniverse.md) | 46.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoWeatherComplicationsCompanion.framework/NanoWeatherComplicationsCompanion`](System__Library__PrivateFrameworks__NanoWeatherComplicationsCompanion.framework__NanoWeatherComplicationsCompanion.md) | 1169.2.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/NanoWeatherKitUICompanion.framework/NanoWeatherKitUICompanion`](System__Library__PrivateFrameworks__NanoWeatherKitUICompanion.framework__NanoWeatherKitUICompanion.md) | 1169.2.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/NearFieldAccessory.framework/NearFieldAccessory`](System__Library__PrivateFrameworks__NearFieldAccessory.framework__NearFieldAccessory.md) | 371.8.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/NearFieldPrivateServices`](System__Library__PrivateFrameworks__NearFieldPrivateServices.framework__NearFieldPrivateServices.md) | 371.8.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NearFieldUI.framework/NearFieldUI`](System__Library__PrivateFrameworks__NearFieldUI.framework__NearFieldUI.md) | 371.8.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/NeighborhoodActivityConduit`](System__Library__PrivateFrameworks__NeighborhoodActivityConduit.framework__NeighborhoodActivityConduit.md) | 1628.200.81.21.4 | light |
| [`/System/Library/PrivateFrameworks/SafariSafeBrowsing.framework/SafariSafeBrowsing`](System__Library__PrivateFrameworks__SafariSafeBrowsing.framework__SafariSafeBrowsing.md) | 625.2.8.21.5 | light |
| [`/System/Library/PrivateFrameworks/NeighborhoodActivityConduitIntents.framework/NeighborhoodActivityConduitIntents`](System__Library__PrivateFrameworks__NeighborhoodActivityConduitIntents.framework__NeighborhoodActivityConduitIntents.md) | 1628.200.81.21.4 | light |
| [`/System/Library/PrivateFrameworks/NetAppsUtilitiesUI.framework/NetAppsUtilitiesUI`](System__Library__PrivateFrameworks__NetAppsUtilitiesUI.framework__NetAppsUtilitiesUI.md) | 108.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/Netrb.framework/Netrb`](System__Library__PrivateFrameworks__Netrb.framework__Netrb.md) | 406.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NetworkInfo.framework/NetworkInfo`](System__Library__PrivateFrameworks__NetworkInfo.framework__NetworkInfo.md) | 227.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NetworkQuality.framework/NetworkQuality`](System__Library__PrivateFrameworks__NetworkQuality.framework__NetworkQuality.md) | 227.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay`](System__Library__PrivateFrameworks__NetworkRelay.framework__NetworkRelay.md) | 914.42.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/NetworkScore.framework/NetworkScore`](System__Library__PrivateFrameworks__NetworkScore.framework__NetworkScore.md) | 59.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NetworkStatistics.framework/NetworkStatistics`](System__Library__PrivateFrameworks__NetworkStatistics.framework__NetworkStatistics.md) | 279.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NeutrinoKit.framework/NeutrinoKit`](System__Library__PrivateFrameworks__NeutrinoKit.framework__NeutrinoKit.md) | 916.62.154.0.0 | light |
| [`/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/NewDeviceOutreach`](System__Library__PrivateFrameworks__NewDeviceOutreach.framework__NewDeviceOutreach.md) | 624.40.22.0.0 | light |
| [`/System/Library/PrivateFrameworks/NewDeviceOutreachUI.framework/NewDeviceOutreachUI`](System__Library__PrivateFrameworks__NewDeviceOutreachUI.framework__NewDeviceOutreachUI.md) | 624.40.22.0.0 | light |
| [`/System/Library/PrivateFrameworks/NewsAnalyticsUpload.framework/NewsAnalyticsUpload`](System__Library__PrivateFrameworks__NewsAnalyticsUpload.framework__NewsAnalyticsUpload.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NewsDaemon.framework/NewsDaemon`](System__Library__PrivateFrameworks__NewsDaemon.framework__NewsDaemon.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NewsEngagement.framework/NewsEngagement`](System__Library__PrivateFrameworks__NewsEngagement.framework__NewsEngagement.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NewsEngagementCollector.framework/NewsEngagementCollector`](System__Library__PrivateFrameworks__NewsEngagementCollector.framework__NewsEngagementCollector.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NewsFoundation.framework/NewsFoundation`](System__Library__PrivateFrameworks__NewsFoundation.framework__NewsFoundation.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NewsKit.framework/NewsKit`](System__Library__PrivateFrameworks__NewsKit.framework__NewsKit.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NewsServices.framework/NewsServices`](System__Library__PrivateFrameworks__NewsServices.framework__NewsServices.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NewsServicesInternal.framework/NewsServicesInternal`](System__Library__PrivateFrameworks__NewsServicesInternal.framework__NewsServicesInternal.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NewsToday.framework/NewsToday`](System__Library__PrivateFrameworks__NewsToday.framework__NewsToday.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NewsUI.framework/NewsUI`](System__Library__PrivateFrameworks__NewsUI.framework__NewsUI.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NewsURLBucket.framework/NewsURLBucket`](System__Library__PrivateFrameworks__NewsURLBucket.framework__NewsURLBucket.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NewsURLResolution.framework/NewsURLResolution`](System__Library__PrivateFrameworks__NewsURLResolution.framework__NewsURLResolution.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/Nexus.framework/Nexus`](System__Library__PrivateFrameworks__Nexus.framework__Nexus.md) | 910.31.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NexusDaemon.framework/NexusDaemon`](System__Library__PrivateFrameworks__NexusDaemon.framework__NexusDaemon.md) | 910.31.0.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend27.dylib`](usr__lib__objc__libobjcMsgSend27.dylib.md) | 973.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NewsTransport.framework/NewsTransport`](System__Library__PrivateFrameworks__NewsTransport.framework__NewsTransport.md) | 5971.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NightingaleTraining.framework/NightingaleTraining`](System__Library__PrivateFrameworks__NightingaleTraining.framework__NightingaleTraining.md) | 47.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NotTheStoreKitUIFrameworkYouAreLookingFor.framework/NotTheStoreKitUIFrameworkYouAreLookingFor`](System__Library__PrivateFrameworks__NotTheStoreKitUIFrameworkYouAreLookingFor.framework__NotTheStoreKitUIFrameworkYouAreLookingFor.md) | 1.4.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/Notes.framework/Notes`](System__Library__PrivateFrameworks__Notes.framework__Notes.md) | 3001.42.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/NotesAnalytics.framework/NotesAnalytics`](System__Library__PrivateFrameworks__NotesAnalytics.framework__NotesAnalytics.md) | 3001.42.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/NotesPreviewKit.framework/NotesPreviewKit`](System__Library__PrivateFrameworks__NotesPreviewKit.framework__NotesPreviewKit.md) | 3001.42.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/NotesSiriUI.framework/NotesSiriUI`](System__Library__PrivateFrameworks__NotesSiriUI.framework__NotesSiriUI.md) | 3001.42.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/NumberAdder.framework/NumberAdder`](System__Library__PrivateFrameworks__NumberAdder.framework__NumberAdder.md) | 5.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/NutritionCore.framework/NutritionCore`](System__Library__PrivateFrameworks__NutritionCore.framework__NutritionCore.md) | 30.40.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/NutritionUICore.framework/NutritionUICore`](System__Library__PrivateFrameworks__NutritionUICore.framework__NutritionUICore.md) | 30.40.6.0.0 | light |
| [`/System/Library/PrivateFrameworks/OAuth.framework/OAuth`](System__Library__PrivateFrameworks__OAuth.framework__OAuth.md) | 32.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ODCurareAnalysis.framework/ODCurareAnalysis`](System__Library__PrivateFrameworks__ODCurareAnalysis.framework__ODCurareAnalysis.md) | 3500.3.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ODCurareEvaluationAndReporting.framework/ODCurareEvaluationAndReporting`](System__Library__PrivateFrameworks__ODCurareEvaluationAndReporting.framework__ODCurareEvaluationAndReporting.md) | 3500.3.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ODIE.framework/Frameworks/libODIECompiler.dylib`](System__Library__PrivateFrameworks__ODIE.framework__Frameworks__libODIECompiler.dylib.md) | 3605.6.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/ODIE.framework/ODIE`](System__Library__PrivateFrameworks__ODIE.framework__ODIE.md) | 3605.6.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/ODIEDelegates.framework/ODIEDelegates`](System__Library__PrivateFrameworks__ODIEDelegates.framework__ODIEDelegates.md) | 3605.6.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/ODT.framework/ODT`](System__Library__PrivateFrameworks__ODT.framework__ODT.md) | 31.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/OSASubmissionClient.framework/OSASubmissionClient`](System__Library__PrivateFrameworks__OSASubmissionClient.framework__OSASubmissionClient.md) | 1056.40.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/OSASyncProxyClient.framework/OSASyncProxyClient`](System__Library__PrivateFrameworks__OSASyncProxyClient.framework__OSASyncProxyClient.md) | 1056.40.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/OSAnalyticsPrivate.framework/OSAnalyticsPrivate`](System__Library__PrivateFrameworks__OSAnalyticsPrivate.framework__OSAnalyticsPrivate.md) | 1056.40.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility`](System__Library__PrivateFrameworks__OSEligibility.framework__OSEligibility.md) | 446.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence`](System__Library__PrivateFrameworks__OSIntelligence.framework__OSIntelligence.md) | 288.40.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/OTSVG.framework/OTSVG`](System__Library__PrivateFrameworks__OTSVG.framework__OTSVG.md) | 910.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ObjectUnderstanding.framework/ObjectUnderstanding`](System__Library__PrivateFrameworks__ObjectUnderstanding.framework__ObjectUnderstanding.md) | 4.3.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/OfficeImport.framework/OfficeImport`](System__Library__PrivateFrameworks__OfficeImport.framework__OfficeImport.md) | 322.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/OmniSearch.framework/OmniSearch`](System__Library__PrivateFrameworks__OmniSearch.framework__OmniSearch.md) | 3605.32.1.11.5 | light |
| [`/System/Library/PrivateFrameworks/OmniSearchClient.framework/OmniSearchClient`](System__Library__PrivateFrameworks__OmniSearchClient.framework__OmniSearchClient.md) | 3605.32.1.11.5 | light |
| [`/System/Library/PrivateFrameworks/OmniSearchTypes.framework/OmniSearchTypes`](System__Library__PrivateFrameworks__OmniSearchTypes.framework__OmniSearchTypes.md) | 3605.32.1.11.5 | light |
| [`/System/Library/PrivateFrameworks/OnDeviceDaemon.framework/OnDeviceDaemon`](System__Library__PrivateFrameworks__OnDeviceDaemon.framework__OnDeviceDaemon.md) | 3.1.15.0.0 | light |
| [`/System/Library/PrivateFrameworks/OnDeviceFoundation.framework/OnDeviceFoundation`](System__Library__PrivateFrameworks__OnDeviceFoundation.framework__OnDeviceFoundation.md) | 3.1.15.0.0 | light |
| [`/System/Library/PrivateFrameworks/OnDeviceStorage.framework/OnDeviceStorage`](System__Library__PrivateFrameworks__OnDeviceStorage.framework__OnDeviceStorage.md) | 3.1.15.0.0 | light |
| [`/System/Library/PrivateFrameworks/OpenAPIRuntimeInternal.framework/OpenAPIRuntimeInternal`](System__Library__PrivateFrameworks__OpenAPIRuntimeInternal.framework__OpenAPIRuntimeInternal.md) | 1.8.3.1.0 | light |
| [`/System/Library/PrivateFrameworks/OpenAPIURLSessionInternal.framework/OpenAPIURLSessionInternal`](System__Library__PrivateFrameworks__OpenAPIURLSessionInternal.framework__OpenAPIURLSessionInternal.md) | 1.1.0.2.0 | light |
| [`/System/Library/PrivateFrameworks/Osprey.framework/Osprey`](System__Library__PrivateFrameworks__Osprey.framework__Osprey.md) | 3500.5.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/PBBridgeSupport.framework/PBBridgeSupport`](System__Library__PrivateFrameworks__PBBridgeSupport.framework__PBBridgeSupport.md) | 1373.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/PCCAgentClient.framework/PCCAgentClient`](System__Library__PrivateFrameworks__PCCAgentClient.framework__PCCAgentClient.md) | 65.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/PCCAgentClientCommon.framework/PCCAgentClientCommon`](System__Library__PrivateFrameworks__PCCAgentClientCommon.framework__PCCAgentClientCommon.md) | 65.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/PDS.framework/PDS`](System__Library__PrivateFrameworks__PDS.framework__PDS.md) | 2003.200.71.2.4 | light |
| [`/System/Library/PrivateFrameworks/PDSAgent.framework/PDSAgent`](System__Library__PrivateFrameworks__PDSAgent.framework__PDSAgent.md) | 2003.200.71.2.4 | light |
| [`/System/Library/PrivateFrameworks/PIRGeoProtos.framework/PIRGeoProtos`](System__Library__PrivateFrameworks__PIRGeoProtos.framework__PIRGeoProtos.md) | 2465.1.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/PLSnapshot.framework/PLSnapshot`](System__Library__PrivateFrameworks__PLSnapshot.framework__PLSnapshot.md) | 3486.52.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/PacketFilter-embedded.framework/PacketFilter-embedded`](System__Library__PrivateFrameworks__PacketFilter-embedded.framework__PacketFilter-embedded.md) | 120.40.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/PacketFilter.framework/PacketFilter`](System__Library__PrivateFrameworks__PacketFilter.framework__PacketFilter.md) | 120.40.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/PacketParser.framework/PacketParser`](System__Library__PrivateFrameworks__PacketParser.framework__PacketParser.md) | 145.2.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/PairedUnlock.framework/PairedUnlock`](System__Library__PrivateFrameworks__PairedUnlock.framework__PairedUnlock.md) | 184.4.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/PairingProximity.framework/PairingProximity`](System__Library__PrivateFrameworks__PairingProximity.framework__PairingProximity.md) | 1373.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/PanicHelper.framework/PanicHelper`](System__Library__PrivateFrameworks__PanicHelper.framework__PanicHelper.md) | 41.40.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/PanicProcessingSupport.framework/PanicProcessingSupport`](System__Library__PrivateFrameworks__PanicProcessingSupport.framework__PanicProcessingSupport.md) | 41.40.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/ParavirtualizedANE.framework/ParavirtualizedANE`](System__Library__PrivateFrameworks__ParavirtualizedANE.framework__ParavirtualizedANE.md) | 382.101.2.0.0 | full |
| `/System/Library/PrivateFrameworks/ParsecModel.framework/ParsecModel` | 3605.27.1.11.1 | not generated |
| `/System/Library/PrivateFrameworks/ParsecSubscriptionServiceSupport.framework/ParsecSubscriptionServiceSupport` | 3605.27.1.11.1 | not generated |
| `/System/Library/PrivateFrameworks/ParsingInternal.framework/ParsingInternal` | 5027.1.6.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PartnerVisualSearch.framework/PartnerVisualSearch` | 297.12.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PassKitServices.framework/PassKitServices` | 1696.2.9.2.0 | not generated |
| `/System/Library/PrivateFrameworks/PasscodeAndBiometricsSettings.framework/PasscodeAndBiometricsSettings` | 40.2.3.100.0 | not generated |
| `/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI` | 7625.2.8.21.6 | not generated |
| `/System/Library/PrivateFrameworks/Pasteboard.framework/Pasteboard` | 9127.1.12.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PaymentUI.framework/PaymentUI` | 1696.2.9.2.0 | not generated |
| `/System/Library/PrivateFrameworks/PebblePlayCore.framework/PebblePlayCore` | 164.2.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PebblePlayDaemon.framework/PebblePlayDaemon` | 164.2.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PebblePlayFeatures.framework/PebblePlayFeatures` | 164.2.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PebblePlayKit.framework/PebblePlayKit` | 164.2.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PegasusPersistence.framework/PegasusPersistence` | 3605.27.1.11.1 | not generated |
| [`/System/Library/PrivateFrameworks/PencilPairing.framework/PencilPairing`](System__Library__PrivateFrameworks__PencilPairing.framework__PencilPairing.md) | 227.1.1.102.0 | full |
| [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) | 227.1.1.102.0 | full |
| `/System/Library/PrivateFrameworks/PeopleUI.framework/PeopleUI` | 148.125.5.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PeopleUIInternal.framework/PeopleUIInternal` | 148.125.5.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PerfPowerMetricMonitor.framework/PerfPowerMetricMonitor` | 3486.52.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PerfPowerServicesMetadata.framework/PerfPowerServicesMetadata` | 3486.52.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader` | 3486.52.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PerformanceControlKit.framework/PerformanceControlKit` | 1794.40.23.0.1 | not generated |
| `/System/Library/PrivateFrameworks/PerformanceTrace.framework/PerformanceTrace` | 268.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PeridotDepth.framework/PeridotDepth` | 52.0.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PersonaKit.framework/PersonaKit` | 1372.200.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PersonaUI.framework/PersonaUI` | 1372.200.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio` | 543.2.5.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PersonalIntelligenceCore.framework/PersonalIntelligenceCore` | 1354.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/PersonalizedSensing` | 502.0.8.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Phoenix.framework/Phoenix` | 3245.8.9.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PhoneKit.framework/PhoneKit` | 158.200.81.21.9 | not generated |
| `/System/Library/PrivateFrameworks/PhoneNumberResolver.framework/PhoneNumberResolver` | 40.32.10.16.1 | not generated |
| `/System/Library/PrivateFrameworks/PhoneNumbers.framework/PhoneNumbers` | 158.200.81.21.9 | not generated |
| `/System/Library/PrivateFrameworks/PhoneSnippetUI.framework/PhoneSnippetUI` | 3605.27.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PhotosEditing.framework/PhotosEditing` | 916.62.154.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PhotosFaceCore.framework/PhotosFaceCore` | 98.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PhotosFaceLayout.framework/PhotosFaceLayout` | 98.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PhotosFaceLayoutCore.framework/PhotosFaceLayoutCore` | 98.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PhotosImagingFoundation.framework/PhotosImagingFoundation` | 916.62.154.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PhotosKnowledgeGraph.framework/PhotosKnowledgeGraph` | 916.62.154.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PhotosMediaFoundation.framework/PhotosMediaFoundation` | 916.62.154.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PhotosPosterCore.framework/PhotosPosterCore` | 916.62.154.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PhotosRendering.framework/PhotosRendering` | 916.62.154.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PhotosSearchClient.framework/PhotosSearchClient` | 99.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PhotosSpatialMedia.framework/PhotosSpatialMedia` | 916.62.154.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PhotosSpatialMediaCore.framework/PhotosSpatialMediaCore` | 916.62.154.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PhotosSpatialMediaEditing.framework/PhotosSpatialMediaEditing` | 916.62.154.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PhotosUIComponents.framework/PhotosUIComponents` | 916.62.154.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PhotosensitivityProcessing.framework/PhotosensitivityProcessing` | 241.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PhysicsKit.framework/PhysicsKit` | 43.0.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Planks.framework/Planks` | 1.7.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO` | 643.40.34.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PlatformSSOCore.framework/PlatformSSOCore` | 643.40.34.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PnROnDeviceFramework.framework/PnROnDeviceFramework` | 3605.3.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PodcastsKit.framework/PodcastsKit` | 4027.210.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PointerUISystemServices.framework/PointerUISystemServices` | 172.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PoirotAnalytics.framework/PoirotAnalytics` | 3605.11.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Polaris.framework/Polaris` | 256.0.5.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PolarisBufferService.framework/PolarisBufferService` | 256.0.5.0.0 | not generated |
| [`/System/Library/PrivateFrameworks/PolarisExclaveSupport.framework/PolarisExclaveSupport`](System__Library__PrivateFrameworks__PolarisExclaveSupport.framework__PolarisExclaveSupport.md) | 256.0.5.0.0 | full |
| [`/System/Library/PrivateFrameworks/PolarisExclaveTestClientSupport.framework/PolarisExclaveTestClientSupport`](System__Library__PrivateFrameworks__PolarisExclaveTestClientSupport.framework__PolarisExclaveTestClientSupport.md) | 256.0.5.0.0 | full |
| `/System/Library/PrivateFrameworks/PolarisGraph.framework/PolarisGraph` | 256.0.5.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PolarisRuntime.framework/PolarisRuntime` | 256.0.5.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PolarisSwift.framework/PolarisSwift` | 256.0.5.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PolarisSystemGraph.framework/PolarisSystemGraph` | 256.0.5.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PortraitCore.framework/PortraitCore` | 560.40.5.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PostSiriEngagement.framework/PostSiriEngagement` | 3605.17.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PosterBoardUI.framework/PosterBoardUI` | 355.2.12.0.4 | not generated |
| `/System/Library/PrivateFrameworks/PosterFuturesKit.framework/PosterFuturesKit` | 355.2.12.0.4 | not generated |
| `/System/Library/PrivateFrameworks/PosterLegibilityKit.framework/PosterLegibilityKit` | 355.2.12.0.4 | not generated |
| `/System/Library/PrivateFrameworks/PosterModel.framework/PosterModel` | 355.2.12.0.4 | not generated |
| `/System/Library/PrivateFrameworks/PosterPlatformSupport.framework/PosterPlatformSupport` | 355.2.12.0.4 | not generated |
| `/System/Library/PrivateFrameworks/PowerExceptions_ClientFramework.framework/PowerExceptions_ClientFramework` | 177.40.5.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PowerExceptions_PushTopicLimits.framework/PowerExceptions_PushTopicLimits` | 177.40.5.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PowerExperience.framework/PowerExperience` | 182.40.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI` | 753.40.10.0.0 | not generated |
| [`/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting`](System__Library__PrivateFrameworks__PowerlogAccounting.framework__PowerlogAccounting.md) | 3486.52.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/PowerlogControl.framework/PowerlogControl`](System__Library__PrivateFrameworks__PowerlogControl.framework__PowerlogControl.md) | 3486.52.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/PowerlogDatabaseReader.framework/PowerlogDatabaseReader`](System__Library__PrivateFrameworks__PowerlogDatabaseReader.framework__PowerlogDatabaseReader.md) | 3486.52.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators`](System__Library__PrivateFrameworks__PowerlogFullOperators.framework__PowerlogFullOperators.md) | 3486.52.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) | 3486.52.2.0.0 | full |
| `/System/Library/PrivateFrameworks/PreviewShellKit.framework/PreviewShellKit` | 24.20.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PreviewsFoundationOS.framework/PreviewsFoundationOS` | 24.20.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PreviewsInjection.framework/PreviewsInjection` | 24.20.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PreviewsMessagingOS.framework/PreviewsMessagingOS` | 24.20.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/PreviewsOSSupport` | 24.20.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PreviewsOSSupportUI.framework/PreviewsOSSupportUI` | 24.20.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PreviewsServices.framework/PreviewsServices` | 24.20.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PreviewsServicesUI.framework/PreviewsServicesUI` | 24.20.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PriMLETL.framework/PriMLETL` | 47.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PriMLFoundation.framework/PriMLFoundation` | 47.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PrintKit.framework/PrintKit` | 327.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PrintKitUI.framework/PrintKitUI` | 97.5.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PrivacyDisclosureCore.framework/PrivacyDisclosureCore` | 53.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PrivacyDisclosureUI.framework/PrivacyDisclosureUI` | 53.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PrivacyPolicy.framework/PrivacyPolicy` | 8.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/PrivateCloudCompute` | 2570.40.41.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning` | 47.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PrivateSearchClient.framework/PrivateSearchClient` | 4.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PrivateSearchCore.framework/PrivateSearchCore` | 4.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PrivateSearchProtocols.framework/PrivateSearchProtocols` | 4.0.0.0.0 | not generated |
| [`/System/Library/PrivateFrameworks/ProDisplayLibrary.framework/ProDisplayLibrary`](System__Library__PrivateFrameworks__ProDisplayLibrary.framework__ProDisplayLibrary.md) | 11.1.1.0.0 | full |
| `/System/Library/PrivateFrameworks/ProVideo.framework/ProVideo` | 612.0.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ProactiveBlendingLayer_iOS.framework/ProactiveBlendingLayer_iOS` | 678.0.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ProactiveCDNDownloader.framework/ProactiveCDNDownloader` | 678.0.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ProactiveContextClient.framework/ProactiveContextClient` | 678.0.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ProactiveEventTracker.framework/ProactiveEventTracker` | 425.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ProactiveExperiments.framework/ProactiveExperiments` | 1354.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ProactiveExperimentsInternals.framework/ProactiveExperimentsInternals` | 1354.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ProactiveHarvesting.framework/ProactiveHarvesting` | 1354.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ProactiveInputPredictions.framework/ProactiveInputPredictions` | 1354.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ProactiveInputPredictionsInternals.framework/ProactiveInputPredictionsInternals` | 1354.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ProactiveML.framework/ProactiveML` | 1354.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ProactiveMagicalMoments.framework/ProactiveMagicalMoments` | 678.0.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ProactivePredictionClient.framework/ProactivePredictionClient` | 678.0.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ProactivePredictionFoundation.framework/ProactivePredictionFoundation` | 678.0.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization` | 1354.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ProactiveSupportStubs.framework/ProactiveSupportStubs` | 425.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ProductKit.framework/ProductKit` | 155.200.61.2.2 | not generated |
| `/System/Library/PrivateFrameworks/ProductKitCore.framework/ProductKitCore` | 155.200.61.2.2 | not generated |
| `/System/Library/PrivateFrameworks/ProfileValidatedAppIdentity.framework/ProfileValidatedAppIdentity` | 158.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ProgressUI.framework/ProgressUI` | 2858.1.5.100.0 | not generated |
| `/System/Library/PrivateFrameworks/PromotedContentPrediction.framework/PromotedContentPrediction` | 102.4.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PromotedContentProxy.framework/PromotedContentProxy` | 557.2.14.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PromotedContentSupport.framework/PromotedContentSupport` | 557.2.14.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PromptKit.framework/PromptKit` | 297.12.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ProtoDataExtractor.framework/ProtoDataExtractor` | 2.4.6.0.0 | not generated |
| `/System/Library/PrivateFrameworks/PrototypeToolsUI.framework/PrototypeToolsUI` | 165.1.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ProxCardKit.framework/ProxCardKit` | 2131.21.31.21.8 | not generated |
| `/System/Library/PrivateFrameworks/ProximityAppleIDSetup.framework/ProximityAppleIDSetup` | 92.125.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ProximityAppleIDSetupUI.framework/ProximityAppleIDSetupUI` | 92.125.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ProximityControl.framework/ProximityControl` | 376.11.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ProximityReaderCore.framework/ProximityReaderCore` | 151.6.0.0.0 | not generated |
| `/usr/lib/objc/libobjcMsgSend28.dylib` | 973.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ProximityUI.framework/ProximityUI` | 576.0.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/QLCharts.framework/QLCharts` | 322.1.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/QOSToolkit.framework/QOSToolkit` | 2025.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Quagga.framework/Quagga` | 234.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/QueryUnderstanding.framework/QueryUnderstanding` | 3605.8.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/QuickLookThumbnailGeneration.framework/QuickLookThumbnailGeneration` | 218.1.3.200.0 | not generated |
| `/System/Library/PrivateFrameworks/QuickLookThumbnailingDaemon.framework/QuickLookThumbnailingDaemon` | 218.1.3.200.0 | not generated |
| `/System/Library/PrivateFrameworks/RESync.framework/RESync` | 453.42.1.0.1 | not generated |
| [`/System/Library/PrivateFrameworks/RTBuddyCrashlogDecoder.framework/RTBuddyCrashlogDecoder`](System__Library__PrivateFrameworks__RTBuddyCrashlogDecoder.framework__RTBuddyCrashlogDecoder.md) | 778.40.12.0.0 | full |
| `/System/Library/PrivateFrameworks/RTTUI.framework/RTTUI` | 543.2.5.0.0 | not generated |
| `/System/Library/PrivateFrameworks/RTTUtilities.framework/RTTUtilities` | 543.2.5.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Radio.framework/Radio` | 4026.200.7.0.0 | not generated |
| `/System/Library/PrivateFrameworks/RapportUI.framework/RapportUI` | 751.200.101.0.0 | not generated |
| `/System/Library/PrivateFrameworks/RealityCoreTextureImport.framework/RealityCoreTextureImport` | 24.40.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/RealityFusion.framework/RealityFusion` | 453.42.1.0.1 | not generated |
| `/System/Library/PrivateFrameworks/RealityIO.framework/RealityIO` | 235.40.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/RealityKitInspection.framework/RealityKitInspection` | 48.0.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Recap.framework/Recap` | 201.107.0.1.0 | not generated |
| `/System/Library/PrivateFrameworks/RecapPerformanceTesting.framework/RecapPerformanceTesting` | 56.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Recon3D.framework/Recon3D` | 9.26.7.9.0 | not generated |
| `/System/Library/PrivateFrameworks/Recount.framework/Recount` | 99.40.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ReflectionInternal.framework/ReflectionInternal` | 5027.1.6.0.0 | not generated |
| `/System/Library/PrivateFrameworks/RelativeMotion.framework/RelativeMotion` | 376.0.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/RelevanceEngine.framework/RelevanceEngine` | 576.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/RelevanceEngineUI.framework/RelevanceEngineUI` | 576.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ReminderKitUI.framework/ReminderKitUI` | 4080.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/RemindersIntentsFramework.framework/RemindersIntentsFramework` | 4080.0.0.0.0 | not generated |
| [`/System/Library/PrivateFrameworks/RemoteCoreML.framework/RemoteCoreML`](System__Library__PrivateFrameworks__RemoteCoreML.framework__RemoteCoreML.md) | 2.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/RemoteHID.framework/RemoteHID`](System__Library__PrivateFrameworks__RemoteHID.framework__RemoteHID.md) | 224.40.2.0.0 | full |
| `/System/Library/PrivateFrameworks/RemoteManagementModel.framework/RemoteManagementModel` | 624.52.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/RemoteManagementProtocol.framework/RemoteManagementProtocol` | 624.52.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore` | 624.52.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/RemoteManagementUI.framework/RemoteManagementUI` | 624.52.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/RemoteMediaServices.framework/RemoteMediaServices` | 2024.200.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery` | 245.40.9.0.0 | not generated |
| `/System/Library/PrivateFrameworks/RemoteSoftwareUpdate.framework/RemoteSoftwareUpdate` | 1.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/RemoteStateDumpKit.framework/RemoteStateDumpKit` | 391.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC` | 3298.52.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ReplicatorDependencies.framework/ReplicatorDependencies` | 176.2.6.0.0 | not generated |
| `/System/Library/PrivateFrameworks/RespiratoryHealth.framework/RespiratoryHealth` | 7027.1.56.6.5 | not generated |
| `/System/Library/PrivateFrameworks/RespiratoryHealthDaemon.framework/RespiratoryHealthDaemon` | 7027.1.56.6.5 | not generated |
| `/System/Library/PrivateFrameworks/RespiratoryHealthUI.framework/RespiratoryHealthUI` | 7027.1.56.6.5 | not generated |
| `/System/Library/PrivateFrameworks/ResponseKit.framework/ResponseKit` | 207.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ResponseUI.framework/ResponseUI` | 3600.6.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/RevealCore.framework/RevealCore` | 62.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Rewind.framework/Rewind` | 99.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/RoomScanCore.framework/RoomScanCore` | 20.10.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/RoyaCapture.framework/RoyaCapture` | 47.0.1.0.1 | not generated |
| `/System/Library/PrivateFrameworks/RoyaCaptureCore.framework/RoyaCaptureCore` | 47.0.1.0.1 | not generated |
| `/System/Library/PrivateFrameworks/RoyaFormatCore.framework/RoyaFormatCore` | 47.0.1.0.1 | not generated |
| `/System/Library/PrivateFrameworks/RoyaMediaOffload.framework/RoyaMediaOffload` | 47.0.1.0.1 | not generated |
| `/System/Library/PrivateFrameworks/RoyaProtobufKit.framework/RoyaProtobufKit` | 47.0.1.0.1 | not generated |
| `/System/Library/PrivateFrameworks/RoyaReplay.framework/RoyaReplay` | 47.0.1.0.1 | not generated |
| `/System/Library/PrivateFrameworks/RoyaReplayCore.framework/RoyaReplayCore` | 47.0.1.0.1 | not generated |
| `/System/Library/PrivateFrameworks/RoyaSystemCapture.framework/RoyaSystemCapture` | 47.0.1.0.1 | not generated |
| `/System/Library/PrivateFrameworks/RoyaUtilities.framework/RoyaUtilities` | 47.0.1.0.1 | not generated |
| `/System/Library/PrivateFrameworks/RoyaUtilitiesSwift.framework/RoyaUtilitiesSwift` | 47.0.1.0.1 | not generated |
| `/System/Library/PrivateFrameworks/Rules.framework/Rules` | 106.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/RuntimeInternal.framework/RuntimeInternal` | 5027.1.6.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SADSupport.framework/SADSupport` | 849.40.7.0.2 | not generated |
| `/System/Library/PrivateFrameworks/SAML.framework/SAML` | 609.10.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SANovaGestureRecognizers.framework/SANovaGestureRecognizers` | 114.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SCSharingReminders.framework/SCSharingReminders` | 653.0.10.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SDAPI.framework/SDAPI` | 19.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SESShared.framework/SESShared` | 71.9.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SESUIService.framework/SESUIService` | 71.9.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SESUIServiceCore.framework/SESUIServiceCore` | 71.9.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SFSymbols.framework/SFSymbols` | 207.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SIDFitness.framework/SIDFitness` | 1.81.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SIDThinClient.framework/SIDThinClient` | 1.81.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SILManager.framework/SILManager` | 68.14.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SIMToolkitUI.framework/SIMToolkitUI` | 87.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SLOM.framework/SLOM` | 1.19.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SLOMCommon.framework/SLOMCommon` | 1.19.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SLOMMapping.framework/SLOMMapping` | 1.19.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SLOMOdometry.framework/SLOMOdometry` | 1.19.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SMBClientEngine.framework/SMBClientEngine` | 155.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SMBClientProvider.framework/SMBClientProvider` | 249.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SMBSearch.framework/SMBSearch` | 249.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SMCT.framework/SMCT` | 10.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SOS.framework/SOS` | 684.200.21.21.1 | not generated |
| `/System/Library/PrivateFrameworks/SOSUI.framework/SOSUI` | 684.200.21.21.1 | not generated |
| `/System/Library/PrivateFrameworks/SPRCore.framework/SPRCore` | 51.5.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SPShared.framework/SPShared` | 449.31.6.16.29 | not generated |
| `/System/Library/PrivateFrameworks/STSXPCHelperClient.framework/STSXPCHelperClient` | 6.1.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation` | 625.2.8.21.5 | not generated |
| `/System/Library/PrivateFrameworks/SafetyAlerts.framework/SafetyAlerts` | 70.0.21.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor` | 1123.0.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Sage.framework/Sage` | 297.12.4.0.0 | not generated |
| [`/System/Library/PrivateFrameworks/SavageCameraInterface.framework/SavageCameraInterface`](System__Library__PrivateFrameworks__SavageCameraInterface.framework__SavageCameraInterface.md) | 10.66.0.0.0 | full |
| `/System/Library/PrivateFrameworks/Scandium.framework/Scandium` | 96.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SceneHosting.framework/SceneHosting` | 38.1.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SceneIntelligence.framework/SceneIntelligence` | 138.5.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SchoolTime.framework/SchoolTime` | 39.0.6.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SchoolTimeSettingsUI.framework/SchoolTimeSettingsUI` | 39.0.6.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ScreenContinuityServices.framework/ScreenContinuityServices` | 126.12.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ScreenReaderBrailleDriver.framework/ScreenReaderBrailleDriver` | 467.3.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ScreenReaderCore.framework/ScreenReaderCore` | 285.0.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput` | 467.3.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ScreenSharingAccessibilityService.framework/ScreenSharingAccessibilityService` | 126.12.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ScreenSharingKit.framework/ScreenSharingKit` | 126.12.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ScreenTimeSettingsServicesUI.framework/ScreenTimeSettingsServicesUI` | 97.1.14.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI` | 655.1.14.1.0 | not generated |
| `/System/Library/PrivateFrameworks/ScreenTimeUI.framework/ScreenTimeUI` | 655.1.14.1.0 | not generated |
| `/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/ScreenTimeUICore` | 655.1.14.1.0 | not generated |
| `/System/Library/PrivateFrameworks/Search.framework/Search` | 2465.1.9.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SearchIntrospectionKit.framework/SearchIntrospectionKit` | 140.1.17.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SearchToShareCore.framework/SearchToShareCore` | 3400.1.6.40.0 | not generated |
| `/System/Library/PrivateFrameworks/SearchUICardKitProviderSupport.framework/SearchUICardKitProviderSupport` | 3520.8.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SecureAudioPasscode.framework/SecureAudioPasscode` | 210.3.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SecureCaptureKit.framework/SecureCaptureKit` | 159.2.5.0.6 | not generated |
| `/System/Library/PrivateFrameworks/SecureChannel.framework/SecureChannel` | 1.0.67.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SecureMessaging.framework/SecureMessaging` | 59.200.41.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SecureMessagingAgentCore.framework/SecureMessagingAgentCore` | 59.200.41.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SecurePairing.framework/SecurePairing` | 67.7.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SecurePairingSession.framework/SecurePairingSession` | 67.7.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SecurePairingTypes.framework/SecurePairingTypes` | 67.7.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SecureSessionManagement.framework/SecureSessionManagement` | 248.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SecureTransactionService.framework/SecureTransactionService` | 6.1.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SecureVectorStore.framework/SecureVectorStore` | 117.0.1.1.8 | not generated |
| [`/System/Library/PrivateFrameworks/SecureVoiceTriggerAssets.framework/SecureVoiceTriggerAssets`](System__Library__PrivateFrameworks__SecureVoiceTriggerAssets.framework__SecureVoiceTriggerAssets.md) | 4.6.4.0.0 | full |
| `/System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation` | 55294.0.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SecurityUICore.framework/SecurityUICore` | 55222.40.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Seeding.framework/Seeding` | 131.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SemanticPerception.framework/SemanticPerception` | 1.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SensingAlgsPadHostServiceJ8xx.framework/SensingAlgsPadHostServiceJ8xx` | 10.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SensingAlgsService.framework/SensingAlgsService` | 72.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SensingAlgsTouchButtonHost.framework/SensingAlgsTouchButtonHost` | 114.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SensingPredict.framework/SensingPredict` | 20.27.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SensingPredictDaemon.framework/SensingPredictDaemon` | 20.27.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SensingPredictServices.framework/SensingPredictServices` | 20.27.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/SensitiveContentAnalysisML` | 165.5.0.0.0 | not generated |
| [`/System/Library/PrivateFrameworks/SensorAccess.framework/SensorAccess`](System__Library__PrivateFrameworks__SensorAccess.framework__SensorAccess.md) | 27.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/SensorKitHelper.framework/SensorKitHelper`](System__Library__PrivateFrameworks__SensorKitHelper.framework__SensorKitHelper.md) | 1039.0.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/SensorKitSupport.framework/SensorKitSupport`](System__Library__PrivateFrameworks__SensorKitSupport.framework__SensorKitSupport.md) | 7.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/SensorKitUI.framework/SensorKitUI`](System__Library__PrivateFrameworks__SensorKitUI.framework__SensorKitUI.md) | 1039.0.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/SensorKitWriting.framework/SensorKitWriting`](System__Library__PrivateFrameworks__SensorKitWriting.framework__SensorKitWriting.md) | 1039.0.1.0.0 | full |
| `/System/Library/PrivateFrameworks/SentencePieceInternal.framework/SentencePieceInternal` | 70.3.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Sentry.framework/Sentry` | 12.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ServiceManagement.framework/ServiceManagement` | 3298.52.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ServicesAnalyticsCore.framework/ServicesAnalyticsCore` | 3.1.15.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ServicesAnalyticsKit.framework/ServicesAnalyticsKit` | 3.1.15.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ServicesPaymentKit.framework/ServicesPaymentKit` | 1.1.14.2.2 | not generated |
| `/System/Library/PrivateFrameworks/ServicesPaymentUI.framework/ServicesPaymentUI` | 1.1.14.2.2 | not generated |
| `/System/Library/PrivateFrameworks/SessionAlert.framework/SessionAlert` | 313.2.9.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SessionAssertion.framework/SessionAssertion` | 313.2.9.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SessionSQL.framework/SessionSQL` | 313.2.9.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SessionSyncEngine.framework/SessionSyncEngine` | 313.2.9.0.0 | not generated |
| [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) | 1215.1.6.600.0 | full |
| `/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI` | 2027.1.10.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Settings/SettingsUIKitPrivate.framework/SettingsUIKitPrivate` | 2027.0.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SettingsCellular.framework/SettingsCellular` | 756.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI` | 756.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation` | 2027.1.1.0.0 | not generated |
| [`/System/Library/PrivateFrameworks/SetupAssistantPane.framework/SetupAssistantPane`](System__Library__PrivateFrameworks__SetupAssistantPane.framework__SetupAssistantPane.md) | 7.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/SetupAssistantPaneUI.framework/SetupAssistantPaneUI`](System__Library__PrivateFrameworks__SetupAssistantPaneUI.framework__SetupAssistantPaneUI.md) | 7.0.0.0.0 | full |
| `/System/Library/PrivateFrameworks/SetupAssistantSoftwareUpdateUI.framework/SetupAssistantSoftwareUpdateUI` | 772.40.12.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SetupAssistantSupport.framework/SetupAssistantSupport` | 568.1.5.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SetupAssistantUI.framework/SetupAssistantUI` | 5411.2.4.602.0 | not generated |
| `/usr/lib/objc/libobjcMsgSend29.dylib` | 973.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SensingAlgsCodexV68AP.framework/SensingAlgsCodexV68AP` | 62.8.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SetupAssistantSupportUI.framework/SetupAssistantSupportUI` | 568.1.5.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SetupKit.framework/SetupKit` | 910.31.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SeymourAppStore.framework/SeymourAppStore` | 2027.1.69.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SeymourBiome.framework/SeymourBiome` | 2027.1.69.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SeymourClientFoundation.framework/SeymourClientFoundation` | 2027.1.69.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SeymourCoreFoundation.framework/SeymourCoreFoundation` | 2027.1.69.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SeymourHealth.framework/SeymourHealth` | 2027.1.69.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SeymourServerProtocol.framework/SeymourServerProtocol` | 2027.1.69.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SeymourServiceSubscriptionCore.framework/SeymourServiceSubscriptionCore` | 2027.1.69.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SeymourSharePlay.framework/SeymourSharePlay` | 2027.1.69.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SeymourXPCServicesFoundation.framework/SeymourXPCServicesFoundation` | 2027.1.69.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ShareReporting.framework/ShareReporting` | 106.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SharedWebCredentials.framework/SharedWebCredentials` | 1036.2.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SharingHUD.framework/SharingHUD` | 2131.21.31.21.8 | not generated |
| `/System/Library/PrivateFrameworks/SharingXPCServices.framework/SharingXPCServices` | 2131.21.31.21.8 | not generated |
| `/System/Library/PrivateFrameworks/ShazamCore.framework/ShazamCore` | 427.2.6.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ShazamEventsUI.framework/ShazamEventsUI` | 427.2.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ShazamInsights.framework/ShazamInsights` | 427.2.6.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ShazamKitUI.framework/ShazamKitUI` | 427.2.6.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ShimGameServices.framework/ShimGameServices` | 821.1.16.2.1 | not generated |
| `/System/Library/PrivateFrameworks/ShortcutUIKit.framework/ShortcutUIKit` | 391.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ShortcutsAgent.framework/ShortcutsAgent` | 5114.0.12.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ShortcutsLanguage.framework/ShortcutsLanguage` | 5114.0.12.0.0 | not generated |
| [`/System/Library/PrivateFrameworks/SidebarFileDispatcher.framework/SidebarFileDispatcher`](System__Library__PrivateFrameworks__SidebarFileDispatcher.framework__SidebarFileDispatcher.md) | 849.40.17.0.0 | full |
| `/System/Library/PrivateFrameworks/SidecarCore.framework/SidecarCore` | 412.4.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SidecarUI.framework/SidecarUI` | 412.4.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SignalCompression.framework/SignalCompression` | 32.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SignpostCollection.framework/SignpostCollection` | 205.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SignpostMetrics.framework/SignpostMetrics` | 205.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SignpostNotification.framework/SignpostNotification` | 205.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Silex.framework/Silex` | 5971.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SilexVideo.framework/SilexVideo` | 5971.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SilexWeb.framework/SilexWeb` | 5971.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SimpleClockFacePosters.framework/SimpleClockFacePosters` | 123.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriAnalyticsRuntime.framework/SiriAnalyticsRuntime` | 3605.33.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriAnalyticsToolKitSupport.framework/SiriAnalyticsToolKitSupport` | 2.8.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriAppIntents.framework/SiriAppIntents` | 3605.17.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriAppIntentsRuntime.framework/SiriAppIntentsRuntime` | 3605.17.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriAppLaunchFlowTools.framework/SiriAppLaunchFlowTools` | 3605.6.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/SiriAppLaunchIntents` | 3605.6.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriAppLaunchUIFramework.framework/SiriAppLaunchUIFramework` | 3605.6.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriAppResolution.framework/SiriAppResolution` | 3605.22.1.11.1 | not generated |
| `/System/Library/PrivateFrameworks/SiriAssetUtilities.framework/SiriAssetUtilities` | 3605.17.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriAudioIntentUtils.framework/SiriAudioIntentUtils` | 3605.24.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriAudioInternal.framework/SiriAudioInternal` | 3605.24.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriAudioSnippetKit.framework/SiriAudioSnippetKit` | 3605.24.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriAudioSupport.framework/SiriAudioSupport` | 3605.24.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriAutoComplete.framework/SiriAutoComplete` | 3605.7.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriAutoCompleteAPI.framework/SiriAutoCompleteAPI` | 3605.7.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriAvailability.framework/SiriAvailability` | 3605.4.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriCalendar.framework/SiriCalendar` | 3605.10.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriCalendarIntents.framework/SiriCalendarIntents` | 3605.10.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriCalendarUI.framework/SiriCalendarUI` | 3605.10.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriCam.framework/SiriCam` | 3605.3.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriCarCommandsIntents.framework/SiriCarCommandsIntents` | 3605.4.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriContactsCommon.framework/SiriContactsCommon` | 3605.8.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriContactsIntents.framework/SiriContactsIntents` | 3605.8.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriContactsUI.framework/SiriContactsUI` | 3605.8.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriCoreMetrics.framework/SiriCoreMetrics` | 6.1.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriCorrections.framework/SiriCorrections` | 3500.4.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriDailyBriefingInternal.framework/SiriDailyBriefingInternal` | 3605.2.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriDeviceSelection.framework/SiriDeviceSelection` | 3605.25.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriDeviceSelectionSignals.framework/SiriDeviceSelectionSignals` | 3605.25.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriEmergencyIntents.framework/SiriEmergencyIntents` | 3605.11.1.11.1 | not generated |
| `/System/Library/PrivateFrameworks/SiriExpanseInternal.framework/SiriExpanseInternal` | 3505.1.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriExpanseInternalUI.framework/SiriExpanseInternalUI` | 3505.1.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriFindMy.framework/SiriFindMy` | 3605.19.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriFlowEnvironment.framework/SiriFlowEnvironment` | 3600.1.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriGeo.framework/SiriGeo` | 3605.14.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriGestureBridge.framework/SiriGestureBridge` | 3600.2.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriGlobalConfiguration.framework/SiriGlobalConfiguration` | 3525.3.1.0.0 | not generated |
| [`/System/Library/PrivateFrameworks/SiriHomeAccessoryFramework.framework/SiriHomeAccessoryFramework`](System__Library__PrivateFrameworks__SiriHomeAccessoryFramework.framework__SiriHomeAccessoryFramework.md) | 3605.31.1.11.2 | full |
| `/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/SiriIdentityInternal` | 3605.3.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriInferenceFlow.framework/SiriInferenceFlow` | 3605.20.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriInferenceIntents.framework/SiriInferenceIntents` | 3204.7.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriInformationTypes.framework/SiriInformationTypes` | 3605.24.1.11.2 | not generated |
| `/System/Library/PrivateFrameworks/SiriInstrumentationEx.framework/SiriInstrumentationEx` | 3605.33.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriInstrumentationManifest.framework/SiriInstrumentationManifest` | 3605.17.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriIntentEvents.framework/SiriIntentEvents` | 3605.20.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriInteractive.framework/SiriInteractive` | 3605.28.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriKitInvocation.framework/SiriKitInvocation` | 3520.3.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriLiminal.framework/SiriLiminal` | 3605.32.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriLocalization.framework/SiriLocalization` | 3605.31.1.11.2 | not generated |
| `/System/Library/PrivateFrameworks/SiriMailInternal.framework/SiriMailInternal` | 3605.18.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriMailOntology.framework/SiriMailOntology` | 3605.18.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriMailUI.framework/SiriMailUI` | 3605.18.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriMailUIModel.framework/SiriMailUIModel` | 3605.18.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow` | 3605.21.1.11.2 | not generated |
| `/System/Library/PrivateFrameworks/SiriMessagesFlowCommon.framework/SiriMessagesFlowCommon` | 3605.21.1.11.2 | not generated |
| `/System/Library/PrivateFrameworks/SiriMessagesFlowTools.framework/SiriMessagesFlowTools` | 3605.21.1.11.2 | not generated |
| `/System/Library/PrivateFrameworks/SiriMessagesUI.framework/SiriMessagesUI` | 3605.21.1.11.2 | not generated |
| `/System/Library/PrivateFrameworks/SiriMessagesUICommon.framework/SiriMessagesUICommon` | 3605.21.1.11.2 | not generated |
| `/System/Library/PrivateFrameworks/SiriMetricsBugReporter.framework/SiriMetricsBugReporter` | 3605.17.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriModes.framework/SiriModes` | 3402.3.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriNLUOverrides.framework/SiriNLUOverrides` | 3605.19.1.11.1 | not generated |
| `/System/Library/PrivateFrameworks/SiriNLUTypes.framework/SiriNLUTypes` | 3605.3.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriNaturalLanguageGeneration.framework/SiriNaturalLanguageGeneration` | 3500.4.1.0.0 | not generated |
| [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) | 3605.10.1.0.0 | full |
| `/System/Library/PrivateFrameworks/SiriNotebook.framework/SiriNotebook` | 3605.16.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriNotebookUI.framework/SiriNotebookUI` | 3605.16.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriNotificationsIntents.framework/SiriNotificationsIntents` | 3605.6.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriOntologyProtobuf.framework/SiriOntologyProtobuf` | 3605.4.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriOrchestration.framework/SiriOrchestration` | 3605.4.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriOrchestrationServices.framework/SiriOrchestrationServices` | 3605.4.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriPaymentsIntents.framework/SiriPaymentsIntents` | 3605.6.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriPhoneCATs.framework/SiriPhoneCATs` | 3605.27.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriPhoneIntents.framework/SiriPhoneIntents` | 3605.27.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/SiriPlaybackControlIntents` | 3605.17.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriPlaybackControlSupport.framework/SiriPlaybackControlSupport` | 3605.17.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriPowerInstrumentation.framework/SiriPowerInstrumentation` | 3500.3.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriPrivateLearningLogging.framework/SiriPrivateLearningLogging` | 3200.3.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriReaderIntents.framework/SiriReaderIntents` | 3600.1.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriReaderServices.framework/SiriReaderServices` | 3605.23.2.3.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriReferenceResolutionDataModel.framework/SiriReferenceResolutionDataModel` | 3500.13.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriReferenceResolver.framework/SiriReferenceResolver` | 3500.3.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriSchemaRegistry.framework/SiriSchemaRegistry` | 3.3.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/SiriSettingsIntents` | 3605.6.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriSettingsUI.framework/SiriSettingsUI` | 3605.6.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriSetup.framework/SiriSetup` | 3605.33.1.11.9 | not generated |
| `/System/Library/PrivateFrameworks/SiriSignals.framework/SiriSignals` | 3605.20.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriSocialConversation.framework/SiriSocialConversation` | 3600.5.2.0.0 | not generated |
| [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) | 3605.24.1.11.3 | full |
| `/System/Library/PrivateFrameworks/SiriStates.framework/SiriStates` | 3500.2.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriSuggestions.framework/SiriSuggestions` | 3605.7.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/SiriSuggestionsBaseModel` | 3605.7.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriSuggestionsIntelligence.framework/SiriSuggestionsIntelligence` | 3605.7.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/SiriSuggestionsSupport` | 3605.7.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriSystemCommandsIntents.framework/SiriSystemCommandsIntents` | 3600.3.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriSystemCommandsUIFramework.framework/SiriSystemCommandsUIFramework` | 3600.3.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriTaskEngagement.framework/SiriTaskEngagement` | 3605.17.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriTasks.framework/SiriTasks` | 3605.31.1.11.2 | not generated |
| `/System/Library/PrivateFrameworks/SiriTasksEvaluation.framework/SiriTasksEvaluation` | 3600.3.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriTimeAlarmInternal.framework/SiriTimeAlarmInternal` | 3605.13.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriTimeInternal.framework/SiriTimeInternal` | 3605.13.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriTimeTimerInternal.framework/SiriTimeTimerInternal` | 3605.13.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriTranslationIntents.framework/SiriTranslationIntents` | 3605.7.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriTranslationUI.framework/SiriTranslationUI` | 3605.7.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriUIBridge.framework/SiriUIBridge` | 3605.2.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriUICardKitProviderSupport.framework/SiriUICardKitProviderSupport` | 3605.23.2.3.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriUIFoundation.framework/SiriUIFoundation` | 3605.23.2.3.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriUserSegments.framework/SiriUserSegments` | 3600.5.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriVOX.framework/SiriVOX` | 3605.19.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriVideoIntents.framework/SiriVideoIntents` | 3605.27.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriVideoUIFramework.framework/SiriVideoUIFramework` | 3605.27.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriVirtualDeviceResolution.framework/SiriVirtualDeviceResolution` | 3520.3.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SiriWellnessIntents.framework/SiriWellnessIntents` | 3605.11.1.11.1 | not generated |
| `/System/Library/PrivateFrameworks/SleepDaemon.framework/SleepDaemon` | 7027.1.56.6.5 | not generated |
| `/System/Library/PrivateFrameworks/SleepWidgetUI.framework/SleepWidgetUI` | 7027.1.56.6.5 | not generated |
| `/System/Library/PrivateFrameworks/SlideshowKit.framework/Frameworks/OpusFoundation.framework/OpusFoundation` | 1704.0.110.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SlideshowKit.framework/SlideshowKit` | 1704.0.110.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SmartNameSuggestions.framework/SmartNameSuggestions` | 24.1.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SmartRepliesServer.framework/SmartRepliesServer` | 192.0.0.0.0 | not generated |
| `/usr/lib/objc/libobjcMsgSend30.dylib` | 973.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Skimmer.framework/Skimmer` | 1.4.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SleepHealthUI.framework/SleepHealthUI` | 7027.1.56.6.5 | not generated |
| `/System/Library/PrivateFrameworks/SlideshowKit.framework/Frameworks/OpusKit.framework/OpusKit` | 1704.0.110.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SmartReplies.framework/SmartReplies` | 192.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SmartRepliesUI.framework/SmartRepliesUI` | 192.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SmartStackFoundation.framework/SmartStackFoundation` | 350.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SmartStackUIServices.framework/SmartStackUIServices` | 350.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SnippetCommands.framework/SnippetCommands` | 3605.28.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SnippetKit.framework/SnippetKit` | 3605.28.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SnippetUI.framework/SnippetUI` | 3605.28.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SnippetUI_Proto.framework/SnippetUI_Proto` | 3605.28.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SocialServices.framework/SocialServices` | 774.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking` | 72.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SoftPosReader.framework/SoftPosReader` | 51.5.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SoftwareUpdateBridge.framework/SoftwareUpdateBridge` | 393.40.6.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SoftwareUpdateController.framework/SoftwareUpdateController` | 201.40.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore` | 2718.52.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/SoftwareUpdateServicesUI` | 305.40.5.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SoftwareUpdateSettings.framework/SoftwareUpdateSettings` | 772.40.12.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SoftwareUpdateSettingsUI.framework/SoftwareUpdateSettingsUI` | 772.40.12.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SoftwareUpdateUIBridge.framework/SoftwareUpdateUIBridge` | 772.40.12.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SoftwareUpdateUIFoundation.framework/SoftwareUpdateUIFoundation` | 772.40.12.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SoftwareUpdateUIKit.framework/SoftwareUpdateUIKit` | 772.40.12.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SoftwareUpdateUIMobile.framework/SoftwareUpdateUIMobile` | 772.40.12.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SonicAudioUnits.framework/SonicAudioUnits` | 26110.26.36.301.0 | not generated |
| `/System/Library/PrivateFrameworks/SonicFoundation.framework/SonicFoundation` | 26210.26.40.301.0 | not generated |
| `/System/Library/PrivateFrameworks/SoundAutoConfig.framework/SoundAutoConfig` | 109.27.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SoundBoardServices.framework/SoundBoardServices` | 914.10.35.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SoundScapesUtility.framework/SoundScapesUtility` | 268.10.46.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SpaceAttribution.framework/SpaceAttribution` | 499.40.4.0.1 | not generated |
| `/System/Library/PrivateFrameworks/SpatialAudioProfile.framework/SpatialAudioProfile` | 41.7.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SpatialAudioServices.framework/SpatialAudioServices` | 23.40.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SpatialInspectorFoundation.framework/SpatialInspectorFoundation` | 48.0.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SpatialPerception.framework/SpatialPerception` | 9.26.5.12.5 | not generated |
| `/System/Library/PrivateFrameworks/SpeakThisServices.framework/SpeakThisServices` | 3245.8.9.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SpeakTypingServices.framework/SpeakTypingServices` | 3245.8.9.0.0 | not generated |
| [`/System/Library/PrivateFrameworks/SpeakerGroupSetupKit.framework/SpeakerGroupSetupKit`](System__Library__PrivateFrameworks__SpeakerGroupSetupKit.framework__SpeakerGroupSetupKit.md) | 69.10.60.0.0 | full |
| [`/System/Library/PrivateFrameworks/SpeakerRecognitionKit.framework/SpeakerRecognitionKit`](System__Library__PrivateFrameworks__SpeakerRecognitionKit.framework__SpeakerRecognitionKit.md) | 3605.32.1.0.0 | full |
| `/System/Library/PrivateFrameworks/SpeechDetector.framework/SpeechDetector` | 3605.32.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SpeechDictionary.framework/SpeechDictionary` | 22.1.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SpeechEngine.framework/SpeechEngine` | 3605.8.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SpeechRecognitionCommandAndControl.framework/SpeechRecognitionCommandAndControl` | 191.2.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SpeechRecognitionCommandServices.framework/SpeechRecognitionCommandServices` | 35.1.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/SpeechRecognitionCore` | 41.1.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SpeechRecognitionSharedSupport.framework/SpeechRecognitionSharedSupport` | 41.1.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SpeechRuntime.framework/SpeechRuntime` | 3605.14.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SpeechTranslation.framework/SpeechTranslation` | 396.2.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SplashBoard.framework/SplashBoard` | 321.1.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SpotlightDiagnostics.framework/SpotlightDiagnostics` | 2465.1.9.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SpotlightEmbedding.framework/SpotlightEmbedding` | 2465.1.9.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SpotlightEmbeddingCore.framework/SpotlightEmbeddingCore` | 2465.1.9.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SpotlightFoundation.framework/SpotlightFoundation` | 2465.1.9.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SpotlightLinguistics.framework/SpotlightLinguistics` | 2465.1.9.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SpotlightRecommendation.framework/SpotlightRecommendation` | 2465.1.9.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SpotlightSettingsSupport.framework/SpotlightSettingsSupport` | 250.1.12.200.0 | not generated |
| `/System/Library/PrivateFrameworks/SpotlightUI.framework/SpotlightUI` | 250.1.12.200.0 | not generated |
| `/System/Library/PrivateFrameworks/SpotlightUICLI.framework/SpotlightUICLI` | 250.1.12.200.0 | not generated |
| [`/System/Library/PrivateFrameworks/SpringBoardDisplayServices.framework/SpringBoardDisplayServices`](System__Library__PrivateFrameworks__SpringBoardDisplayServices.framework__SpringBoardDisplayServices.md) | 41.100.0.0.0 | full |
| `/System/Library/PrivateFrameworks/SpringBoardIntents.framework/SpringBoardIntents` | 391.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Stateful.framework/Stateful` | 196.40.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/StickerFoundationInternal.framework/StickerFoundationInternal` | 152.1.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/StickerKitInternal.framework/StickerKitInternal` | 152.1.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Stickers.framework/Support/IndexerService.framework/IndexerService` | 90.1.5.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Stickers.framework/Support/RecencyService.framework/RecencyService` | 90.1.5.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Stickers.framework/Support/ServiceShared.framework/ServiceShared` | 90.1.5.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Stickers.framework/Support/StarmojiSearch.framework/StarmojiSearch` | 90.1.5.0.0 | not generated |
| `/System/Library/PrivateFrameworks/StickersUI.framework/StickersUI` | 406.200.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Stocks.framework/Stocks` | 1555.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/StocksKit.framework/StocksKit` | 2063.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/StopwatchAppIntents.framework/StopwatchAppIntents` | 308.2.7.0.0 | not generated |
| `/System/Library/PrivateFrameworks/StorageContainersPrivate.framework/StorageContainersPrivate` | 833.40.18.0.1 | not generated |
| `/System/Library/PrivateFrameworks/StorageData.framework/StorageData` | 157.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/StorageKit.framework/StorageKit` | 1076.40.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/StorageSettings.framework/StorageSettings` | 157.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/StorageUI.framework/StorageUI` | 177.1.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/StoreBookkeeper.framework/StoreBookkeeper` | 4026.200.7.0.0 | not generated |
| `/System/Library/PrivateFrameworks/StoreBookkeeperClient.framework/StoreBookkeeperClient` | 4026.200.7.0.0 | not generated |
| `/System/Library/PrivateFrameworks/StoreKitUI.framework/StoreKitUI` | 816.1.16.0.0 | not generated |
| `/System/Library/PrivateFrameworks/StreamingAppleTrace.framework/StreamingAppleTrace` | 122.0.0.0.1 | not generated |
| `/System/Library/PrivateFrameworks/StrokeAnimation.framework/StrokeAnimation` | 3401.1.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/StudyLog.framework/StudyLog` | 35.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SuggestionsSpotlightMetrics.framework/SuggestionsSpotlightMetrics` | 1354.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SummariesHealthDaemon.framework/SummariesHealthDaemon` | 7027.1.56.6.5 | not generated |
| `/System/Library/PrivateFrameworks/SummarizationKit.framework/SummarizationKit` | 25.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SupportFlowUI.framework/SupportFlowUI` | 37.1.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SupportServices.framework/SupportServices` | 37.1.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SurveyKit.framework/SurveyKit` | 7027.1.56.6.5 | not generated |
| `/System/Library/PrivateFrameworks/SurveyKitUI.framework/SurveyKitUI` | 7027.1.56.6.5 | not generated |
| `/System/Library/PrivateFrameworks/SwiftASN1Internal.framework/SwiftASN1Internal` | 26.0.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SwiftCertificate.framework/SwiftCertificate` | 62460.40.78.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SwiftMLS.framework/SwiftMLS` | 341.40.12.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SwiftTLS.framework/SwiftTLS` | 171.40.10.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SwiftUIAccessibility.framework/SwiftUIAccessibility` | 3245.8.9.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SwiftUITracingSupport.framework/SwiftUITracingSupport` | 87.0.0.0.0 | not generated |
| [`/System/Library/PrivateFrameworks/SymptomBasebandChannel.framework/SymptomBasebandChannel`](System__Library__PrivateFrameworks__SymptomBasebandChannel.framework__SymptomBasebandChannel.md) | 2394.40.17.0.0 | full |
| `/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter` | 469.40.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SymptomLinkAdvisory.framework/SymptomLinkAdvisory` | 2394.40.17.0.0 | not generated |
| [`/System/Library/PrivateFrameworks/SymptomLinkAdvisoryAOPShim.framework/SymptomLinkAdvisoryAOPShim`](System__Library__PrivateFrameworks__SymptomLinkAdvisoryAOPShim.framework__SymptomLinkAdvisoryAOPShim.md) | 251.40.7.0.0 | full |
| `/System/Library/PrivateFrameworks/SymptomReporter.framework/SymptomReporter` | 2394.40.17.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/ManagedEvent.framework/ManagedEvent` | 2394.40.17.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationLite.framework/SymptomPresentationLite` | 2394.40.17.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SyncedDefaultsDaemon.framework/SyncedDefaultsDaemon` | 2720.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SystemAperture.framework/SystemAperture` | 101.100.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SystemApertureUI.framework/SystemApertureUI` | 101.100.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SystemIntentsSupport.framework/SystemIntentsSupport` | 18.1.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SystemPaperPresentation.framework/SystemPaperPresentation` | 3001.42.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SystemStatusServer.framework/SystemStatusServer` | 288.1.6.0.2 | not generated |
| `/System/Library/PrivateFrameworks/SystemUIAnimationKit.framework/SystemUIAnimationKit` | 104.100.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SystemUISecureFlipBookUtilities.framework/SystemUISecureFlipBookUtilities` | 104.100.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SystemUITraits.framework/SystemUITraits` | 9.1.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SystemUIWindowingKit.framework/SystemUIWindowingKit` | 104.100.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/SystemVoiceAssistantServices.framework/SystemVoiceAssistantServices` | 3605.23.2.3.0 | not generated |
| `/System/Library/PrivateFrameworks/SystemWake.framework/SystemWake` | 827.2.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TCCAuthorizationService.framework/TCCAuthorizationService` | 921.0.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TDGSharing.framework/TDGSharing` | 42.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TSReading.framework/TSReading` | 801.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TSUtility.framework/TSUtility` | 801.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TVLatency.framework/TVLatency` | 179.10.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TVMLKit.framework/TVMLKit` | 1151.10.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TVPlayback.framework/TVPlayback` | 635.10.15.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore` | 627.11.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI` | 627.11.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TVUIKit.framework/TVUIKit` | 182.10.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TailspinSymbolication.framework/TailspinSymbolication` | 268.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TeaSettings.framework/TeaSettings` | 1517.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TeaSnappy.framework/TeaSnappy` | 1517.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TeaState.framework/TeaState` | 1517.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TeaTemplate.framework/TeaTemplate` | 1517.1.0.0.0 | not generated |
| [`/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/TelephonyBlastDoorSupport`](System__Library__PrivateFrameworks__TelephonyBlastDoorSupport.framework__TelephonyBlastDoorSupport.md) | 331.200.71.0.0 | full |
| [`/System/Library/PrivateFrameworks/TelephonyCoreUtils.framework/TelephonyCoreUtils`](System__Library__PrivateFrameworks__TelephonyCoreUtils.framework__TelephonyCoreUtils.md) | 6575.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/TelephonyKit.framework/TelephonyKit`](System__Library__PrivateFrameworks__TelephonyKit.framework__TelephonyKit.md) | 1441.52.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) | 410.200.41.21.1 | full |
| [`/System/Library/PrivateFrameworks/TelephonyRPC.framework/TelephonyRPC`](System__Library__PrivateFrameworks__TelephonyRPC.framework__TelephonyRPC.md) | 1161.1.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/TelephonyXPCClient.framework/TelephonyXPCClient`](System__Library__PrivateFrameworks__TelephonyXPCClient.framework__TelephonyXPCClient.md) | 6575.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/TelephonyXPCServer.framework/TelephonyXPCServer`](System__Library__PrivateFrameworks__TelephonyXPCServer.framework__TelephonyXPCServer.md) | 6575.0.0.0.0 | full |
| `/System/Library/PrivateFrameworks/TerminalToolKit.framework/TerminalToolKit` | 158.200.81.21.9 | not generated |
| `/System/Library/PrivateFrameworks/TestFlightCore.framework/TestFlightCore` | 4.5.14.0.0 | not generated |
| [`/System/Library/PrivateFrameworks/TextComposerRuntime.framework/TextComposerRuntime`](System__Library__PrivateFrameworks__TextComposerRuntime.framework__TextComposerRuntime.md) | 211.37.1.0.0 | full |
| `/System/Library/PrivateFrameworks/TextFormattingUI.framework/TextFormattingUI` | 9127.1.13.13.0 | not generated |
| `/System/Library/PrivateFrameworks/TextGeneration.framework/TextGeneration` | 8.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextGenerationInference.framework/TextGenerationInference` | 8.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextInputCJK.framework/TextInputCJK` | 3568.1.8.600.0 | not generated |
| `/System/Library/PrivateFrameworks/TextInputCore.framework/Support/StickersSearchCore.framework/StickersSearchCore` | 3568.1.8.600.0 | not generated |
| `/System/Library/PrivateFrameworks/TextInputSwift.framework/TextInputSwift` | 3568.1.8.600.0 | not generated |
| `/System/Library/PrivateFrameworks/TextInputTestingKit.framework/TextInputTestingKit` | 3568.1.8.600.0 | not generated |
| `/System/Library/PrivateFrameworks/TextToSpeechBundleSupport.framework/TextToSpeechBundleSupport` | 727.3.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/chs.dylib` | 683.2.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/chsrom.dylib` | 683.2.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/cht.dylib` | 683.2.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/chtrom.dylib` | 683.2.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/deu.dylib` | 683.2.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/eci.dylib` | 683.2.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/eng.dylib` | 683.2.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/enu.dylib` | 683.2.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/esm.dylib` | 683.2.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/esp.dylib` | 683.2.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/fin.dylib` | 683.2.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/fra.dylib` | 683.2.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/frc.dylib` | 683.2.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/ita.dylib` | 683.2.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/jpn.dylib` | 683.2.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/jpnrom.dylib` | 683.2.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/kor.dylib` | 683.2.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/korrom.dylib` | 683.2.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Frameworks/ptb.dylib` | 683.2.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/TextToSpeechMauiSupport` | 683.2.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingUI.framework/TextToSpeechVoiceBankingUI` | 727.3.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextUnderstandingFoundation.framework/TextUnderstandingFoundation` | 192.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextUnderstandingShared.framework/TextUnderstandingShared` | 192.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TextureIO.framework/TextureIO` | 3.10.12.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ThirdPartyApplicationSettings.framework/ThirdPartyApplicationSettings` | 2027.0.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ThreatNotification.framework/ThreatNotification` | 46.0.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ThreatNotificationCore.framework/ThreatNotificationCore` | 46.0.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ThreatNotificationUI.framework/ThreatNotificationUI` | 46.0.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ThumbnailsBlastDoorSupport.framework/ThumbnailsBlastDoorSupport` | 331.200.71.0.0 | not generated |
| [`/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam`](System__Library__PrivateFrameworks__Tightbeam.framework__Tightbeam.md) | 631.40.4.0.0 | full |
| `/System/Library/PrivateFrameworks/TimeAppServices.framework/TimeAppServices` | 354.2.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Timeline.framework/Timeline` | 22.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TimerAppIntents.framework/TimerAppIntents` | 308.2.7.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TinCanShared.framework/TinCanShared` | 247.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TipKitServices.framework/TipKitServices` | 129.1.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TipsFoundation.framework/TipsFoundation` | 866.2.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TipsTryIt.framework/TipsTryIt` | 866.2.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TokenGenerationInference.framework/TokenGenerationInference` | 307.12.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ToolRenderer.framework/ToolRenderer` | 5114.0.12.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TouchAccommodations.framework/TouchAccommodations` | 3245.8.9.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TouchML.framework/TouchML` | 1.0.31.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TouchRemote.framework/TouchRemote` | 210.10.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TrackingAvoidance.framework/TrackingAvoidance` | 107.0.26.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TrackpadAndMouseSupport.framework/TrackpadAndMouseSupport` | 2027.1.7.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TraitsArbiter.framework/TraitsArbiter` | 3.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TranslationAPISupport.framework/TranslationAPISupport` | 396.2.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TranslationPersistence.framework/TranslationPersistence` | 396.2.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TranslationUI.framework/TranslationUI` | 396.2.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TranslationUIServices.framework/TranslationUIServices` | 396.2.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Transliteration.framework/Transliteration` | 45.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TransparencyDetailsView.framework/TransparencyDetailsView` | 638.2.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TransparencyUI.framework/TransparencyUI` | 1766.40.58.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Trial.framework/Trial` | 511.1.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TrialProto.framework/TrialProto` | 511.1.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer` | 511.1.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TrustedClockingServices.framework/TrustedClockingServices` | 95.202.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TrustedPeers.framework/TrustedPeers` | 62460.40.78.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TuriCore.framework/TuriCore` | 370.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TurnManagerService.framework/TurnManagerService` | 3605.4.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TypistFramework.framework/TypistFramework` | 501.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/TypologyAccess.framework/TypologyAccess` | 3568.1.8.600.0 | not generated |
| `/System/Library/PrivateFrameworks/UARPAssetManager.framework/UARPAssetManager` | 1587.40.33.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UARPKit.framework/UARPKit` | 1587.40.33.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UARPUpdaterService.framework/UARPUpdaterService` | 1587.40.33.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UARPiCloud.framework/UARPiCloud` | 1587.40.33.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UIGrounding.framework/UIGrounding` | 39.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UIIntelligenceIntents.framework/UIIntelligenceIntents` | 9127.1.13.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UIIntelligenceInteraction.framework/UIIntelligenceInteraction` | 9127.1.13.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UITriggerVC.framework/UITriggerVC` | 1115.1.11.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UIUnderstanding.framework/UIUnderstanding` | 2.8.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ULPNHeuristicsClientFramework.framework/ULPNHeuristicsClientFramework` | 251.40.7.0.0 | not generated |
| `/System/Library/PrivateFrameworks/URLCompression.framework/URLCompression` | 1021.3.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/URLFormatting.framework/URLFormatting` | 317.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/USDLib_FormatLoaderProxy.framework/USDLib_FormatLoaderProxy` | 24.1.32.0.0 | not generated |
| `/System/Library/PrivateFrameworks/USDObjCKit.framework/USDObjCKit` | 59.2.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UVFSXPCService.framework/UVFSXPCService` | 764.40.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UnblockClient.framework/UnblockClient` | 18.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UnilogCommonLibrary.framework/UnilogCommonLibrary` | 2.1.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UnilogConfig.framework/UnilogConfig` | 7.5.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UnilogCoordination.framework/UnilogCoordination` | 3.3.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UnilogIngestion.framework/UnilogIngestion` | 3.3.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UnilogInstrumentation.framework/UnilogInstrumentation` | 2.1.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UnilogMailSearchLibrary.framework/UnilogMailSearchLibrary` | 2.1.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UnilogPlatformLibrary.framework/UnilogPlatformLibrary` | 2.1.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UnilogSchemaManifest.framework/UnilogSchemaManifest` | 2.1.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UnilogStreamAlgorithms.framework/UnilogStreamAlgorithms` | 3.3.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UnityPoster.framework/UnityPoster` | 51.2.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UniversalDrag.framework/UniversalDrag` | 29.0.0.0.0 | not generated |
| [`/System/Library/PrivateFrameworks/UniversalHID.framework/UniversalHID`](System__Library__PrivateFrameworks__UniversalHID.framework__UniversalHID.md) | 94.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/UniversalHIDKit.framework/UniversalHIDKit`](System__Library__PrivateFrameworks__UniversalHIDKit.framework__UniversalHIDKit.md) | 94.0.0.0.0 | full |
| `/System/Library/PrivateFrameworks/UpdateCycle.framework/UpdateCycle` | 9127.1.13.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UpdateCycleSupport.framework/UpdateCycleSupport` | 9127.1.13.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UrchinKit.framework/UrchinKit` | 178.2.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UserAlerts.framework/UserAlerts` | 14.7.0.0.0 | not generated |
| `/usr/lib/objc/libobjcMsgSend31.dylib` | 973.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UnifiedMessagingKit.framework/UnifiedMessagingKit` | 3.1.16.2.2 | not generated |
| `/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTracking` | 407.1.5.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/liblivefiles.plugin.dummy.dylib` | 764.40.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib` | 3288.52.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_cs.dylib` | 753.42.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_exfat.dylib` | 561.40.5.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_hfs.dylib` | 753.42.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_msdos.dylib` | 845.40.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_ntfs.dylib` | 171.40.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UserFS.framework/UserFS` | 764.40.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UserManagementLayout.framework/UserManagementLayout` | 490.0.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UserManagementUI.framework/UserManagementUI` | 490.0.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UserNotificationsSettings.framework/UserNotificationsSettings` | 720.2.7.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UserNotificationsTranslation.framework/UserNotificationsTranslation` | 720.2.7.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UserProfilesCore.framework/UserProfilesCore` | 299.10.21.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UserSafety.framework/UserSafety` | 151.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/UserSafetyUI.framework/UserSafetyUI` | 151.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/VDAF.framework/VDAF` | 35.5.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/VFXAssets.framework/VFXAssets` | 45.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/VFXBase.framework/VFXBase` | 233.40.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/VideoEffect.framework/VideoEffect` | 3.7.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/VideoIntelligence.framework/VideoIntelligence` | 33.13.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/VideoSubscriberAccountUI.framework/VideoSubscriberAccountUI` | 609.10.3.0.0 | not generated |
| [`/System/Library/PrivateFrameworks/VideoToolboxParavirtualizationSupport.framework/VideoToolboxParavirtualizationSupport`](System__Library__PrivateFrameworks__VideoToolboxParavirtualizationSupport.framework__VideoToolboxParavirtualizationSupport.md) | 71.0.14.0.0 | full |
| `/System/Library/PrivateFrameworks/VideosUICore.framework/VideosUICore` | 1145.11.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/VirtualGarage.framework/VirtualGarage` | 2436.31.9.18.102 | not generated |
| `/System/Library/PrivateFrameworks/Visage.framework/Visage` | 279.0.13.0.0 | not generated |
| `/System/Library/PrivateFrameworks/VisionCompanion.framework/VisionCompanion` | 35.40.6.0.0 | not generated |
| `/System/Library/PrivateFrameworks/VisionCompanionServices.framework/VisionCompanionServices` | 35.40.6.0.0 | not generated |
| `/System/Library/PrivateFrameworks/VisionHWAccelerationServices.framework/VisionHWAccelerationServices` | 4.4.14.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Vista.framework/Vista` | 20.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/VisualActionPrediction.framework/VisualActionPrediction` | 678.0.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/VisualActionPredictionCore.framework/VisualActionPredictionCore` | 678.0.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/VisualActionPredictionSupport.framework/VisualActionPredictionSupport` | 678.0.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/VisualAlert.framework/VisualAlert` | 3245.8.9.0.0 | not generated |
| [`/System/Library/PrivateFrameworks/VisualIntelligenceCameraSupport.framework/VisualIntelligenceCameraSupport`](System__Library__PrivateFrameworks__VisualIntelligenceCameraSupport.framework__VisualIntelligenceCameraSupport.md) | 246.1.29.1.0 | full |
| `/System/Library/PrivateFrameworks/VisualIntelligenceCore.framework/VisualIntelligenceCore` | 246.1.29.1.0 | not generated |
| `/System/Library/PrivateFrameworks/VisualIntelligenceCoreDDSupport.framework/VisualIntelligenceCoreDDSupport` | 246.1.29.1.0 | not generated |
| `/System/Library/PrivateFrameworks/VisualIntelligenceServices.framework/VisualIntelligenceServices` | 246.1.29.1.0 | not generated |
| `/System/Library/PrivateFrameworks/VisualIntelligenceUI.framework/VisualIntelligenceUI` | 246.1.29.1.0 | not generated |
| `/System/Library/PrivateFrameworks/VisualLogger.framework/VisualLogger` | 9.26.7.9.0 | not generated |
| `/System/Library/PrivateFrameworks/VisualMappingKit.framework/VisualMappingKit` | 9.26.5.12.5 | not generated |
| `/System/Library/PrivateFrameworks/VisualMediaRetrieval.framework/VisualMediaRetrieval` | 916.62.154.0.0 | not generated |
| `/System/Library/PrivateFrameworks/VisualPairing.framework/VisualPairing` | 205.200.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/VisualVoicemail.framework/IMAP.framework/IMAP` | 958.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/VisualVoicemail.framework/VisualVoicemail` | 958.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/VoiceActions.framework/VoiceActions` | 99.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/VoiceControl.framework/VoiceControl` | 41.1.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/VoiceControlUI.framework/VoiceControlUI` | 41.1.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos` | 1446.1.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/VoiceOverServices.framework/VoiceOverServices` | 3245.8.9.0.0 | not generated |
| `/System/Library/PrivateFrameworks/VoiceShortcutsUICardKitProviderSupport.framework/VoiceShortcutsUICardKitProviderSupport` | 3605.23.2.3.0 | not generated |
| [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) | 3605.8.2.0.0 | full |
| `/System/Library/PrivateFrameworks/VoicemailStore.framework/VoicemailStore` | 958.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon` | 2701.7.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WalletBlastDoorSupport.framework/WalletBlastDoorSupport` | 331.200.71.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WatchControlAssets.framework/WatchControlAssets` | 199.1.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WatchControlSettings.framework/WatchControlSettings` | 199.1.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/WatchFacesWallpaperSupport` | 2483.561.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit` | 952.10.8.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WatchQuickActionsServices.framework/WatchQuickActionsServices` | 199.1.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WatchReplies.framework/WatchReplies` | 86.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WatchdogClient.framework/WatchdogClient` | 334.40.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WatchdogServiceManagement.framework/WatchdogServiceManagement` | 334.40.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Weather.framework/Weather` | 1820.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WeatherData.framework/WeatherData` | 1474.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WeatherFoundation.framework/WeatherFoundation` | 560.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WeatherResources.framework/WeatherResources` | 1474.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Weave.framework/Weave` | 8.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WebApp.framework/WebApp` | 625.2.8.21.5 | not generated |
| `/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks` | 625.2.8.21.5 | not generated |
| `/System/Library/PrivateFrameworks/WebBookmarksSwift.framework/WebBookmarksSwift` | 7625.2.8.21.6 | not generated |
| `/System/Library/PrivateFrameworks/WebContentAnalysis.framework/WebContentAnalysis` | 56.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WebContentRestrictions.framework/WebContentRestrictions` | 77.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libANGLE-shared.dylib` | 625.2.8.21.2 | not generated |
| `/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib` | 625.2.8.21.2 | not generated |
| `/System/Library/PrivateFrameworks/WebInspector.framework/WebInspector` | 7625.2.8.21.6 | not generated |
| `/System/Library/PrivateFrameworks/WebSheet.framework/WebSheet` | 337.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/Welcome.framework/Welcome` | 34.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WelcomeKit.framework/WelcomeKit` | 1441.52.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WelcomeKitCore.framework/WelcomeKitCore` | 1441.52.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WelcomeKitUI.framework/WelcomeKitUI` | 1441.52.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WellnessUI.framework/WellnessUI` | 3605.11.1.11.1 | not generated |
| [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) | 827.3.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/WiFiCloudSyncEngine.framework/WiFiCloudSyncEngine`](System__Library__PrivateFrameworks__WiFiCloudSyncEngine.framework__WiFiCloudSyncEngine.md) | 865.9.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) | 1207.9.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) | 1207.9.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/WiFiLogCapture.framework/WiFiLogCapture`](System__Library__PrivateFrameworks__WiFiLogCapture.framework__WiFiLogCapture.md) | 1185.8.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) | 887.9.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/WiFiSettingsKit.framework/WiFiSettingsKit`](System__Library__PrivateFrameworks__WiFiSettingsKit.framework__WiFiSettingsKit.md) | 1207.9.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) | 1190.20.0.0.0 | full |
| `/System/Library/PrivateFrameworks/Widgets.framework/Widgets` | 308.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WirelessCoexManager.framework/WirelessCoexManager` | 1950.4.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WirelessDiagnostics.framework/WirelessDiagnostics` | 998.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WirelessProximity.framework/WirelessProximity` | 2701.7.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WorkflowEditor.framework/WorkflowEditor` | 5114.0.12.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WorkflowUI.framework/WorkflowUI` | 5114.0.12.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WorkflowUICore.framework/WorkflowUICore` | 5114.0.12.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/WorkoutAnnouncements` | 3605.11.1.11.1 | not generated |
| `/System/Library/PrivateFrameworks/WorkoutHealthBridge.framework/WorkoutHealthBridge` | 2027.1.63.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WorkoutKitServices.framework/WorkoutKitServices` | 2027.1.63.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WorkoutKitUI.framework/WorkoutKitUI` | 2027.1.63.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WorldAwareSpatialAudio.framework/WorldAwareSpatialAudio` | 47.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WorldClockAppIntents.framework/WorldClockAppIntents` | 308.2.7.0.0 | not generated |
| `/System/Library/PrivateFrameworks/WritingToolsUI.framework/WritingToolsUI` | 151.1.11.100.0 | not generated |
| `/System/Library/PrivateFrameworks/XCTTargetBootstrap.framework/XCTTargetBootstrap` | 25427.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/XGBoostFramework.framework/XGBoostFramework` | 3600.25.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/XOJIT.framework/XOJIT` | 84.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/XOJITExecutor.framework/XOJITExecutor` | 84.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/XavierCore.framework/XavierCore` | 5971.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/XavierNews.framework/XavierNews` | 5971.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ZeoliteFramework.framework/ZeoliteFramework` | 1.7.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ZeoliteLanguage.framework/ZeoliteLanguage` | 1.7.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/ZoomServices.framework/ZoomServices` | 3245.8.9.0.0 | not generated |
| `/System/Library/PrivateFrameworks/_AppIntentsServices_AppIntents.framework/_AppIntentsServices_AppIntents` | 41.1.16.1.103 | not generated |
| `/System/Library/PrivateFrameworks/_AppIntentsServices_ToolKit.framework/_AppIntentsServices_ToolKit` | 41.1.16.1.103 | not generated |
| `/System/Library/PrivateFrameworks/_Coherence_CloudKit_Private.framework/_Coherence_CloudKit_Private` | 241.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/_CommunicationsUICore_PosterBoardServices.framework/_CommunicationsUICore_PosterBoardServices` | 158.200.81.21.9 | not generated |
| `/System/Library/PrivateFrameworks/_DeviceExpertIntents_AppIntents.framework/_DeviceExpertIntents_AppIntents` | 3605.6.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/_FlowToolTypes_AppIntents.framework/_FlowToolTypes_AppIntents` | 3605.31.1.11.2 | not generated |
| `/System/Library/PrivateFrameworks/_FoundationModels_AppIntents.framework/_FoundationModels_AppIntents` | 2.1.14.0.0 | not generated |
| `/System/Library/PrivateFrameworks/_GeoServices_GeoToolbox.framework/_GeoServices_GeoToolbox` | 34.31.6.17.106 | not generated |
| [`/System/Library/PrivateFrameworks/_GeoToolbox_CoreLocation.framework/_GeoToolbox_CoreLocation`](System__Library__PrivateFrameworks___GeoToolbox_CoreLocation.framework___GeoToolbox_CoreLocation.md) | 34.31.6.17.106 | full |
| `/System/Library/PrivateFrameworks/_JetUI_SwiftUI.framework/_JetUI_SwiftUI` | 10.1.11.0.0 | not generated |
| `/System/Library/PrivateFrameworks/_MusicKitInternal_MediaPlaybackCore.framework/_MusicKitInternal_MediaPlaybackCore` | 4026.210.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/_MusicKitInternal_MediaPlayer.framework/_MusicKitInternal_MediaPlayer` | 4026.210.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/_NearField_ExtensionFoundation.framework/_NearField_ExtensionFoundation` | 371.8.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/_OnDeviceStorage_JetEngine.framework/_OnDeviceStorage_JetEngine` | 3.1.15.0.0 | not generated |
| `/System/Library/PrivateFrameworks/_PhotosUIPrivate_SwiftUI.framework/_PhotosUIPrivate_SwiftUI` | 916.62.154.0.0 | not generated |
| `/System/Library/PrivateFrameworks/_SonicKit_MusicKit.framework/_SonicKit_MusicKit` | 26210.26.40.301.0 | not generated |
| `/System/Library/PrivateFrameworks/_SwiftMedia_SwiftUI.framework/_SwiftMedia_SwiftUI` | 70.10.1.1.0 | not generated |
| `/System/Library/PrivateFrameworks/_ToneKit_SwiftUI.framework/_ToneKit_SwiftUI` | 675.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/_ToolKit_AppIntents.framework/_ToolKit_AppIntents` | 5114.0.12.0.0 | not generated |
| `/System/Library/PrivateFrameworks/apfs_boot_mount.framework/apfs_boot_mount` | 3288.52.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/caulk.framework/caulk` | 247.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iCalendar.framework/iCalendar` | 1178.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iCloudCalendarUnifiedSettings.framework/iCloudCalendarUnifiedSettings` | 2027.1.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore` | 5168.40.162.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iCloudDriveService.framework/iCloudDriveService` | 5168.40.162.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iCloudMailAccountUI.framework/iCloudMailAccountUI` | 2027.1.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iCloudMailUnifiedSettings.framework/iCloudMailUnifiedSettings` | 2027.1.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iCloudNotification.framework/iCloudNotification` | 301.24.1.5.0 | not generated |
| `/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota` | 301.24.1.5.0 | not generated |
| [`/System/Library/PrivateFrameworks/iCloudQuotaNetworking.framework/iCloudQuotaNetworking`](System__Library__PrivateFrameworks__iCloudQuotaNetworking.framework__iCloudQuotaNetworking.md) | 301.24.1.5.0 | full |
| [`/System/Library/PrivateFrameworks/iCloudQuotaNetworkingCore.framework/iCloudQuotaNetworkingCore`](System__Library__PrivateFrameworks__iCloudQuotaNetworkingCore.framework__iCloudQuotaNetworkingCore.md) | 301.24.1.5.0 | full |
| `/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI` | 301.24.1.5.0 | not generated |
| `/System/Library/PrivateFrameworks/iCloudSettings.framework/iCloudSettings` | 301.24.1.6.0 | not generated |
| `/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerClient.framework/iCloudSubscriptionOptimizerClient` | 74.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerCore.framework/iCloudSubscriptionOptimizerCore` | 74.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerLighthouse.framework/iCloudSubscriptionOptimizerLighthouse` | 74.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerPFLTraining.framework/iCloudSubscriptionOptimizerPFLTraining` | 74.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iCloudWebData.framework/iCloudWebData` | 71.3.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iCloudWebSupport.framework/iCloudWebSupport` | 71.3.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iCloudWebUI.framework/iCloudWebUI` | 71.3.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iMessageApps.framework/iMessageApps` | 1491.200.101.21.5 | not generated |
| `/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iOSDiagnostics` | 1374.42.1.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iOSScreenSharing.framework/iOSScreenSharing` | 166.13.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iTunesStore.framework/iTunesStore` | 1453.1.1.2.2 | not generated |
| `/System/Library/PrivateFrameworks/iTunesStoreUI.framework/iTunesStoreUI` | 1203.1.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/EquationKit.framework/EquationKit` | 488.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/KeynoteQuicklook.framework/KeynoteQuicklook` | 488.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/NumbersQuicklook.framework/NumbersQuicklook` | 488.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/PagesQuicklook.framework/PagesQuicklook` | 488.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TQQuicklook.framework/TQQuicklook` | 488.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSApplication.framework/TSApplication` | 488.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSCalculationEngine.framework/TSCalculationEngine` | 488.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSCharts.framework/TSCharts` | 488.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSCollaborationKit.framework/TSCollaborationKit` | 488.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSKit.framework/TSKit` | 488.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSStyles.framework/TSStyles` | 488.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iWorkXPC.framework/iWorkXPC` | 31.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/kperf.framework/kperf` | 164.0.2.0.0 | not generated |
| `/System/Library/PrivateFrameworks/kperfdata.framework/kperfdata` | 164.0.2.0.0 | not generated |
| `/usr/lib/objc/libobjcMsgSend32.dylib` | 973.1.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSDrawables.framework/TSDrawables` | 488.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSPersistence.framework/TSPersistence` | 488.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSTables.framework/TSTables` | 488.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSText.framework/TSText` | 488.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSUtility.framework/TSUtility` | 488.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/libEDR.framework/libEDR` | 70.0.0.0.0 | not generated |
| [`/System/Library/PrivateFrameworks/libmalloc_exclaves_introspector.framework/libmalloc_exclaves_introspector`](System__Library__PrivateFrameworks__libmalloc_exclaves_introspector.framework__libmalloc_exclaves_introspector.md) | 886.40.15.0.0 | full |
| `/System/Library/PrivateFrameworks/libsat.framework/libsat` | 122.0.0.0.1 | not generated |
| `/System/Library/PrivateFrameworks/lighthouse_runtime.framework/lighthouse_runtime` | 6.1.3.0.0 | not generated |
| `/System/Library/PrivateFrameworks/oncrpc.framework/oncrpc` | 94.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/perfdata.framework/perfdata` | 135.40.4.0.0 | not generated |
| `/System/Library/PrivateFrameworks/shared_cache_page_prewarming.framework/shared_cache_page_prewarming` | 10.0.0.0.0 | not generated |
| `/System/Library/PrivateFrameworks/vCard.framework/vCard` | 3846.200.91.2.1 | not generated |
| `/System/Library/ProceduralWallpaper/ProceduralWallpapers.bundle/ProceduralWallpapers` | 147.0.0.0.0 | not generated |
| `/System/Library/SecureAnalytics/integrityDiagnose/integrityDiagnose.bundle/universal.bundle/main/main_mlc/model.dylib` | 3.0.7.0.0 | not generated |
| `/System/Library/SubFrameworks/ARKitCore.framework/ARKitCore` | 781.40.6.0.0 | not generated |
| `/System/Library/SubFrameworks/ARKitFoundation.framework/ARKitFoundation` | 781.40.6.0.0 | not generated |
| `/System/Library/SubFrameworks/ARKitUI.framework/ARKitUI` | 781.40.6.0.0 | not generated |
| `/System/Library/SubFrameworks/CoreAIAsset.framework/CoreAIAsset` | 3605.6.4.0.0 | not generated |
| `/System/Library/SubFrameworks/CoreAICache.framework/CoreAICache` | 3605.6.4.0.0 | not generated |
| `/System/Library/SubFrameworks/CoreAICommon.framework/CoreAICommon` | 3605.6.4.0.0 | not generated |
| `/System/Library/SubFrameworks/CoreAICompiler.framework/CoreAICompiler` | 3605.6.4.0.0 | not generated |
| `/System/Library/SubFrameworks/CoreAICompiler.framework/Frameworks/libODIECompiler.dylib` | 3605.6.4.0.0 | not generated |
| `/System/Library/SubFrameworks/CoreAIDelegates.framework/CoreAIDelegates` | 3605.6.4.0.0 | not generated |
| `/System/Library/SubFrameworks/CoreAIRuntime.framework/CoreAIRuntime` | 3605.6.4.0.0 | not generated |
| `/System/Library/SubFrameworks/FocusEngine.framework/FocusEngine` | 9127.1.13.13.0 | not generated |
| `/System/Library/SubFrameworks/RealityCoreDeformation.framework/RealityCoreDeformation` | 23.40.1.0.0 | not generated |
| `/System/Library/SubFrameworks/RealityCoreRenderer.framework/RealityCoreRenderer` | 24.40.1.0.0 | not generated |
| `/System/Library/SubFrameworks/RealityCoreTextureProcessing.framework/RealityCoreTextureProcessing` | 24.40.1.0.0 | not generated |
| `/System/Library/SubFrameworks/RealityFoundationCloth.framework/RealityFoundationCloth` | 453.42.1.0.1 | not generated |
| `/System/Library/SubFrameworks/ShaderGraph.framework/ShaderGraph` | 159.40.2.0.0 | not generated |
| `/System/Library/SubFrameworks/UIUtilities.framework/UIUtilities` | 9127.1.13.13.0 | not generated |
| `/System/Library/SystemConfiguration/CaptiveNetworkSupport.bundle/CaptiveNetworkSupport` | 545.40.1.0.0 | not generated |
| `/System/Library/TextInput/TextInput_ar.bundle/TextInput_ar` | 3568.1.8.600.0 | not generated |
| `/System/Library/TextInput/TextInput_bn.bundle/TextInput_bn` | 3568.1.8.600.0 | not generated |
| `/System/Library/TextInput/TextInput_bo.bundle/TextInput_bo` | 3568.1.8.600.0 | not generated |
| `/System/Library/TextInput/TextInput_ca.bundle/TextInput_ca` | 3568.1.8.600.0 | not generated |
| `/System/Library/TextInput/TextInput_chr.bundle/TextInput_chr` | 3568.1.8.600.0 | not generated |
| `/System/Library/TextInput/TextInput_cs.bundle/TextInput_cs` | 3568.1.8.600.0 | not generated |
| `/System/Library/TextInput/TextInput_de.bundle/TextInput_de` | 3568.1.8.600.0 | not generated |
| `/System/Library/TextInput/TextInput_el.bundle/TextInput_el` | 3568.1.8.600.0 | not generated |
| `/System/Library/TextInput/TextInput_emoji.bundle/TextInput_emoji` | 3568.1.8.600.0 | not generated |
| [`/System/Library/TextInput/TextInput_en.bundle/TextInput_en`](System__Library__TextInput__TextInput_en.bundle__TextInput_en.md) | 3568.1.8.600.0 | light |
| [`/System/Library/TextInput/TextInput_es.bundle/TextInput_es`](System__Library__TextInput__TextInput_es.bundle__TextInput_es.md) | 3568.1.8.600.0 | light |
| [`/System/Library/TextInput/TextInput_fr.bundle/TextInput_fr`](System__Library__TextInput__TextInput_fr.bundle__TextInput_fr.md) | 3568.1.8.600.0 | light |
| [`/System/Library/TextInput/TextInput_haw.bundle/TextInput_haw`](System__Library__TextInput__TextInput_haw.bundle__TextInput_haw.md) | 3568.1.8.600.0 | light |
| [`/System/Library/TextInput/TextInput_he.bundle/TextInput_he`](System__Library__TextInput__TextInput_he.bundle__TextInput_he.md) | 3568.1.8.600.0 | light |
| [`/System/Library/TextInput/TextInput_hi.bundle/TextInput_hi`](System__Library__TextInput__TextInput_hi.bundle__TextInput_hi.md) | 3568.1.8.600.0 | light |
| [`/System/Library/TextInput/TextInput_intl.bundle/TextInput_intl`](System__Library__TextInput__TextInput_intl.bundle__TextInput_intl.md) | 3568.1.8.600.0 | light |
| [`/System/Library/TextInput/TextInput_ja.bundle/TextInput_ja`](System__Library__TextInput__TextInput_ja.bundle__TextInput_ja.md) | 3568.1.8.600.0 | light |
| [`/System/Library/TextInput/TextInput_ko.bundle/TextInput_ko`](System__Library__TextInput__TextInput_ko.bundle__TextInput_ko.md) | 3568.1.8.600.0 | light |
| [`/System/Library/TextInput/TextInput_mr.bundle/TextInput_mr`](System__Library__TextInput__TextInput_mr.bundle__TextInput_mr.md) | 3568.1.8.600.0 | light |
| [`/System/Library/TextInput/TextInput_mul.bundle/TextInput_mul`](System__Library__TextInput__TextInput_mul.bundle__TextInput_mul.md) | 3568.1.8.600.0 | light |
| [`/System/Library/TextInput/TextInput_my.bundle/TextInput_my`](System__Library__TextInput__TextInput_my.bundle__TextInput_my.md) | 3568.1.8.600.0 | light |
| [`/System/Library/TextInput/TextInput_nl.bundle/TextInput_nl`](System__Library__TextInput__TextInput_nl.bundle__TextInput_nl.md) | 3568.1.8.600.0 | light |
| [`/System/Library/TextInput/TextInput_pa.bundle/TextInput_pa`](System__Library__TextInput__TextInput_pa.bundle__TextInput_pa.md) | 3568.1.8.600.0 | light |
| [`/System/Library/TextInput/TextInput_pt.bundle/TextInput_pt`](System__Library__TextInput__TextInput_pt.bundle__TextInput_pt.md) | 3568.1.8.600.0 | light |
| [`/System/Library/TextInput/TextInput_si.bundle/TextInput_si`](System__Library__TextInput__TextInput_si.bundle__TextInput_si.md) | 3568.1.8.600.0 | light |
| [`/System/Library/TextInput/TextInput_sk.bundle/TextInput_sk`](System__Library__TextInput__TextInput_sk.bundle__TextInput_sk.md) | 3568.1.8.600.0 | light |
| [`/System/Library/TextInput/TextInput_sl.bundle/TextInput_sl`](System__Library__TextInput__TextInput_sl.bundle__TextInput_sl.md) | 3568.1.8.600.0 | light |
| [`/System/Library/TextInput/TextInput_ta.bundle/TextInput_ta`](System__Library__TextInput__TextInput_ta.bundle__TextInput_ta.md) | 3568.1.8.600.0 | light |
| [`/System/Library/TextInput/TextInput_th.bundle/TextInput_th`](System__Library__TextInput__TextInput_th.bundle__TextInput_th.md) | 3568.1.8.600.0 | light |
| [`/System/Library/TextInput/TextInput_tr.bundle/TextInput_tr`](System__Library__TextInput__TextInput_tr.bundle__TextInput_tr.md) | 3568.1.8.600.0 | light |
| [`/System/Library/TextInput/TextInput_ug.bundle/TextInput_ug`](System__Library__TextInput__TextInput_ug.bundle__TextInput_ug.md) | 3568.1.8.600.0 | light |
| [`/System/Library/TextInput/TextInput_vi.bundle/TextInput_vi`](System__Library__TextInput__TextInput_vi.bundle__TextInput_vi.md) | 3568.1.8.600.0 | light |
| [`/System/Library/TextInput/TextInput_yue.bundle/TextInput_yue`](System__Library__TextInput__TextInput_yue.bundle__TextInput_yue.md) | 3568.1.8.600.0 | light |
| [`/System/Library/TextInput/TextInput_zh.bundle/TextInput_zh`](System__Library__TextInput__TextInput_zh.bundle__TextInput_zh.md) | 3568.1.8.600.0 | light |
| [`/System/Library/UserEventPlugins/AppleHDQGasGauge.plugin/AppleHDQGasGauge`](System__Library__UserEventPlugins__AppleHDQGasGauge.plugin__AppleHDQGasGauge.md) | 240.0.0.0.0 | light |
| [`/System/Library/VideoCodecs/ave.videoencoder`](System__Library__VideoCodecs__ave.videoencoder.md) | 913.64.1.0.0 | light |
| [`/System/Library/VideoDecoders/AV1SW.videodecoder`](System__Library__VideoDecoders__AV1SW.videodecoder.md) | 158.5.0.0.0 | light |
| [`/System/Library/VideoDecoders/AppleProResHWDecoder.videodecoder`](System__Library__VideoDecoders__AppleProResHWDecoder.videodecoder.md) | 600.53.0.0.0 | light |
| [`/System/Library/VideoDecoders/AppleProResSWDecoder.videodecoder`](System__Library__VideoDecoders__AppleProResSWDecoder.videodecoder.md) | 60623.0.0.0.0 | light |
| [`/System/Library/VideoDecoders/JPEGH1.videodecoder`](System__Library__VideoDecoders__JPEGH1.videodecoder.md) | 3385.14.1.3.0 | light |
| [`/System/Library/VideoDecoders/VCH263.videodecoder`](System__Library__VideoDecoders__VCH263.videodecoder.md) | 682.4.0.0.0 | light |
| [`/System/Library/VideoDecoders/VCPMP4V.videodecoder`](System__Library__VideoDecoders__VCPMP4V.videodecoder.md) | 746.2.0.0.0 | light |
| [`/System/Library/VideoEncoders/AV1SW.videoencoder`](System__Library__VideoEncoders__AV1SW.videoencoder.md) | 158.5.0.0.0 | light |
| [`/System/Library/VideoEncoders/AppleProResHWEncoder.videoencoder`](System__Library__VideoEncoders__AppleProResHWEncoder.videoencoder.md) | 600.53.0.0.0 | light |
| [`/System/Library/VideoEncoders/AppleProResSWEncoder.videoencoder`](System__Library__VideoEncoders__AppleProResSWEncoder.videoencoder.md) | 60623.0.0.0.0 | light |
| [`/System/Library/VideoEncoders/JPEGH1.videoencoder`](System__Library__VideoEncoders__JPEGH1.videoencoder.md) | 3385.14.1.3.0 | light |
| [`/System/Library/VideoEncoders/VCH263.videoencoder`](System__Library__VideoEncoders__VCH263.videoencoder.md) | 682.4.0.0.0 | light |
| [`/System/Library/VideoProcessors/BarcodeScanner.videoprocessor`](System__Library__VideoProcessors__BarcodeScanner.videoprocessor.md) | 764.42.9.0.0 | light |
| [`/System/Library/VideoProcessors/CCPortrait.bundle/CCPortrait`](System__Library__VideoProcessors__CCPortrait.bundle__CCPortrait.md) | 764.42.9.0.0 | light |
| [`/System/Library/VideoProcessors/CalibrationV1.bundle/CalibrationV1`](System__Library__VideoProcessors__CalibrationV1.bundle__CalibrationV1.md) | 764.42.9.0.0 | light |
| [`/System/Library/VideoProcessors/DepthProcessorV2.bundle/DepthProcessorV2`](System__Library__VideoProcessors__DepthProcessorV2.bundle__DepthProcessorV2.md) | 764.42.9.0.0 | light |
| [`/System/Library/VideoProcessors/DisparityV5.bundle/DisparityV5`](System__Library__VideoProcessors__DisparityV5.bundle__DisparityV5.md) | 764.42.9.0.0 | full |
| [`/System/Library/VideoProcessors/FPDisparityV3.bundle/FPDisparityV3`](System__Library__VideoProcessors__FPDisparityV3.bundle__FPDisparityV3.md) | 764.42.9.0.0 | full |
| [`/System/Library/VideoProcessors/IntelligentDistortionCorrectionV1.bundle/IntelligentDistortionCorrectionV1`](System__Library__VideoProcessors__IntelligentDistortionCorrectionV1.bundle__IntelligentDistortionCorrectionV1.md) | 764.42.9.0.0 | light |
| [`/System/Library/VideoProcessors/MattingV2.bundle/MattingV2`](System__Library__VideoProcessors__MattingV2.bundle__MattingV2.md) | 764.42.9.0.0 | light |
| [`/System/Library/VideoProcessors/MetalFilter.bundle/MetalFilter`](System__Library__VideoProcessors__MetalFilter.bundle__MetalFilter.md) | 764.42.9.0.0 | full |
| [`/System/Library/VideoProcessors/NRFV2.bundle/NRFV2`](System__Library__VideoProcessors__NRFV2.bundle__NRFV2.md) | 764.42.9.0.0 | light |
| [`/System/Library/VideoProcessors/NRFV4.bundle/NRFV4`](System__Library__VideoProcessors__NRFV4.bundle__NRFV4.md) | 764.42.9.0.0 | light |
| [`/System/Library/VideoProcessors/SDOFRenderingV5.bundle/SDOFRenderingV5`](System__Library__VideoProcessors__SDOFRenderingV5.bundle__SDOFRenderingV5.md) | 764.42.9.0.0 | light |
| [`/System/Library/VideoProcessors/STF.bundle/STF`](System__Library__VideoProcessors__STF.bundle__STF.md) | 764.42.9.0.0 | light |
| [`/System/Library/VoiceServices/PlugIns/VoiceDial.vsplugin/VoiceDial`](System__Library__VoiceServices__PlugIns__VoiceDial.vsplugin__VoiceDial.md) | 3079.200.81.21.2 | light |
| [`/usr/lib/ACIPCBTLib.dylib`](usr__lib__ACIPCBTLib.dylib.md) | 197.40.2.0.0 | light |
| [`/usr/lib/AppleConvergedTransport.dylib`](usr__lib__AppleConvergedTransport.dylib.md) | 197.40.2.0.0 | light |
| [`/usr/lib/CarrierBundleUtilities.dylib`](usr__lib__CarrierBundleUtilities.dylib.md) | 106.0.0.0.0 | light |
| [`/usr/lib/i18n/libBIG5.dylib`](usr__lib__i18n__libBIG5.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/i18n/libDECHanyu.dylib`](usr__lib__i18n__libDECHanyu.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/i18n/libDECKanji.dylib`](usr__lib__i18n__libDECKanji.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/i18n/libEUC.dylib`](usr__lib__i18n__libEUC.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/i18n/libEUCTW.dylib`](usr__lib__i18n__libEUCTW.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/i18n/libGBK2K.dylib`](usr__lib__i18n__libGBK2K.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/i18n/libHZ.dylib`](usr__lib__i18n__libHZ.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/i18n/libISO2022.dylib`](usr__lib__i18n__libISO2022.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/i18n/libJOHAB.dylib`](usr__lib__i18n__libJOHAB.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/i18n/libMSKanji.dylib`](usr__lib__i18n__libMSKanji.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/i18n/libUES.dylib`](usr__lib__i18n__libUES.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/i18n/libUTF1632.dylib`](usr__lib__i18n__libUTF1632.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/i18n/libUTF7.dylib`](usr__lib__i18n__libUTF7.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/i18n/libUTF8.dylib`](usr__lib__i18n__libUTF8.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/i18n/libUTF8MAC.dylib`](usr__lib__i18n__libUTF8MAC.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/i18n/libVIQR.dylib`](usr__lib__i18n__libVIQR.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/i18n/libZW.dylib`](usr__lib__i18n__libZW.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/i18n/libiconv_none.dylib`](usr__lib__i18n__libiconv_none.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/i18n/libiconv_std.dylib`](usr__lib__i18n__libiconv_std.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/i18n/libmapper_646.dylib`](usr__lib__i18n__libmapper_646.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/i18n/libmapper_none.dylib`](usr__lib__i18n__libmapper_none.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/i18n/libmapper_parallel.dylib`](usr__lib__i18n__libmapper_parallel.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/i18n/libmapper_serial.dylib`](usr__lib__i18n__libmapper_serial.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/i18n/libmapper_std.dylib`](usr__lib__i18n__libmapper_std.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/i18n/libmapper_zone.dylib`](usr__lib__i18n__libmapper_zone.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/libAHTRestore.dylib`](usr__lib__libAHTRestore.dylib.md) | 10110.1.0.0.0 | light |
| [`/usr/lib/libAONConnection.dylib`](usr__lib__libAONConnection.dylib.md) | 251.40.7.0.0 | light |
| [`/usr/lib/libARIServer.dylib`](usr__lib__libARIServer.dylib.md) | 1640.0.0.0.0 | light |
| [`/usr/lib/libATCommandStudioDynamic.dylib`](usr__lib__libATCommandStudioDynamic.dylib.md) | 1594.0.0.0.0 | light |
| [`/usr/lib/libAWDProtobufBluetooth.dylib`](usr__lib__libAWDProtobufBluetooth.dylib.md) | 7019.0.0.0.0 | full |
| [`/usr/lib/libAWDProtobufFacetime.dylib`](usr__lib__libAWDProtobufFacetime.dylib.md) | 7019.0.0.0.0 | light |
| [`/usr/lib/libAWDProtobufFacetimeiMessage.dylib`](usr__lib__libAWDProtobufFacetimeiMessage.dylib.md) | 7019.0.0.0.0 | light |
| [`/usr/lib/libAWDProtobufGCK.dylib`](usr__lib__libAWDProtobufGCK.dylib.md) | 7019.0.0.0.0 | light |
| [`/usr/lib/libAWDProtobufLocation.dylib`](usr__lib__libAWDProtobufLocation.dylib.md) | 7019.0.0.0.0 | light |
| [`/usr/lib/libAWDSupport.dylib`](usr__lib__libAWDSupport.dylib.md) | 998.0.0.0.0 | light |
| [`/usr/lib/libAWDSupportFramework.dylib`](usr__lib__libAWDSupportFramework.dylib.md) | 7019.0.0.0.0 | light |
| [`/usr/lib/libAXSafeCategoryBundle.dylib`](usr__lib__libAXSafeCategoryBundle.dylib.md) | 3245.8.9.0.0 | light |
| [`/usr/lib/libAXSpeechManager.dylib`](usr__lib__libAXSpeechManager.dylib.md) | 3245.8.9.0.0 | light |
| [`/usr/lib/libAmber.dylib`](usr__lib__libAmber.dylib.md) | 42.0.0.0.0 | light |
| [`/usr/lib/libAppPatch.dylib`](usr__lib__libAppPatch.dylib.md) | 1680.40.14.0.0 | light |
| [`/usr/lib/libAppleArchive.dylib`](usr__lib__libAppleArchive.dylib.md) | 469.40.4.0.0 | light |
| [`/usr/lib/libAppleEXR.dylib`](usr__lib__libAppleEXR.dylib.md) | 1011.0.0.0.0 | light |
| [`/usr/lib/libAppleSSE.dylib`](usr__lib__libAppleSSE.dylib.md) | 332.0.0.0.0 | light |
| [`/usr/lib/libAppleSSEExt.dylib`](usr__lib__libAppleSSEExt.dylib.md) | 332.0.0.0.0 | light |
| [`/usr/lib/libAudioDSPCore.dylib`](usr__lib__libAudioDSPCore.dylib.md) | 881.210.0.0.0 | light |
| [`/usr/lib/libAudioIssueDetector.dylib`](usr__lib__libAudioIssueDetector.dylib.md) | 881.210.0.0.0 | light |
| [`/usr/lib/libAudioStatistics.dylib`](usr__lib__libAudioStatistics.dylib.md) | 300.205.0.0.0 | light |
| [`/usr/lib/libBASupport.dylib`](usr__lib__libBASupport.dylib.md) | 279.52.2.0.0 | light |
| [`/usr/lib/libBBUpdaterDynamic_stubs.dylib`](usr__lib__libBBUpdaterDynamic_stubs.dylib.md) | 1594.0.0.0.0 | light |
| [`/usr/lib/libBKDM1.dylib`](usr__lib__libBKDM1.dylib.md) | 10321.40.10.0.0 | light |
| [`/usr/lib/libBasebandCommandDrivers.dylib`](usr__lib__libBasebandCommandDrivers.dylib.md) | 1594.0.0.0.0 | full |
| [`/usr/lib/libBasebandCommandDriversMIPC.dylib`](usr__lib__libBasebandCommandDriversMIPC.dylib.md) | 1594.0.0.0.0 | full |
| [`/usr/lib/libBasebandCommandDriversQMI.dylib`](usr__lib__libBasebandCommandDriversQMI.dylib.md) | 1594.0.0.0.0 | full |
| [`/usr/lib/libBasebandDiagnostics.dylib`](usr__lib__libBasebandDiagnostics.dylib.md) | 1594.0.0.0.0 | full |
| [`/usr/lib/libBasebandManager.dylib`](usr__lib__libBasebandManager.dylib.md) | 1594.0.0.0.0 | full |
| [`/usr/lib/libBasebandManagerDAL.dylib`](usr__lib__libBasebandManagerDAL.dylib.md) | 1594.0.0.0.0 | full |
| [`/usr/lib/libBasebandServicesRestResources.dylib`](usr__lib__libBasebandServicesRestResources.dylib.md) | 1594.0.0.0.0 | full |
| [`/usr/lib/libBasebandSharedServices.dylib`](usr__lib__libBasebandSharedServices.dylib.md) | 1594.0.0.0.0 | full |
| [`/usr/lib/libCRFSuite.dylib`](usr__lib__libCRFSuite.dylib.md) | 55.0.0.0.0 | light |
| [`/usr/lib/libCTGreenTeaLogger.dylib`](usr__lib__libCTGreenTeaLogger.dylib.md) | 13499.0.0.0.0 | light |
| [`/usr/lib/libChineseTokenizer.dylib`](usr__lib__libChineseTokenizer.dylib.md) | 44.0.0.0.0 | light |
| [`/usr/lib/libCoreEntitlements.dylib`](usr__lib__libCoreEntitlements.dylib.md) | 94.0.0.0.0 | light |
| [`/usr/lib/libCoreEntitlements_V2.dylib`](usr__lib__libCoreEntitlements_V2.dylib.md) | 94.0.0.0.0 | light |
| [`/usr/lib/libDHCPServer.A.dylib`](usr__lib__libDHCPServer.A.dylib.md) | 557.0.0.0.0 | light |
| [`/usr/lib/libDetachedCertificates.dylib`](usr__lib__libDetachedCertificates.dylib.md) | 1171.40.9.0.0 | light |
| [`/usr/lib/libDetachedCertificatesLookup.dylib`](usr__lib__libDetachedCertificatesLookup.dylib.md) | 1171.40.9.0.0 | light |
| [`/usr/lib/libETLDIAGLoggingDynamic.dylib`](usr__lib__libETLDIAGLoggingDynamic.dylib.md) | 1594.0.0.0.0 | light |
| [`/usr/lib/libETLDLFDynamic.dylib`](usr__lib__libETLDLFDynamic.dylib.md) | 1594.0.0.0.0 | light |
| [`/usr/lib/libETLDLOADCoreDumpDynamic.dylib`](usr__lib__libETLDLOADCoreDumpDynamic.dylib.md) | 1594.0.0.0.0 | light |
| [`/usr/lib/libETLDLOADDynamic.dylib`](usr__lib__libETLDLOADDynamic.dylib.md) | 1594.0.0.0.0 | light |
| [`/usr/lib/libETLDMCDynamic.dylib`](usr__lib__libETLDMCDynamic.dylib.md) | 1594.0.0.0.0 | light |
| [`/usr/lib/libETLDynamic.dylib`](usr__lib__libETLDynamic.dylib.md) | 1594.0.0.0.0 | light |
| [`/usr/lib/libETLEFSDumpDynamic.dylib`](usr__lib__libETLEFSDumpDynamic.dylib.md) | 1594.0.0.0.0 | light |
| [`/usr/lib/libETLSAHDynamic.dylib`](usr__lib__libETLSAHDynamic.dylib.md) | 1594.0.0.0.0 | light |
| [`/usr/lib/libEndpointSecurity.dylib`](usr__lib__libEndpointSecurity.dylib.md) | 657.40.27.0.0 | light |
| [`/usr/lib/libFDRDecode.dylib`](usr__lib__libFDRDecode.dylib.md) | 1636.40.11.0.0 | light |
| [`/usr/lib/libFosl_dynamic.dylib`](usr__lib__libFosl_dynamic.dylib.md) | 302.0.0.0.0 | light |
| [`/usr/lib/libHDLCDynamic.dylib`](usr__lib__libHDLCDynamic.dylib.md) | 1594.0.0.0.0 | light |
| [`/usr/lib/libHSFilerDynamic.dylib`](usr__lib__libHSFilerDynamic.dylib.md) | 1594.0.0.0.0 | light |
| [`/usr/lib/libICEClient.dylib`](usr__lib__libICEClient.dylib.md) | 1640.0.0.0.0 | light |
| [`/usr/lib/libIOABP.dylib`](usr__lib__libIOABP.dylib.md) | 960.0.0.0.0 | light |
| [`/usr/lib/libIOACIPC.dylib`](usr__lib__libIOACIPC.dylib.md) | 313.0.0.0.0 | light |
| [`/usr/lib/libIOACIPCBB.dylib`](usr__lib__libIOACIPCBB.dylib.md) | 430.0.0.0.0 | light |
| [`/usr/lib/libIOAccessoryManager.dylib`](usr__lib__libIOAccessoryManager.dylib.md) | 1068.40.6.0.0 | full |
| [`/usr/lib/libIOReport.dylib`](usr__lib__libIOReport.dylib.md) | 116.0.0.0.0 | light |
| [`/usr/lib/libImage4_V2.dylib`](usr__lib__libImage4_V2.dylib.md) | 27.0.3.0.0 | light |
| [`/usr/lib/libInFieldCollection.dylib`](usr__lib__libInFieldCollection.dylib.md) | 0.0.0.0.0 | light |
| [`/usr/lib/libMIPCSdk.dylib`](usr__lib__libMIPCSdk.dylib.md) | 177.0.0.0.0 | light |
| [`/usr/lib/libMatch.1.dylib`](usr__lib__libMatch.1.dylib.md) | 50.40.2.0.0 | light |
| [`/usr/lib/libMemoryResourceException.dylib`](usr__lib__libMemoryResourceException.dylib.md) | 369.40.1.0.0 | light |
| [`/usr/lib/libMobileCheckpoint.dylib`](usr__lib__libMobileCheckpoint.dylib.md) | 40.0.0.0.0 | light |
| [`/usr/lib/libNFC_Comet.dylib`](usr__lib__libNFC_Comet.dylib.md) | 371.8.0.0.0 | full |
| [`/usr/lib/libNFC_HAL.dylib`](usr__lib__libNFC_HAL.dylib.md) | 371.8.0.0.0 | full |
| [`/usr/lib/libPCITransport.dylib`](usr__lib__libPCITransport.dylib.md) | 1160.0.0.0.0 | light |
| [`/usr/lib/libPN548_API.dylib`](usr__lib__libPN548_API.dylib.md) | 371.8.0.0.0 | light |
| [`/usr/lib/libPPM.dylib`](usr__lib__libPPM.dylib.md) | 1191.40.27.0.1 | light |
| [`/usr/lib/libPPMDataModel.dylib`](usr__lib__libPPMDataModel.dylib.md) | 1191.40.27.0.1 | light |
| [`/usr/lib/libParallelCompression.dylib`](usr__lib__libParallelCompression.dylib.md) | 469.40.4.0.0 | light |
| [`/usr/lib/libQMIParserDynamic.dylib`](usr__lib__libQMIParserDynamic.dylib.md) | 1594.0.0.0.0 | light |
| [`/usr/lib/libRemoteTelephonyTransport.dylib`](usr__lib__libRemoteTelephonyTransport.dylib.md) | 6575.0.0.0.0 | full |
| [`/usr/lib/libReverseProxyDevice.dylib`](usr__lib__libReverseProxyDevice.dylib.md) | 114.40.2.0.0 | full |
| [`/usr/lib/libRoseBooter.dylib`](usr__lib__libRoseBooter.dylib.md) | 133.0.0.0.0 | full |
| [`/usr/lib/libRosetta.dylib`](usr__lib__libRosetta.dylib.md) | 385.0.0.0.0 | full |
| [`/usr/lib/libSCLM.dylib`](usr__lib__libSCLM.dylib.md) | 58.1.4.0.0 | light |
| [`/usr/lib/libSLAMDynamic.dylib`](usr__lib__libSLAMDynamic.dylib.md) | 58.1.4.0.0 | light |
| [`/usr/lib/libSMC.dylib`](usr__lib__libSMC.dylib.md) | 40.0.0.0.0 | light |
| [`/usr/lib/libSecureMAHelper.dylib`](usr__lib__libSecureMAHelper.dylib.md) | 2215.52.1.0.0 | light |
| [`/usr/lib/libSoftwareUpdateSSO.dylib`](usr__lib__libSoftwareUpdateSSO.dylib.md) | 2215.52.1.0.0 | light |
| [`/usr/lib/libSpatial.dylib`](usr__lib__libSpatial.dylib.md) | 113.0.0.0.0 | light |
| [`/usr/lib/libSystem.B.dylib`](usr__lib__libSystem.B.dylib.md) | 1359.40.3.0.0 | light |
| [`/usr/lib/libSystemHealth.dylib`](usr__lib__libSystemHealth.dylib.md) | 1307.52.1.0.0 | light |
| [`/usr/lib/libTLE.dylib`](usr__lib__libTLE.dylib.md) | 94.0.0.0.0 | light |
| [`/usr/lib/libTelephonyBasebandDynamic.dylib`](usr__lib__libTelephonyBasebandDynamic.dylib.md) | 6575.0.0.0.0 | full |
| [`/usr/lib/libTelephonyDebugDynamic.dylib`](usr__lib__libTelephonyDebugDynamic.dylib.md) | 6575.0.0.0.0 | full |
| [`/usr/lib/libTelephonyIOKitDynamic.dylib`](usr__lib__libTelephonyIOKitDynamic.dylib.md) | 6575.0.0.0.0 | full |
| [`/usr/lib/libTelephonyUSBDynamic.dylib`](usr__lib__libTelephonyUSBDynamic.dylib.md) | 6575.0.0.0.0 | full |
| [`/usr/lib/libThaiTokenizer.dylib`](usr__lib__libThaiTokenizer.dylib.md) | 28.0.0.0.0 | light |
| [`/usr/lib/libVinylNonUpdater.dylib`](usr__lib__libVinylNonUpdater.dylib.md) | 178.0.0.0.0 | light |
| [`/usr/lib/libWAPI.dylib`](usr__lib__libWAPI.dylib.md) | 440.1.0.0.0 | light |
| [`/usr/lib/libWISSupport.dylib`](usr__lib__libWISSupport.dylib.md) | 370.0.0.0.0 | light |
| [`/usr/lib/libWirelessAudioIPC.dylib`](usr__lib__libWirelessAudioIPC.dylib.md) | 1160.0.0.0.0 | light |
| [`/usr/lib/libacmobileshim.dylib`](usr__lib__libacmobileshim.dylib.md) | 30.0.0.0.0 | light |
| [`/usr/lib/libafc.dylib`](usr__lib__libafc.dylib.md) | 293.0.0.0.0 | light |
| [`/usr/lib/libamsupport.dylib`](usr__lib__libamsupport.dylib.md) | 475.40.7.0.0 | light |
| [`/usr/lib/libapple_nghttp2.dylib`](usr__lib__libapple_nghttp2.dylib.md) | 43.0.0.0.0 | light |
| [`/usr/lib/libarchive.2.dylib`](usr__lib__libarchive.2.dylib.md) | 182.40.6.0.0 | light |
| [`/usr/lib/libate.dylib`](usr__lib__libate.dylib.md) | 3.0.11.0.0 | light |
| [`/usr/lib/libauthinstall.dylib`](usr__lib__libauthinstall.dylib.md) | 1155.40.8.0.0 | light |
| [`/usr/lib/libaxis.dylib`](usr__lib__libaxis.dylib.md) | 8.1.15.0.0 | light |
| [`/usr/lib/libbsm.0.dylib`](usr__lib__libbsm.0.dylib.md) | 91.40.2.0.0 | light |
| [`/usr/lib/libbz2.1.0.dylib`](usr__lib__libbz2.1.0.dylib.md) | 49.0.0.0.0 | light |
| [`/usr/lib/libc++abi.dylib`](usr__lib__libc++abi.dylib.md) | 2200.32.0.0.0 | light |
| [`/usr/lib/libchannel.dylib`](usr__lib__libchannel.dylib.md) | 59.0.1.0.0 | light |
| [`/usr/lib/libcharset.1.dylib`](usr__lib__libcharset.1.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/libcmark-gfm.dylib`](usr__lib__libcmark-gfm.dylib.md) | 1.29.0.19.0 | light |
| [`/usr/lib/libcmph.dylib`](usr__lib__libcmph.dylib.md) | 9.0.0.0.0 | light |
| [`/usr/lib/libcompression.dylib`](usr__lib__libcompression.dylib.md) | 212.40.2.0.0 | light |
| [`/usr/lib/libcoretls.dylib`](usr__lib__libcoretls.dylib.md) | 189.40.2.0.0 | light |
| [`/usr/lib/libcoretls_cfhelpers.dylib`](usr__lib__libcoretls_cfhelpers.dylib.md) | 189.40.2.0.0 | light |
| [`/usr/lib/libcryptex.dylib`](usr__lib__libcryptex.dylib.md) | 761.40.23.0.0 | light |
| [`/usr/lib/libcryptex_core.dylib`](usr__lib__libcryptex_core.dylib.md) | 761.40.23.0.0 | light |
| [`/usr/lib/libcryptex_interface.dylib`](usr__lib__libcryptex_interface.dylib.md) | 761.40.23.0.0 | light |
| [`/usr/lib/libcryptex_trampoline.dylib`](usr__lib__libcryptex_trampoline.dylib.md) | 761.40.23.0.0 | light |
| [`/usr/lib/libcupolicy.dylib`](usr__lib__libcupolicy.dylib.md) | 13499.0.0.0.0 | light |
| [`/usr/lib/libdns_services.dylib`](usr__lib__libdns_services.dylib.md) | 3111.40.45.0.0 | light |
| [`/usr/lib/libdscsym.dylib`](usr__lib__libdscsym.dylib.md) | 441.0.0.0.0 | light |
| [`/usr/lib/libedit.3.dylib`](usr__lib__libedit.3.dylib.md) | 65.0.0.0.0 | light |
| [`/usr/lib/libenergytrace.dylib`](usr__lib__libenergytrace.dylib.md) | 23.0.0.0.0 | light |
| [`/usr/lib/libexpat.1.dylib`](usr__lib__libexpat.1.dylib.md) | 49.0.0.0.0 | light |
| [`/usr/lib/libexslt.0.dylib`](usr__lib__libexslt.0.dylib.md) | 22.0.0.0.0 | light |
| [`/usr/lib/libffi.dylib`](usr__lib__libffi.dylib.md) | 40.0.0.0.0 | light |
| [`/usr/lib/libfire7.dylib`](usr__lib__libfire7.dylib.md) | 135.0.5.0.0 | light |
| [`/usr/lib/libfire9.dylib`](usr__lib__libfire9.dylib.md) | 34.0.4.0.0 | light |
| [`/usr/lib/libform.5.4.dylib`](usr__lib__libform.5.4.dylib.md) | 85.0.0.0.0 | light |
| [`/usr/lib/libgermantok.dylib`](usr__lib__libgermantok.dylib.md) | 31.0.0.0.0 | light |
| [`/usr/lib/libheimdal-asn1.dylib`](usr__lib__libheimdal-asn1.dylib.md) | 725.40.6.0.0 | light |
| [`/usr/lib/libheimdalasn1.dylib`](usr__lib__libheimdalasn1.dylib.md) | 30.40.2.0.0 | light |
| [`/usr/lib/libhvf.dylib`](usr__lib__libhvf.dylib.md) | 14.0.0.0.0 | light |
| [`/usr/lib/libhwtrace.dylib`](usr__lib__libhwtrace.dylib.md) | 328.40.36.0.0 | light |
| [`/usr/lib/libiconv.2.dylib`](usr__lib__libiconv.2.dylib.md) | 123.0.0.0.0 | light |
| [`/usr/lib/libimage4.dylib`](usr__lib__libimage4.dylib.md) | 374.0.0.0.0 | light |
| [`/usr/lib/libindus.dylib`](usr__lib__libindus.dylib.md) | 221.0.0.0.0 | light |
| [`/usr/lib/libipsec.A.dylib`](usr__lib__libipsec.A.dylib.md) | 1130.0.0.0.0 | light |
| [`/usr/lib/libktrace.dylib`](usr__lib__libktrace.dylib.md) | 706.40.6.0.0 | light |
| [`/usr/lib/liblangid.dylib`](usr__lib__liblangid.dylib.md) | 140.0.0.0.0 | light |
| [`/usr/lib/liblockdown.dylib`](usr__lib__liblockdown.dylib.md) | 1378.40.3.0.0 | light |
| [`/usr/lib/liblzma.5.dylib`](usr__lib__liblzma.5.dylib.md) | 21.0.0.0.0 | light |
| [`/usr/lib/libmarisa.dylib`](usr__lib__libmarisa.dylib.md) | 28.0.0.0.0 | light |
| [`/usr/lib/libmav_ipc_router_dynamic.dylib`](usr__lib__libmav_ipc_router_dynamic.dylib.md) | 1594.0.0.0.0 | light |
| [`/usr/lib/libmd.dylib`](usr__lib__libmd.dylib.md) | 7.0.0.0.0 | light |
| [`/usr/lib/libmdns.dylib`](usr__lib__libmdns.dylib.md) | 3111.40.45.0.0 | light |
| [`/usr/lib/libmecab.dylib`](usr__lib__libmecab.dylib.md) | 1160.1.5.0.0 | light |
| [`/usr/lib/libmecabra.dylib`](usr__lib__libmecabra.dylib.md) | 1160.1.5.0.0 | light |
| [`/usr/lib/libmorphun.dylib`](usr__lib__libmorphun.dylib.md) | 3600.36.1.0.0 | light |
| [`/usr/lib/libmrc.dylib`](usr__lib__libmrc.dylib.md) | 3111.40.45.0.0 | light |
| [`/usr/lib/libncurses.5.4.dylib`](usr__lib__libncurses.5.4.dylib.md) | 85.0.0.0.0 | light |
| [`/usr/lib/libnfrestore.dylib`](usr__lib__libnfrestore.dylib.md) | 371.8.0.0.0 | light |
| [`/usr/lib/libnfstorage.dylib`](usr__lib__libnfstorage.dylib.md) | 371.8.0.0.0 | light |
| [`/usr/lib/liboah.dylib`](usr__lib__liboah.dylib.md) | 385.0.0.0.0 | light |
| [`/usr/lib/libolaf.dylib`](usr__lib__libolaf.dylib.md) | 193.0.0.0.0 | light |
| [`/usr/lib/libpartition2_dynamic.dylib`](usr__lib__libpartition2_dynamic.dylib.md) | 3696.40.14.0.1 | light |
| [`/usr/lib/libperfcheck.dylib`](usr__lib__libperfcheck.dylib.md) | 46.40.2.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend33.dylib`](usr__lib__objc__libobjcMsgSend33.dylib.md) | 973.1.0.0.0 | light |
| [`/usr/lib/libpcap.A.dylib`](usr__lib__libpcap.A.dylib.md) | 148.0.0.0.0 | light |
| [`/usr/lib/libpmenergy.dylib`](usr__lib__libpmenergy.dylib.md) | 307.0.0.0.0 | light |
| [`/usr/lib/libpmsample.dylib`](usr__lib__libpmsample.dylib.md) | 307.0.0.0.0 | light |
| [`/usr/lib/libprequelite.dylib`](usr__lib__libprequelite.dylib.md) | 162.0.0.0.0 | light |
| [`/usr/lib/libprotobuf.dylib`](usr__lib__libprotobuf.dylib.md) | 7019.0.0.0.0 | light |
| [`/usr/lib/librealtime_safety.dylib`](usr__lib__librealtime_safety.dylib.md) | 59.0.1.0.0 | light |
| [`/usr/lib/libresolv.9.dylib`](usr__lib__libresolv.9.dylib.md) | 99.0.0.0.0 | light |
| [`/usr/lib/libsandbox.1.dylib`](usr__lib__libsandbox.1.dylib.md) | 3051.40.81.0.0 | light |
| [`/usr/lib/libsbuf.dylib`](usr__lib__libsbuf.dylib.md) | 3.0.0.0.0 | light |
| [`/usr/lib/libskit.dylib`](usr__lib__libskit.dylib.md) | 3600.15.2.0.0 | light |
| [`/usr/lib/libsp.dylib`](usr__lib__libsp.dylib.md) | 66.0.0.0.0 | light |
| [`/usr/lib/libspindump.dylib`](usr__lib__libspindump.dylib.md) | 453.1.0.0.0 | light |
| [`/usr/lib/libswiftPrespecialized.dylib`](usr__lib__libswiftPrespecialized.dylib.md) | 0.0.0.0.0 | light |
| [`/usr/lib/libsysdiagnose.dylib`](usr__lib__libsysdiagnose.dylib.md) | 1598.40.4.0.0 | light |
| [`/usr/lib/libsysmon.dylib`](usr__lib__libsysmon.dylib.md) | 135.0.0.0.0 | light |
| [`/usr/lib/libsystemstats.dylib`](usr__lib__libsystemstats.dylib.md) | 515.40.3.0.0 | light |
| [`/usr/lib/libtailspin.dylib`](usr__lib__libtailspin.dylib.md) | 268.0.0.0.0 | light |
| [`/usr/lib/libtailspin_internal.dylib`](usr__lib__libtailspin_internal.dylib.md) | 268.0.0.0.0 | light |
| [`/usr/lib/libtidy.A.dylib`](usr__lib__libtidy.A.dylib.md) | 21.0.0.0.0 | light |
| [`/usr/lib/libtzupdate.dylib`](usr__lib__libtzupdate.dylib.md) | 90.0.0.0.0 | light |
| [`/usr/lib/libutil.dylib`](usr__lib__libutil.dylib.md) | 78.0.0.0.0 | light |
| [`/usr/lib/libxo.dylib`](usr__lib__libxo.dylib.md) | 4.0.0.0.0 | light |
| [`/usr/lib/libxpc_datastores.dylib`](usr__lib__libxpc_datastores.dylib.md) | 3298.52.1.0.0 | light |
| [`/usr/lib/libxslt.1.dylib`](usr__lib__libxslt.1.dylib.md) | 22.0.0.0.0 | light |
| [`/usr/lib/libz.1.dylib`](usr__lib__libz.1.dylib.md) | 105.0.0.0.0 | light |
| [`/usr/lib/log/liblog_IOHIDFamily.dylib`](usr__lib__log__liblog_IOHIDFamily.dylib.md) | 2360.40.13.0.1 | full |
| [`/usr/lib/log/liblog_SystemConfiguration.dylib`](usr__lib__log__liblog_SystemConfiguration.dylib.md) | 1453.40.1.0.0 | light |
| [`/usr/lib/log/liblog_coreacc.dylib`](usr__lib__log__liblog_coreacc.dylib.md) | 1219.52.1.0.0 | light |
| [`/usr/lib/log/liblog_geo.dylib`](usr__lib__log__liblog_geo.dylib.md) | 2076.31.9.18.106 | light |
| [`/usr/lib/log/liblog_location.dylib`](usr__lib__log__liblog_location.dylib.md) | 3187.0.1.0.0 | light |
| [`/usr/lib/log/liblog_mdns.dylib`](usr__lib__log__liblog_mdns.dylib.md) | 3111.40.45.0.0 | light |
| [`/usr/lib/log/liblog_mdnsresponder.dylib`](usr__lib__log__liblog_mdnsresponder.dylib.md) | 3111.40.45.0.0 | light |
| [`/usr/lib/log/liblog_network.dylib`](usr__lib__log__liblog_network.dylib.md) | 6681.52.6.0.0 | light |
| [`/usr/lib/log/liblog_signpost.description.dylib`](usr__lib__log__liblog_signpost.description.dylib.md) | 205.0.0.0.0 | light |
| [`/usr/lib/log/liblog_signpost.dylib`](usr__lib__log__liblog_signpost.dylib.md) | 205.0.0.0.0 | light |
| [`/usr/lib/log/liblog_signpost.telemetry.dylib`](usr__lib__log__liblog_signpost.telemetry.dylib.md) | 205.0.0.0.0 | light |
| [`/usr/lib/log/liblog_sonic.dylib`](usr__lib__log__liblog_sonic.dylib.md) | 26210.26.40.301.0 | light |
| [`/usr/lib/log/liblog_srp.dylib`](usr__lib__log__liblog_srp.dylib.md) | 3111.40.45.0.0 | light |
| [`/usr/lib/swift/libswiftARKit.dylib`](usr__lib__swift__libswiftARKit.dylib.md) | 781.40.6.0.0 | light |
| [`/usr/lib/swift/libswiftAppleArchive.dylib`](usr__lib__swift__libswiftAppleArchive.dylib.md) | 469.40.4.0.0 | light |
| [`/usr/lib/swift/libswiftCallKit.dylib`](usr__lib__swift__libswiftCallKit.dylib.md) | 5.0.0.0.0 | light |
| [`/usr/lib/swift/libswiftCarPlay.dylib`](usr__lib__swift__libswiftCarPlay.dylib.md) | 552.7.1.0.0 | light |
| [`/usr/lib/swift/libswiftCompression.dylib`](usr__lib__swift__libswiftCompression.dylib.md) | 18.0.0.0.0 | light |
| [`/usr/lib/swift/libswiftContacts.dylib`](usr__lib__swift__libswiftContacts.dylib.md) | 3.0.0.0.0 | light |
| [`/usr/lib/swift/libswiftCoreAudio.dylib`](usr__lib__swift__libswiftCoreAudio.dylib.md) | 482.208.0.0.0 | full |
| [`/usr/lib/swift/libswiftCoreAudio_Private.dylib`](usr__lib__swift__libswiftCoreAudio_Private.dylib.md) | 482.208.0.0.0 | full |
| [`/usr/lib/swift/libswiftCoreData.dylib`](usr__lib__swift__libswiftCoreData.dylib.md) | 25.0.0.0.0 | light |
| [`/usr/lib/swift/libswiftCoreGraphics.dylib`](usr__lib__swift__libswiftCoreGraphics.dylib.md) | 17.0.0.0.0 | light |
| [`/usr/lib/swift/libswiftCoreImage.dylib`](usr__lib__swift__libswiftCoreImage.dylib.md) | 3.0.0.0.0 | light |
| [`/usr/lib/swift/libswiftCoreMIDI.dylib`](usr__lib__swift__libswiftCoreMIDI.dylib.md) | 6.0.0.0.0 | light |
| [`/usr/lib/swift/libswiftCoreML.dylib`](usr__lib__swift__libswiftCoreML.dylib.md) | 3600.25.2.0.0 | full |
| [`/usr/lib/swift/libswiftCoreMedia.dylib`](usr__lib__swift__libswiftCoreMedia.dylib.md) | 3385.14.1.3.0 | light |
| [`/usr/lib/swift/libswiftCoreNFC.dylib`](usr__lib__swift__libswiftCoreNFC.dylib.md) | 3.4.0.0.0 | full |
| [`/usr/lib/swift/libswiftCryptoTokenKit.dylib`](usr__lib__swift__libswiftCryptoTokenKit.dylib.md) | 878.40.5.0.0 | light |
| [`/usr/lib/swift/libswiftDarwin.dylib`](usr__lib__swift__libswiftDarwin.dylib.md) | 428.40.1.0.0 | light |
| [`/usr/lib/swift/libswiftDataDetection.dylib`](usr__lib__swift__libswiftDataDetection.dylib.md) | 852.0.0.0.0 | light |
| [`/usr/lib/swift/libswiftDemangle.dylib`](usr__lib__swift__libswiftDemangle.dylib.md) | 6.4.2.1.9 | light |
| [`/usr/lib/swift/libswiftExtensionFoundation.dylib`](usr__lib__swift__libswiftExtensionFoundation.dylib.md) | 290.1.3.0.0 | light |
| [`/usr/lib/swift/libswiftExtensionKit.dylib`](usr__lib__swift__libswiftExtensionKit.dylib.md) | 290.1.3.0.0 | light |
| [`/usr/lib/swift/libswiftFileProvider.dylib`](usr__lib__swift__libswiftFileProvider.dylib.md) | 4838.42.2.0.0 | light |
| [`/usr/lib/swift/libswiftFoundation.dylib`](usr__lib__swift__libswiftFoundation.dylib.md) | 2000.0.0.0.0 | light |
| [`/usr/lib/swift/libswiftGLKit.dylib`](usr__lib__swift__libswiftGLKit.dylib.md) | 1.2.0.0.0 | light |
| [`/usr/lib/swift/libswiftGameplayKit.dylib`](usr__lib__swift__libswiftGameplayKit.dylib.md) | 2.0.0.0.0 | light |
| [`/usr/lib/swift/libswiftHealthKit.dylib`](usr__lib__swift__libswiftHealthKit.dylib.md) | 7027.1.56.6.5 | light |
| [`/usr/lib/swift/libswiftIntents.dylib`](usr__lib__swift__libswiftIntents.dylib.md) | 12.0.0.0.0 | light |
| [`/usr/lib/swift/libswiftMLCompute.dylib`](usr__lib__swift__libswiftMLCompute.dylib.md) | 87.0.0.0.0 | light |
| [`/usr/lib/swift/libswiftMapKit.dylib`](usr__lib__swift__libswiftMapKit.dylib.md) | 27.31.9.22.1 | light |
| [`/usr/lib/swift/libswiftMediaPlayer.dylib`](usr__lib__swift__libswiftMediaPlayer.dylib.md) | 4026.210.1.0.0 | light |
| [`/usr/lib/swift/libswiftMetal.dylib`](usr__lib__swift__libswiftMetal.dylib.md) | 383.1.2.0.0 | full |
| [`/usr/lib/swift/libswiftMetalKit.dylib`](usr__lib__swift__libswiftMetalKit.dylib.md) | 1.3.0.0.0 | full |
| [`/usr/lib/swift/libswiftModelIO.dylib`](usr__lib__swift__libswiftModelIO.dylib.md) | 2.0.0.0.0 | light |
| [`/usr/lib/swift/libswiftNaturalLanguage.dylib`](usr__lib__swift__libswiftNaturalLanguage.dylib.md) | 4.3.0.0.0 | light |
| [`/usr/lib/swift/libswiftNearbyInteraction.dylib`](usr__lib__swift__libswiftNearbyInteraction.dylib.md) | 576.0.1.0.0 | full |
| [`/usr/lib/swift/libswiftOSLog.dylib`](usr__lib__swift__libswiftOSLog.dylib.md) | 10.0.0.0.0 | light |
| [`/usr/lib/swift/libswiftPassKit.dylib`](usr__lib__swift__libswiftPassKit.dylib.md) | 1696.2.9.2.0 | light |
| [`/usr/lib/swift/libswiftQuartzCore.dylib`](usr__lib__swift__libswiftQuartzCore.dylib.md) | 5.0.0.0.0 | full |
| [`/usr/lib/swift/libswiftSceneKit.dylib`](usr__lib__swift__libswiftSceneKit.dylib.md) | 1.2.0.0.0 | light |
| [`/usr/lib/swift/libswiftSpatial.dylib`](usr__lib__swift__libswiftSpatial.dylib.md) | 113.0.0.0.0 | light |
| [`/usr/lib/swift/libswiftSpeech.dylib`](usr__lib__swift__libswiftSpeech.dylib.md) | 4.0.0.0.0 | light |
| [`/usr/lib/swift/libswiftSpriteKit.dylib`](usr__lib__swift__libswiftSpriteKit.dylib.md) | 1.2.0.0.0 | light |
| [`/usr/lib/swift/libswiftSwiftOnoneSupport.dylib`](usr__lib__swift__libswiftSwiftOnoneSupport.dylib.md) | 6.4.2.1.9 | light |
| [`/usr/lib/swift/libswiftSystem_Foundation.dylib`](usr__lib__swift__libswiftSystem_Foundation.dylib.md) | 5027.1.8.0.0 | light |
| [`/usr/lib/swift/libswiftUIKit.dylib`](usr__lib__swift__libswiftUIKit.dylib.md) | 9127.1.13.13.0 | light |
| [`/usr/lib/swift/libswiftVideoToolbox.dylib`](usr__lib__swift__libswiftVideoToolbox.dylib.md) | 3385.14.1.3.0 | full |
| [`/usr/lib/swift/libswiftVision.dylib`](usr__lib__swift__libswiftVision.dylib.md) | 4.0.0.0.0 | light |
| [`/usr/lib/swift/libswiftWatchKit.dylib`](usr__lib__swift__libswiftWatchKit.dylib.md) | 8.0.0.0.0 | light |
| [`/usr/lib/swift/libswift_Builtin_float.dylib`](usr__lib__swift__libswift_Builtin_float.dylib.md) | 6.4.2.1.9 | light |
| [`/usr/lib/swift/libswift_DarwinFoundation1.dylib`](usr__lib__swift__libswift_DarwinFoundation1.dylib.md) | 428.40.1.0.0 | light |
| [`/usr/lib/swift/libswift_DarwinFoundation2.dylib`](usr__lib__swift__libswift_DarwinFoundation2.dylib.md) | 428.40.1.0.0 | light |
| [`/usr/lib/swift/libswift_DarwinFoundation3.dylib`](usr__lib__swift__libswift_DarwinFoundation3.dylib.md) | 428.40.1.0.0 | light |
| [`/usr/lib/swift/libswift_Volatile.dylib`](usr__lib__swift__libswift_Volatile.dylib.md) | 6.4.2.1.9 | light |
| [`/usr/lib/swift/libswift_errno.dylib`](usr__lib__swift__libswift_errno.dylib.md) | 428.40.1.0.0 | light |
| [`/usr/lib/swift/libswift_math.dylib`](usr__lib__swift__libswift_math.dylib.md) | 428.40.1.0.0 | light |
| [`/usr/lib/swift/libswift_signal.dylib`](usr__lib__swift__libswift_signal.dylib.md) | 428.40.1.0.0 | light |
| [`/usr/lib/swift/libswift_stdio.dylib`](usr__lib__swift__libswift_stdio.dylib.md) | 428.40.1.0.0 | light |
| [`/usr/lib/swift/libswift_time.dylib`](usr__lib__swift__libswift_time.dylib.md) | 428.40.1.0.0 | light |
| [`/usr/lib/swift/libswiftsimd.dylib`](usr__lib__swift__libswiftsimd.dylib.md) | 25.0.0.0.0 | light |
| [`/usr/lib/swift/libswiftsys_time.dylib`](usr__lib__swift__libswiftsys_time.dylib.md) | 428.40.1.0.0 | light |
| [`/usr/lib/swift/libswiftunistd.dylib`](usr__lib__swift__libswiftunistd.dylib.md) | 428.40.1.0.0 | light |
| [`/usr/lib/system/libcache.dylib`](usr__lib__system__libcache.dylib.md) | 95.0.0.0.0 | light |
| [`/usr/lib/system/libcommonCrypto.dylib`](usr__lib__system__libcommonCrypto.dylib.md) | 600041.40.3.0.0 | light |
| [`/usr/lib/system/libcompiler_rt.dylib`](usr__lib__system__libcompiler_rt.dylib.md) | 103.4.0.0.0 | light |
| [`/usr/lib/system/libcopyfile.dylib`](usr__lib__system__libcopyfile.dylib.md) | 260.40.4.0.0 | light |
| [`/usr/lib/system/libcorecrypto_noasm.dylib`](usr__lib__system__libcorecrypto_noasm.dylib.md) | 2109.40.22.0.0 | light |
| [`/usr/lib/system/libcorecrypto_trace.dylib`](usr__lib__system__libcorecrypto_trace.dylib.md) | 2109.40.22.0.0 | light |
| [`/usr/lib/system/liblaunch.dylib`](usr__lib__system__liblaunch.dylib.md) | 3298.52.1.0.0 | light |
| [`/usr/lib/system/libmacho.dylib`](usr__lib__system__libmacho.dylib.md) | 27104.0.0.0.0 | light |
| [`/usr/lib/system/libremovefile.dylib`](usr__lib__system__libremovefile.dylib.md) | 96.40.3.0.0 | light |
| [`/usr/lib/system/libsystem_blocks.dylib`](usr__lib__system__libsystem_blocks.dylib.md) | 98.0.0.0.0 | light |
| [`/usr/lib/system/libsystem_collections.dylib`](usr__lib__system__libsystem_collections.dylib.md) | 1786.40.6.0.0 | light |
| [`/usr/lib/system/libsystem_configuration.dylib`](usr__lib__system__libsystem_configuration.dylib.md) | 1453.40.1.0.0 | light |
| [`/usr/lib/system/libsystem_darwindirectory.dylib`](usr__lib__system__libsystem_darwindirectory.dylib.md) | 129.0.1.0.0 | light |
| [`/usr/lib/system/libsystem_eligibility.dylib`](usr__lib__system__libsystem_eligibility.dylib.md) | 446.52.1.0.0 | light |
| [`/usr/lib/system/libsystem_m.dylib`](usr__lib__system__libsystem_m.dylib.md) | 3326.40.2.0.0 | light |
| [`/usr/lib/system/libsystem_notify.dylib`](usr__lib__system__libsystem_notify.dylib.md) | 368.40.2.0.0 | light |
| [`/usr/lib/system/libsystem_sandbox.dylib`](usr__lib__system__libsystem_sandbox.dylib.md) | 3051.40.81.0.0 | light |
| [`/usr/lib/system/libsystem_sanitizers.dylib`](usr__lib__system__libsystem_sanitizers.dylib.md) | 32.0.0.0.0 | light |
| [`/usr/lib/system/libsystem_trial.dylib`](usr__lib__system__libsystem_trial.dylib.md) | 511.1.2.0.0 | light |
| [`/usr/lib/system/libunwind.dylib`](usr__lib__system__libunwind.dylib.md) | 2200.5.0.0.0 | light |
| [`/usr/lib/updaters/libAce3Updater.dylib`](usr__lib__updaters__libAce3Updater.dylib.md) | 1587.40.33.0.0 | light |
| [`/usr/lib/updaters/libAppleTCONTwoStageUpdater.dylib`](usr__lib__updaters__libAppleTCONTwoStageUpdater.dylib.md) | 230.40.6.0.0 | light |
| [`/usr/lib/updaters/libAppleTCONUpdater.dylib`](usr__lib__updaters__libAppleTCONUpdater.dylib.md) | 230.40.6.0.0 | light |
| [`/usr/lib/updaters/libAppleTconUARPUpdater.dylib`](usr__lib__updaters__libAppleTconUARPUpdater.dylib.md) | 1587.40.33.0.0 | light |
| [`/usr/lib/updaters/libCentauriUpdater.dylib`](usr__lib__updaters__libCentauriUpdater.dylib.md) | 80.0.0.0.0 | full |
| [`/usr/lib/updaters/libPS190Updater.dylib`](usr__lib__updaters__libPS190Updater.dylib.md) | 1587.40.33.0.0 | light |
| [`/usr/lib/updaters/libRoseUpdater.dylib`](usr__lib__updaters__libRoseUpdater.dylib.md) | 133.0.0.0.0 | full |
| [`/usr/lib/updaters/libSEUpdater.dylib`](usr__lib__updaters__libSEUpdater.dylib.md) | 58.1.4.0.0 | light |
| [`/usr/lib/updaters/libSavageRestoreInfo_iOS.dylib`](usr__lib__updaters__libSavageRestoreInfo_iOS.dylib.md) | 7.116.0.0.0 | light |
| [`/usr/lib/updaters/libSavageUpdater_iOS.dylib`](usr__lib__updaters__libSavageUpdater_iOS.dylib.md) | 7.116.0.0.0 | light |
| [`/usr/lib/updaters/libT200Updater.dylib`](usr__lib__updaters__libT200Updater.dylib.md) | 1.0.0.8.96 | light |
| [`/usr/lib/updaters/libVinylUpdater.dylib`](usr__lib__updaters__libVinylUpdater.dylib.md) | 178.0.0.0.0 | light |
| [`/usr/lib/usd/libusd_ms.dylib`](usr__lib__usd__libusd_ms.dylib.md) | 24.1.32.0.0 | light |
| [`/System/Library/AccessibilityBundles/AboutSettings.axbundle/AboutSettings`](System__Library__AccessibilityBundles__AboutSettings.axbundle__AboutSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AssistantIsland.axbundle/AssistantIsland`](System__Library__AccessibilityBundles__AssistantIsland.axbundle__AssistantIsland.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/AssistantIslandClient.axbundle/AssistantIslandClient`](System__Library__AccessibilityBundles__AssistantIslandClient.axbundle__AssistantIslandClient.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/CampoUIInternal.axbundle/CampoUIInternal`](System__Library__AccessibilityBundles__CampoUIInternal.axbundle__CampoUIInternal.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/ClockAngel.axbundle/ClockAngel`](System__Library__AccessibilityBundles__ClockAngel.axbundle__ClockAngel.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/FeedbackCore.axbundle/FeedbackCore`](System__Library__AccessibilityBundles__FeedbackCore.axbundle__FeedbackCore.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/FilterAsNewCallersSettingsBundle.axbundle/FilterAsNewCallersSettingsBundle`](System__Library__AccessibilityBundles__FilterAsNewCallersSettingsBundle.axbundle__FilterAsNewCallersSettingsBundle.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/GameOverlayUI.axbundle/GameOverlayUI`](System__Library__AccessibilityBundles__GameOverlayUI.axbundle__GameOverlayUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/HealthMenstrualCyclesUI.axbundle/HealthMenstrualCyclesUI`](System__Library__AccessibilityBundles__HealthMenstrualCyclesUI.axbundle__HealthMenstrualCyclesUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/HealthMobilityUI.axbundle/HealthMobilityUI`](System__Library__AccessibilityBundles__HealthMobilityUI.axbundle__HealthMobilityUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/PingMyWatchControlCenterUI.axbundle/PingMyWatchControlCenterUI`](System__Library__AccessibilityBundles__PingMyWatchControlCenterUI.axbundle__PingMyWatchControlCenterUI.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/SiriSetup.axbundle/SiriSetup`](System__Library__AccessibilityBundles__SiriSetup.axbundle__SiriSetup.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/TransferOrResetSettings.axbundle/TransferOrResetSettings`](System__Library__AccessibilityBundles__TransferOrResetSettings.axbundle__TransferOrResetSettings.md) | 3050.3.8.0.0 | light |
| [`/System/Library/AccessibilityBundles/WidgetRenderer.axbundle/WidgetRenderer`](System__Library__AccessibilityBundles__WidgetRenderer.axbundle__WidgetRenderer.md) | 3050.3.8.0.0 | light |
| [`/System/Library/Frameworks/_AppIntents_HealthKit.framework/_AppIntents_HealthKit`](System__Library__Frameworks___AppIntents_HealthKit.framework___AppIntents_HealthKit.md) | 301.1.16.0.0 | light |
| [`/System/Library/Frameworks/_DataDetection_SwiftUI.framework/_DataDetection_SwiftUI`](System__Library__Frameworks___DataDetection_SwiftUI.framework___DataDetection_SwiftUI.md) | 852.0.0.0.0 | light |
| [`/System/Library/Frameworks/_MediaPlayer_AppIntents.framework/_MediaPlayer_AppIntents`](System__Library__Frameworks___MediaPlayer_AppIntents.framework___MediaPlayer_AppIntents.md) | 4026.210.1.0.0 | light |
| [`/System/Library/Frameworks/_NearbyInteraction_SwiftUI.framework/_NearbyInteraction_SwiftUI`](System__Library__Frameworks___NearbyInteraction_SwiftUI.framework___NearbyInteraction_SwiftUI.md) | 576.0.1.0.0 | full |
| [`/System/Library/Frameworks/_NowPlaying_AppIntents.framework/_NowPlaying_AppIntents`](System__Library__Frameworks___NowPlaying_AppIntents.framework___NowPlaying_AppIntents.md) | 4026.210.4.0.0 | light |
| [`/System/Library/Frameworks/_ScreenCaptureKit_SwiftUI.framework/_ScreenCaptureKit_SwiftUI`](System__Library__Frameworks___ScreenCaptureKit_SwiftUI.framework___ScreenCaptureKit_SwiftUI.md) | 765.15.2.0.0 | light |
| [`/System/Library/Frameworks/LinkSecurity.framework/LinkSecurity`](System__Library__Frameworks__LinkSecurity.framework__LinkSecurity.md) | 1491.200.101.21.5 | full |
| [`/System/Library/Frameworks/SuggestedActions.framework/SuggestedActions`](System__Library__Frameworks__SuggestedActions.framework__SuggestedActions.md) | 22.0.0.0.0 | light |
| [`/System/Library/Frameworks/TrustInsights.framework/TrustInsights`](System__Library__Frameworks__TrustInsights.framework__TrustInsights.md) | 27.2.5.0.0 | light |
| [`/System/Library/Health/FeedItemPlugins/EvaluationsHealthAppPlugin.healthplugin/EvaluationsHealthAppPlugin`](System__Library__Health__FeedItemPlugins__EvaluationsHealthAppPlugin.healthplugin__EvaluationsHealthAppPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/FeedItemPlugins/HealthBalanceAppPluginBundle.healthplugin/HealthBalanceAppPluginBundle`](System__Library__Health__FeedItemPlugins__HealthBalanceAppPluginBundle.healthplugin__HealthBalanceAppPluginBundle.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/FeedItemPlugins/HealthContentAppPluginBundle.healthplugin/HealthContentAppPluginBundle`](System__Library__Health__FeedItemPlugins__HealthContentAppPluginBundle.healthplugin__HealthContentAppPluginBundle.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/FeedItemPlugins/HealthIntelligenceAppPlugin.healthplugin/HealthIntelligenceAppPlugin`](System__Library__Health__FeedItemPlugins__HealthIntelligenceAppPlugin.healthplugin__HealthIntelligenceAppPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/FeedItemPlugins/HealthPlansAppPluginBundle.healthplugin/HealthPlansAppPluginBundle`](System__Library__Health__FeedItemPlugins__HealthPlansAppPluginBundle.healthplugin__HealthPlansAppPluginBundle.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/FeedItemPlugins/HealthReportAppDaemonPlugin.healthplugin/HealthReportAppDaemonPlugin`](System__Library__Health__FeedItemPlugins__HealthReportAppDaemonPlugin.healthplugin__HealthReportAppDaemonPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/FeedItemPlugins/MedicationsHealthAppPluginBundle.healthplugin/MedicationsHealthAppPluginBundle`](System__Library__Health__FeedItemPlugins__MedicationsHealthAppPluginBundle.healthplugin__MedicationsHealthAppPluginBundle.md) | 7027.1.56.6.5 | light |
| [`/System/Library/Health/Plugins/RemoteHeartRateStreamDaemonPlugin.bundle/RemoteHeartRateStreamDaemonPlugin`](System__Library__Health__Plugins__RemoteHeartRateStreamDaemonPlugin.bundle__RemoteHeartRateStreamDaemonPlugin.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/_AppUserEvents_AppAnalytics.framework/_AppUserEvents_AppAnalytics`](System__Library__PrivateFrameworks___AppUserEvents_AppAnalytics.framework___AppUserEvents_AppAnalytics.md) | 12.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/_AppUserEvents_ComputationalGraph.framework/_AppUserEvents_ComputationalGraph`](System__Library__PrivateFrameworks___AppUserEvents_ComputationalGraph.framework___AppUserEvents_ComputationalGraph.md) | 12.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/_MarketplaceIntents_AppIntents.framework/_MarketplaceIntents_AppIntents`](System__Library__PrivateFrameworks___MarketplaceIntents_AppIntents.framework___MarketplaceIntents_AppIntents.md) | 3605.14.1.11.1 | light |
| [`/System/Library/PrivateFrameworks/AgentCanvasModel.framework/AgentCanvasModel`](System__Library__PrivateFrameworks__AgentCanvasModel.framework__AgentCanvasModel.md) | 3605.10.2.11.9 | light |
| [`/System/Library/PrivateFrameworks/AnalyticsAgentFramework.framework/AnalyticsAgentFramework`](System__Library__PrivateFrameworks__AnalyticsAgentFramework.framework__AnalyticsAgentFramework.md) | 577.40.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/AONSenseService.framework/AONSenseService`](System__Library__PrivateFrameworks__AONSenseService.framework__AONSenseService.md) | 131.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/AskToPeopleBridge.framework/AskToPeopleBridge`](System__Library__PrivateFrameworks__AskToPeopleBridge.framework__AskToPeopleBridge.md) | 97.125.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/ASRKit.framework/ASRKit`](System__Library__PrivateFrameworks__ASRKit.framework__ASRKit.md) | 2.40.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/AssetMetricsCoreV2.framework/AssetMetricsCoreV2`](System__Library__PrivateFrameworks__AssetMetricsCoreV2.framework__AssetMetricsCoreV2.md) | 3605.15.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/AXFlashScreenUIServices.framework/AXFlashScreenUIServices`](System__Library__PrivateFrameworks__AXFlashScreenUIServices.framework__AXFlashScreenUIServices.md) | 3245.8.9.0.0 | full |
| [`/System/Library/PrivateFrameworks/BatteryDischarge.framework/BatteryDischarge`](System__Library__PrivateFrameworks__BatteryDischarge.framework__BatteryDischarge.md) | 19.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/BatteryKit.framework/BatteryKit`](System__Library__PrivateFrameworks__BatteryKit.framework__BatteryKit.md) | 3486.52.2.0.0 | full |
| [`/System/Library/PrivateFrameworks/CallIntelligenceRuntime.framework/CallIntelligenceRuntime`](System__Library__PrivateFrameworks__CallIntelligenceRuntime.framework__CallIntelligenceRuntime.md) | 158.200.81.21.9 | light |
| [`/System/Library/PrivateFrameworks/CarPlayAsset.framework/CarPlayAsset`](System__Library__PrivateFrameworks__CarPlayAsset.framework__CarPlayAsset.md) | 509.8.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CKSharingManagementDaemon.framework/CKSharingManagementDaemon`](System__Library__PrivateFrameworks__CKSharingManagementDaemon.framework__CKSharingManagementDaemon.md) | 27.125.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/CloudModuleArbitration.framework/CloudModuleArbitration`](System__Library__PrivateFrameworks__CloudModuleArbitration.framework__CloudModuleArbitration.md) | 4.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreAnalyticsSwiftBridge.framework/CoreAnalyticsSwiftBridge`](System__Library__PrivateFrameworks__CoreAnalyticsSwiftBridge.framework__CoreAnalyticsSwiftBridge.md) | 577.40.7.0.0 | light |
| [`/System/Library/PrivateFrameworks/CoreRoutineProtobuf.framework/CoreRoutineProtobuf`](System__Library__PrivateFrameworks__CoreRoutineProtobuf.framework__CoreRoutineProtobuf.md) | 1123.0.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/CRShipModeUI.framework/CRShipModeUI`](System__Library__PrivateFrameworks__CRShipModeUI.framework__CRShipModeUI.md) | 1307.52.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/CTMessagingSettings.framework/CTMessagingSettings`](System__Library__PrivateFrameworks__CTMessagingSettings.framework__CTMessagingSettings.md) | 13499.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/EligibilityQuorum.framework/EligibilityQuorum`](System__Library__PrivateFrameworks__EligibilityQuorum.framework__EligibilityQuorum.md) | 248.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ExclavesStats.framework/ExclavesStats`](System__Library__PrivateFrameworks__ExclavesStats.framework__ExclavesStats.md) | 10848.40.6.0.0 | full |
| [`/System/Library/PrivateFrameworks/FileBrowsingServices.framework/FileBrowsingServices`](System__Library__PrivateFrameworks__FileBrowsingServices.framework__FileBrowsingServices.md) | 1857.1.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/FitnessRegulatoryApproval.framework/FitnessRegulatoryApproval`](System__Library__PrivateFrameworks__FitnessRegulatoryApproval.framework__FitnessRegulatoryApproval.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/GPUToolsCaptureCoreAI.framework/GPUToolsCaptureCoreAI`](System__Library__PrivateFrameworks__GPUToolsCaptureCoreAI.framework__GPUToolsCaptureCoreAI.md) | 2027.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/HealthArchivableViews.framework/HealthArchivableViews`](System__Library__PrivateFrameworks__HealthArchivableViews.framework__HealthArchivableViews.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthIntelligenceDonation.framework/HealthIntelligenceDonation`](System__Library__PrivateFrameworks__HealthIntelligenceDonation.framework__HealthIntelligenceDonation.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthNarrator.framework/HealthNarrator`](System__Library__PrivateFrameworks__HealthNarrator.framework__HealthNarrator.md) | 38.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/HealthPlansDiagnosticExtensionCore.framework/HealthPlansDiagnosticExtensionCore`](System__Library__PrivateFrameworks__HealthPlansDiagnosticExtensionCore.framework__HealthPlansDiagnosticExtensionCore.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HealthRecordsAssembler.framework/HealthRecordsAssembler`](System__Library__PrivateFrameworks__HealthRecordsAssembler.framework__HealthRecordsAssembler.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/HearingRelevance.framework/HearingRelevance`](System__Library__PrivateFrameworks__HearingRelevance.framework__HearingRelevance.md) | 543.2.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/HybridDatabaseTokenizer.framework/HybridDatabaseTokenizer`](System__Library__PrivateFrameworks__HybridDatabaseTokenizer.framework__HybridDatabaseTokenizer.md) | 60.3.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/HybridSearch.framework/HybridSearch`](System__Library__PrivateFrameworks__HybridSearch.framework__HybridSearch.md) | 73.3.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/HybridSearchAdapter.framework/HybridSearchAdapter`](System__Library__PrivateFrameworks__HybridSearchAdapter.framework__HybridSearchAdapter.md) | 73.3.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/HybridSearchResultRanker.framework/HybridSearchResultRanker`](System__Library__PrivateFrameworks__HybridSearchResultRanker.framework__HybridSearchResultRanker.md) | 73.3.4.0.0 | light |
| [`/System/Library/PrivateFrameworks/IDSRegionStore.framework/IDSRegionStore`](System__Library__PrivateFrameworks__IDSRegionStore.framework__IDSRegionStore.md) | 2003.200.71.2.4 | light |
| [`/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/AppEditIn.framework/AppEditIn`](System__Library__PrivateFrameworks__iWorkImport.framework__Frameworks__AppEditIn.framework__AppEditIn.md) | 488.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSFeatureFlags.framework/TSFeatureFlags`](System__Library__PrivateFrameworks__iWorkImport.framework__Frameworks__TSFeatureFlags.framework__TSFeatureFlags.md) | 488.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSFundamentals.framework/TSFundamentals`](System__Library__PrivateFrameworks__iWorkImport.framework__Frameworks__TSFundamentals.framework__TSFundamentals.md) | 488.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSGeometry.framework/TSGeometry`](System__Library__PrivateFrameworks__iWorkImport.framework__Frameworks__TSGeometry.framework__TSGeometry.md) | 488.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/LocalFederatedSearch.framework/LocalFederatedSearch`](System__Library__PrivateFrameworks__LocalFederatedSearch.framework__LocalFederatedSearch.md) | 3605.32.1.11.5 | light |
| [`/System/Library/PrivateFrameworks/ManagedBackgroundAssetsRelay.framework/ManagedBackgroundAssetsRelay`](System__Library__PrivateFrameworks__ManagedBackgroundAssetsRelay.framework__ManagedBackgroundAssetsRelay.md) | 2.1.9.0.0 | light |
| [`/System/Library/PrivateFrameworks/MarketplaceIntents.framework/MarketplaceIntents`](System__Library__PrivateFrameworks__MarketplaceIntents.framework__MarketplaceIntents.md) | 3605.14.1.11.1 | light |
| [`/System/Library/PrivateFrameworks/MemoryUsage.framework/MemoryUsage`](System__Library__PrivateFrameworks__MemoryUsage.framework__MemoryUsage.md) | 7027.1.56.6.5 | light |
| [`/System/Library/PrivateFrameworks/MomentsAlgorithms.framework/MomentsAlgorithms`](System__Library__PrivateFrameworks__MomentsAlgorithms.framework__MomentsAlgorithms.md) | 502.0.8.0.0 | light |
| [`/System/Library/PrivateFrameworks/MusicKitIntelligence.framework/MusicKitIntelligence`](System__Library__PrivateFrameworks__MusicKitIntelligence.framework__MusicKitIntelligence.md) | 4026.210.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/NexusExtras.framework/NexusExtras`](System__Library__PrivateFrameworks__NexusExtras.framework__NexusExtras.md) | 910.31.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/PencilFeedback.framework/PencilFeedback`](System__Library__PrivateFrameworks__PencilFeedback.framework__PencilFeedback.md) | 12.0.0.0.0 | full |
| [`/System/Library/PrivateFrameworks/PolarisExclaveTestClientDarwin.framework/PolarisExclaveTestClientDarwin`](System__Library__PrivateFrameworks__PolarisExclaveTestClientDarwin.framework__PolarisExclaveTestClientDarwin.md) | 256.0.5.0.0 | full |
| [`/System/Library/PrivateFrameworks/PommesRanking.framework/PommesRanking`](System__Library__PrivateFrameworks__PommesRanking.framework__PommesRanking.md) | 6.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/PommesRankingCore.framework/PommesRankingCore`](System__Library__PrivateFrameworks__PommesRankingCore.framework__PommesRankingCore.md) | 6.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/PriMLCore.framework/PriMLCore`](System__Library__PrivateFrameworks__PriMLCore.framework__PriMLCore.md) | 47.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/PriMLDataPolicy.framework/PriMLDataPolicy`](System__Library__PrivateFrameworks__PriMLDataPolicy.framework__PriMLDataPolicy.md) | 47.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/ProcessorTrace.framework/ProcessorTrace`](System__Library__PrivateFrameworks__ProcessorTrace.framework__ProcessorTrace.md) | 328.40.36.0.0 | light |
| [`/System/Library/PrivateFrameworks/QLens.framework/QLens`](System__Library__PrivateFrameworks__QLens.framework__QLens.md) | 6.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/RelevanceServices.framework/RelevanceServices`](System__Library__PrivateFrameworks__RelevanceServices.framework__RelevanceServices.md) | 248.1.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/RoyaMediaOffloadService.framework/RoyaMediaOffloadService`](System__Library__PrivateFrameworks__RoyaMediaOffloadService.framework__RoyaMediaOffloadService.md) | 47.0.1.0.1 | light |
| [`/System/Library/PrivateFrameworks/RushmoreFramework.framework/RushmoreFramework`](System__Library__PrivateFrameworks__RushmoreFramework.framework__RushmoreFramework.md) | 149.2.4.0.2 | light |
| [`/System/Library/PrivateFrameworks/SafariFeatureSchemaManifest.framework/SafariFeatureSchemaManifest`](System__Library__PrivateFrameworks__SafariFeatureSchemaManifest.framework__SafariFeatureSchemaManifest.md) | 2.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/SafariFeatureUsageRetentionFramework.framework/SafariFeatureUsageRetentionFramework`](System__Library__PrivateFrameworks__SafariFeatureUsageRetentionFramework.framework__SafariFeatureUsageRetentionFramework.md) | 6.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/SafariSearchSchemaManifest.framework/SafariSearchSchemaManifest`](System__Library__PrivateFrameworks__SafariSearchSchemaManifest.framework__SafariSearchSchemaManifest.md) | 2.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/SafariUsageRetentionFramework.framework/SafariUsageRetentionFramework`](System__Library__PrivateFrameworks__SafariUsageRetentionFramework.framework__SafariUsageRetentionFramework.md) | 6.1.3.0.0 | light |
| [`/System/Library/PrivateFrameworks/SchemaTypesCore.framework/SchemaTypesCore`](System__Library__PrivateFrameworks__SchemaTypesCore.framework__SchemaTypesCore.md) | 3605.33.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/ServicesPlayback.framework/ServicesPlayback`](System__Library__PrivateFrameworks__ServicesPlayback.framework__ServicesPlayback.md) | 4.10.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/SettingsServices.framework/SettingsServices`](System__Library__PrivateFrameworks__SettingsServices.framework__SettingsServices.md) | 2027.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/SettingsServicesXPC.framework/SettingsServicesXPC`](System__Library__PrivateFrameworks__SettingsServicesXPC.framework__SettingsServicesXPC.md) | 2027.1.2.0.0 | light |
| [`/System/Library/PrivateFrameworks/SeymourAssetCore.framework/SeymourAssetCore`](System__Library__PrivateFrameworks__SeymourAssetCore.framework__SeymourAssetCore.md) | 2027.1.69.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiphonDriver.framework/SiphonDriver`](System__Library__PrivateFrameworks__SiphonDriver.framework__SiphonDriver.md) | 1.0.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriCloudSettings.framework/SiriCloudSettings`](System__Library__PrivateFrameworks__SiriCloudSettings.framework__SiriCloudSettings.md) | 3605.33.1.11.9 | light |
| [`/System/Library/PrivateFrameworks/SiriInferenceLearning.framework/SiriInferenceLearning`](System__Library__PrivateFrameworks__SiriInferenceLearning.framework__SiriInferenceLearning.md) | 3605.20.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriProcessing.framework/SiriProcessing`](System__Library__PrivateFrameworks__SiriProcessing.framework__SiriProcessing.md) | 3.3.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/SiriRaiseToSpeakExclave.framework/SiriRaiseToSpeakExclave`](System__Library__PrivateFrameworks__SiriRaiseToSpeakExclave.framework__SiriRaiseToSpeakExclave.md) | 3605.32.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/SiriRaiseToSpeakExclaveDebug.framework/SiriRaiseToSpeakExclaveDebug`](System__Library__PrivateFrameworks__SiriRaiseToSpeakExclaveDebug.framework__SiriRaiseToSpeakExclaveDebug.md) | 3605.32.1.0.0 | full |
| [`/System/Library/PrivateFrameworks/SoftwareUpdateServicesDaemonFramework.framework/SoftwareUpdateServicesDaemonFramework`](System__Library__PrivateFrameworks__SoftwareUpdateServicesDaemonFramework.framework__SoftwareUpdateServicesDaemonFramework.md) | 1114.40.10.0.0 | light |
| [`/System/Library/PrivateFrameworks/SpatialAudioServicesUI.framework/SpatialAudioServicesUI`](System__Library__PrivateFrameworks__SpatialAudioServicesUI.framework__SpatialAudioServicesUI.md) | 23.40.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/SPMirrorEntities.framework/SPMirrorEntities`](System__Library__PrivateFrameworks__SPMirrorEntities.framework__SPMirrorEntities.md) | 449.31.6.16.29 | light |
| [`/System/Library/PrivateFrameworks/SpotlightUIRanking.framework/SpotlightUIRanking`](System__Library__PrivateFrameworks__SpotlightUIRanking.framework__SpotlightUIRanking.md) | 6.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/TrustInsightsUI.framework/TrustInsightsUI`](System__Library__PrivateFrameworks__TrustInsightsUI.framework__TrustInsightsUI.md) | 27.2.5.0.0 | light |
| [`/System/Library/PrivateFrameworks/UnilogConfig.framework/XPCServices/UnilogConfigXPCService.xpc/Frameworks/UnilogConfigXPCLibrary.framework/UnilogConfigXPCLibrary`](System__Library__PrivateFrameworks__UnilogConfig.framework__XPCServices__UnilogConfigXPCService.xpc__Frameworks__UnilogConfigXPCLibrary.framework__UnilogConfigXPCLibrary.md) | 7.5.0.0.0 | light |
| [`/System/Library/PrivateFrameworks/UnilogSafariFeatureLibrary.framework/UnilogSafariFeatureLibrary`](System__Library__PrivateFrameworks__UnilogSafariFeatureLibrary.framework__UnilogSafariFeatureLibrary.md) | 2.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/UnilogSafariSearchLibrary.framework/UnilogSafariSearchLibrary`](System__Library__PrivateFrameworks__UnilogSafariSearchLibrary.framework__UnilogSafariSearchLibrary.md) | 2.1.1.0.0 | light |
| [`/System/Library/PrivateFrameworks/UnilogSafariUsageLibrary.framework/UnilogSafariUsageLibrary`](System__Library__PrivateFrameworks__UnilogSafariUsageLibrary.framework__UnilogSafariUsageLibrary.md) | 2.1.1.0.0 | light |
| [`/usr/lib/libfabric.dylib`](usr__lib__libfabric.dylib.md) | 21.0.0.0.0 | light |
| [`/usr/lib/libpcre2-8.0.dylib`](usr__lib__libpcre2-8.0.dylib.md) | 26.0.0.0.0 | light |
| [`/usr/lib/libpcre2-posix.3.dylib`](usr__lib__libpcre2-posix.3.dylib.md) | 26.0.0.0.0 | light |
| [`/usr/lib/updaters/libNVMeUpdater.dylib`](usr__lib__updaters__libNVMeUpdater.dylib.md) | 877.40.5.0.0 | light |
| [`/usr/lib/objc/libobjcMsgSend34.dylib`](usr__lib__objc__libobjcMsgSend34.dylib.md) | 973.1.0.0.0 | light |
