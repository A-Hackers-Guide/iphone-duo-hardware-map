# `/System/Library/ControlCenter/Bundles/DisplayModule.bundle/DisplayModule`

iOS 27.2 dyld shared cache image. Version `704.2.4.0.3`. **[DSC]**

## Linked libraries (10)

- `/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`
- `/System/Library/PrivateFrameworks/ControlCenterUIKit.framework/ControlCenterUIKit`
- `/usr/lib/libAccessibility.dylib`
- `/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`
- `/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/Frameworks/UIKit.framework/UIKit`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 3 classes, 6 protocols, 162 methods, 78 properties

### Class pages

Every class and protocol, with its methods: [`CBPropertyObserver`](../objc/CBPropertyObserver_DisplayModule.protocol.md), [`CCUIContentModule`](../objc/CCUIContentModule_DisplayModule.protocol.md), [`CCUIContentModuleContentViewController`](../objc/CCUIContentModuleContentViewController_DisplayModule.protocol.md), [`CCUIDisplayBackgroundViewController`](../objc/CCUIDisplayBackgroundViewController_DisplayModule.md), [`CCUIDisplayModule`](../objc/CCUIDisplayModule_DisplayModule.md), [`CCUIDisplayModuleViewController`](../objc/CCUIDisplayModuleViewController_DisplayModule.md), [`CCUIDisplayModuleViewControllerDelegate`](../objc/CCUIDisplayModuleViewControllerDelegate_DisplayModule.protocol.md), [`CCUIGroupRendering`](../objc/CCUIGroupRendering_DisplayModule.protocol.md), [`NSObject`](../objc/NSObject_DisplayModule.protocol.md)

### Classes

`CCUIDisplayBackgroundViewController`, `CCUIDisplayModule`, `CCUIDisplayModuleViewController`

### Protocols

`CBPropertyObserver`, `CCUIContentModule`, `CCUIContentModuleContentViewController`, `CCUIDisplayModuleViewControllerDelegate`, `CCUIGroupRendering`, `NSObject`

### Properties

```
@property (T@"NSSet",R) properties;
@property (T@"NSObject<OS_dispatch_queue>",R) notifyQueue;
@property (T@"UIViewController<CCUIContentModuleContentViewController>",?,R,N) contentViewController;
@property (T@"UIViewController<CCUIContentModuleBackgroundViewController>",?,R,N) backgroundViewController;
@property (TQ,?,R,N) supportedGridSizeClasses;
@property (T@"NSString",?,R,C,N) moduleDescription;
@property (TB,?,R,N) expandsGridSizeClassesForAccessibility;
@property (Td,R,N) preferredExpandedContentHeight;
@property (TB,?,N,GisResizing) resizing;
@property (Tq,?,N) gridSizeClass;
@property (TB,?,N) suppressesContentTransitions;
@property (Tq,?,N) userVisibilityStatus;
@property (Td,?,R,N) preferredExpandedContentWidth;
@property (TB,?,R,N) prefersExpandedContentSizeMatchesGridSize;
@property (Td,?,R,N) preferredExpandedContinuousCornerRadius;
@property (Td,?,N) compactContinuousCornerRadius;
@property (TQ,?,N) contentRenderingMode;
@property (T@"CCUIModuleContentMetrics",?,&,N) contentMetrics;
@property (TB,?,R,N) providesOwnPlatter;
@property (T@"NSArray",?,R,N) containerViewsForPlatterTreatment;
@property (T@"UIViewPropertyAnimator",?,R,N) customAnimator;
@property (TB,?,R,N) shouldPerformHoverInteraction;
@property (TB,?,R,N) shouldPerformClickInteraction;
@property (TB,?,R,N) wantsConfigurationIntent;
@property (TB,?,R,N) promptsForUserConfiguration;
@property (T@"INIntent",?,R,N) defaultConfigurationIntent;
@property (TQ,?,R,N) implicitlyExpandedGridSizeClasses;
@property (TB,R,N,GisGroupRenderingRequired) groupRenderingRequired;
@property (T@"NSArray",R,N) punchOutRenderingViews;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"CCUILabeledRoundButtonViewController",&,N,V_styleModeButton) styleModeButton;
@property (T@"CCUILabeledRoundButtonViewController",&,N,V_nightShiftButton) nightShiftButton;
@property (T@"CCUILabeledRoundButtonViewController",&,N,V_trueToneButton) trueToneButton;
@property (T@"CCUIContentModuleContext",&,N,V_contentModuleContext) contentModuleContext;
@property (T@"UIViewController<CCUIContentModuleContentViewController>",?,R,N) contentViewController;
@property (T@"UIViewController<CCUIContentModuleBackgroundViewController>",?,R,N) backgroundViewController;
@property (TQ,?,R,N) supportedGridSizeClasses;
@property (T@"NSString",?,R,C,N) moduleDescription;
@property (TB,?,R,N) expandsGridSizeClassesForAccessibility;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"CCUIContentModuleContext",&,N,V_contentModuleContext) contentModuleContext;
@property (T@"CCUIContinuousSliderView",&,N,V_sliderView) sliderView;
@property (T@"<CCUIDisplayModuleViewControllerDelegate>",W,N,V_delegate) delegate;
@property (Tf,R,N) currentBrightness;
@property (T@"NSSet",R) properties;
@property (T@"NSObject<OS_dispatch_queue>",R) notifyQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N,GisGroupRenderingRequired) groupRenderingRequired;
@property (T@"NSArray",R,N) punchOutRenderingViews;
@property (Td,R,N) preferredExpandedContentHeight;
@property (TB,?,N,GisResizing) resizing;
@property (Tq,?,N) gridSizeClass;
@property (TB,?,N) suppressesContentTransitions;
@property (Tq,?,N) userVisibilityStatus;
@property (Td,?,R,N) preferredExpandedContentWidth;
@property (TB,?,R,N) prefersExpandedContentSizeMatchesGridSize;
@property (Td,?,R,N) preferredExpandedContinuousCornerRadius;
@property (Td,?,N,V_compactContinuousCornerRadius) compactContinuousCornerRadius;
@property (TQ,?,N) contentRenderingMode;
@property (T@"CCUIModuleContentMetrics",?,&,N) contentMetrics;
@property (TB,?,R,N) providesOwnPlatter;
@property (T@"NSArray",?,R,N) containerViewsForPlatterTreatment;
@property (T@"UIViewPropertyAnimator",?,R,N) customAnimator;
@property (TB,?,R,N) shouldPerformHoverInteraction;
@property (TB,?,R,N) shouldPerformClickInteraction;
@property (TB,?,R,N) wantsConfigurationIntent;
@property (TB,?,R,N) promptsForUserConfiguration;
@property (T@"INIntent",?,R,N) defaultConfigurationIntent;
@property (TQ,?,R,N) implicitlyExpandedGridSizeClasses;
```

## Strings (48)

```
_MANUAL
CONTROL_CENTER_STATUS_STYLE_MODE
min
max
StyleMode
CONTROL_CENTER_STYLE_MODE_SETTING_NAME
CONTROL_CENTER_NIGHT_SHIFT_SETTING_NAME
k
_LIGHT
CBBrightnessControlAvailable
full
v16@?0^{?=BBBi{?={?=ii}{?=ii}}QB}8
light
CONTROL_CENTER_NIGHT_SHIFT_DISABLE_ACCESSIBILITY_SCREEN_FILTERS_MESSAGE
H
Brightness
mid
v24@?0Q8@\"NSNumber\"16
dark
_UNTIL_SUNSET
v16@?0@\"<UIViewControllerTransitionCoordinatorContext>\"8
NightShift
CONTROL_CENTER_TRUE_TONE_SETTING_NAME
v8@?0
CONTROL_CENTER_NIGHT_SHIFT_DISABLE_ACCESSIBILITY_SCREEN_FILTERS_CANCEL
CONTROL_CENTER_STATUS_NIGHT_SHIFT_OFF_UNTIL_SUNSET
ON
OFF
CONTROL_CENTER_STATUS_TRUE_TONE_ON
_DARK
CONTROL_CENTER_STATUS_TRUE_TONE_OFF
TrueTone
CONTROL_CENTER_NIGHT_SHIFT_DISABLE_ACCESSIBILITY_SCREEN_FILTERS_TITLE
v16@?0@\"UIAlertAction\"8
CONTROL_CENTER_STATUS_NIGHT_SHIFT_ON_MANUAL
CONTROL_CENTER_STATUS_NIGHT_SHIFT_%@_UNTIL_FORMAT
_UNTIL_SUNRISE
cc-brightness-slider
Q
v48@?0{?=BBBi{?={?=ii}{?=ii}}QB}8
CONTROL_CENTER_NIGHT_SHIFT_DISABLE_ACCESSIBILITY_SCREEN_FILTERS_ENABLE
CONTROL_CENTER_STATUS_NIGHT_SHIFT_ON_UNTIL_SUNRISE
CONTROL_CENTER_STATUS_NIGHT_SHIFT_OFF_MANUAL
_UNTIL_FORMAT
[Display Module] Failed to activate CBClient: %{public}@
[Display Module] Failed to create CBDisplayClient for displayID %lu: %{public}@
[Display Module] Failed to register CBPropertyObserver: %{public}@
[Display Module] Failed to copy brightness control available property: %{public}@
```
