# `CCUIFlashlightModule`

- Image: [`/System/Library/ControlCenter/Bundles/FlashlightModule.bundle/FlashlightModule`](../userland/System__Library__ControlCenter__Bundles__FlashlightModule.bundle__FlashlightModule.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CCUIContentModule`
- 2 instance variables, 9 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"CCUIFlashlightModuleViewController" _viewController;
@"CCUIFlashlightBackgroundViewController" _backgroundViewController;
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
+[CCUIFlashlightModule previewProviderForContext:];
```

## Instance methods

```
-[CCUIFlashlightModule contentViewController];
-[CCUIFlashlightModule backgroundViewController];
-[CCUIFlashlightModule expandsGridSizeClassesForAccessibility];
-[CCUIFlashlightModule contentViewControllerForContext:];
-[CCUIFlashlightModule backgroundViewControllerForContext:];
```
