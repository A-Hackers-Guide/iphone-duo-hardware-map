# `CCUIDisplayModule`

- Image: [`/System/Library/ControlCenter/Bundles/DisplayModule.bundle/DisplayModule`](../userland/System__Library__ControlCenter__Bundles__DisplayModule.bundle__DisplayModule.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CCUIContentModule`, `CCUIDisplayModuleViewControllerDelegate`
- 3 instance variables, 10 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"CCUIDisplayModuleViewController" _moduleViewController;
@"CCUIDisplayBackgroundViewController" _backgroundViewController;
@"CCUIContentModuleContext" _contentModuleContext;
```

## Properties

```
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
```

## Class methods

```
+[CCUIDisplayModule previewProviderForContext:];
```

## Instance methods

```
-[CCUIDisplayModule contentModuleContext];
-[CCUIDisplayModule supportedGridSizeClasses];
-[CCUIDisplayModule setContentModuleContext:];
-[CCUIDisplayModule contentViewControllerForContext:];
-[CCUIDisplayModule backgroundViewControllerForContext:];
-[CCUIDisplayModule displayModuleViewController:brightnessDidChange:];
```
