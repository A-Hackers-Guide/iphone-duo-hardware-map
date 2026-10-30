# `CCUIContentModule` (protocol)

- Image: [`/System/Library/ControlCenter/Bundles/KeyboardBrightnessModule.bundle/KeyboardBrightnessModule`](../userland/System__Library__ControlCenter__Bundles__KeyboardBrightnessModule.bundle__KeyboardBrightnessModule.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 5 properties, 8 instance methods, 0 class methods

## Properties

```
@property (T@"UIViewController<CCUIContentModuleContentViewController>",?,R,N) contentViewController;
@property (T@"UIViewController<CCUIContentModuleBackgroundViewController>",?,R,N) backgroundViewController;
@property (TQ,?,R,N) supportedGridSizeClasses;
@property (T@"NSString",?,R,C,N) moduleDescription;
@property (TB,?,R,N) expandsGridSizeClassesForAccessibility;
```

## Instance methods

```
-[CCUIContentModule supportedGridSizeClasses];
-[CCUIContentModule contentViewController];
-[CCUIContentModule setContentModuleContext:];
-[CCUIContentModule backgroundViewController];
-[CCUIContentModule expandsGridSizeClassesForAccessibility];
-[CCUIContentModule contentViewControllerForContext:];
-[CCUIContentModule backgroundViewControllerForContext:];
-[CCUIContentModule moduleDescription];
```
