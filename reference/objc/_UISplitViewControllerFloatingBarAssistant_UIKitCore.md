# `_UISplitViewControllerFloatingBarAssistant`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 3 properties, 17 instance methods, 0 class methods

## Instance variables

```
? floatingBars;
floatingProxys;
inheritedFloatingProxys;
? splitViewController;
@"_UIScrollPocketCollectorInteraction" collectorInteraction;
```

## Properties

```
@property (T@"NSArray",N,C) floatingBars;
@property (T@"UISplitViewController",N,W,VsplitViewController) splitViewController;
@property (T@"_UIScrollPocketCollectorInteraction",N,R,VcollectorInteraction) collectorInteraction;
```

## Instance methods

```
-[_UISplitViewControllerFloatingBarAssistant splitViewController];
-[_UISplitViewControllerFloatingBarAssistant floatingBarProxyForColumn:planeLevel:];
-[_UISplitViewControllerFloatingBarAssistant init];
-[_UISplitViewControllerFloatingBarAssistant prepareForLayout:];
-[_UISplitViewControllerFloatingBarAssistant containerViewForPlaneLevel:];
-[_UISplitViewControllerFloatingBarAssistant floatingBars];
-[_UISplitViewControllerFloatingBarAssistant collectorInteraction];
-[_UISplitViewControllerFloatingBarAssistant floatingBarContainerProxyForTraitCollection:layout:column:];
-[_UISplitViewControllerFloatingBarAssistant supportsDimmingLevelForPlaneLevel:];
-[_UISplitViewControllerFloatingBarAssistant setFloatingBars:];
-[_UISplitViewControllerFloatingBarAssistant initWithSplitViewController:];
-[_UISplitViewControllerFloatingBarAssistant updateDimmingLevel:planeLevel:];
-[_UISplitViewControllerFloatingBarAssistant setSplitViewController:];
-[_UISplitViewControllerFloatingBarAssistant viewSubtreeDidGainScrollView:enclosingViewController:layout:];
-[_UISplitViewControllerFloatingBarAssistant prepareView:];
-[_UISplitViewControllerFloatingBarAssistant resolvedInheritedProxyWithTraitCollection:column:];
-[_UISplitViewControllerFloatingBarAssistant inheritedFloatingBarProxyWithFloatingBar:host:column:updateMode:];
```
