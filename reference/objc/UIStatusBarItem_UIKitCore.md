# `UIStatusBarItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 6 properties, 17 instance methods, 5 class methods

## Instance variables

```
q _idiom;
i _type;
```

## Properties

```
@property (Ti,R,N,V_type) type;
@property (T#,R,N) viewClass;
@property (Ti,R,N) priority;
@property (Ti,R,N) leftOrder;
@property (Ti,R,N) rightOrder;
@property (T@"NSString",R,N) indicatorName;
```

## Class methods

```
+[UIStatusBarItem itemType:idiom:appearsInRegion:];
+[UIStatusBarItem isItemWithTypeExclusive:outBlacklistItems:outWhitelistItems:];
+[UIStatusBarItem itemType:idiom:canBeEnabledForData:style:];
+[UIStatusBarItem itemWithType:idiom:];
+[UIStatusBarItem typeIsValid:];
```

## Instance methods

```
-[UIStatusBarItem priority];
-[UIStatusBarItem initWithType:];
-[UIStatusBarItem type];
-[UIStatusBarItem description];
-[UIStatusBarItem leftOrder];
-[UIStatusBarItem rightOrder];
-[UIStatusBarItem appearsOnCenter];
-[UIStatusBarItem appearsInRegion:];
-[UIStatusBarItem appearsOnLeft];
-[UIStatusBarItem appearsOnRight];
-[UIStatusBarItem centerOrder];
-[UIStatusBarItem compareCenterOrder:];
-[UIStatusBarItem compareLeftOrder:];
-[UIStatusBarItem comparePriority:];
-[UIStatusBarItem compareRightOrder:];
-[UIStatusBarItem indicatorName];
-[UIStatusBarItem viewClass];
```
