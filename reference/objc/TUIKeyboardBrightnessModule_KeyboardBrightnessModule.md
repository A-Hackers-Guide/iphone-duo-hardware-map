# `TUIKeyboardBrightnessModule`

- Image: [`/System/Library/ControlCenter/Bundles/KeyboardBrightnessModule.bundle/KeyboardBrightnessModule`](../userland/System__Library__ControlCenter__Bundles__KeyboardBrightnessModule.bundle__KeyboardBrightnessModule.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CCUIContentModule`
- 2 instance variables, 9 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"TUIKeyboardBrightnessModuleViewController" _viewController;
@"TUIKeyboardBrightnessBackgroundViewController" _backgroundViewController;
```

## Properties

```
@property (T@"UIViewController<CCUIContentModuleContentViewController>",?,R,N,V_viewController) contentViewController;
@property (T@"UIViewController<CCUIContentModuleBackgroundViewController>",?,R,N,V_backgroundViewController) backgroundViewController;
@property (TQ,?,R,N) supportedGridSizeClasses;
@property (T@"NSString",?,R,C,N) moduleDescription;
@property (TB,?,R,N) expandsGridSizeClassesForAccessibility;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUIKeyboardBrightnessModule previewProviderForContext:];
```

## Instance methods

```
-[TUIKeyboardBrightnessModule contentViewController];
-[TUIKeyboardBrightnessModule backgroundViewController];
-[TUIKeyboardBrightnessModule expandsGridSizeClassesForAccessibility];
-[TUIKeyboardBrightnessModule contentViewControllerForContext:];
-[TUIKeyboardBrightnessModule backgroundViewControllerForContext:];
```
