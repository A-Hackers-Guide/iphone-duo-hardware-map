# `_UISceneBarPositionResolver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCSecureCoding`
- 1 instance variables, 2 properties, 15 instance methods, 1 class methods

## Instance variables

```
barPosition;
```

## Properties

```
@property (T@"NSString",N,R) description;
@property (Tq,N,R) hash;
```

## Class methods

```
+[_UISceneBarPositionResolver supportsBSXPCSecureCoding];
```

## Instance methods

```
-[_UISceneBarPositionResolver initWithRotatingPreferredBarPositionForPortrait:];
-[_UISceneBarPositionResolver initWithPreferredBarPositionForPortrait:landscape:];
-[_UISceneBarPositionResolver initWithRotatingPreferredVerticalBarPositionForPortraitAndLandscapeLeft:];
-[_UISceneBarPositionResolver init];
-[_UISceneBarPositionResolver initWithRotatingPreferredVerticalBarPositionForPortraitAndLandscapeRight:];
-[_UISceneBarPositionResolver initWithVerticalBarEdge:systemHorizontalEdge:layoutDirection:];
-[_UISceneBarPositionResolver preferredBarPositionForOrientation:];
-[_UISceneBarPositionResolver hash];
-[_UISceneBarPositionResolver description];
-[_UISceneBarPositionResolver encodeWithBSXPCCoder:];
-[_UISceneBarPositionResolver initWithBSXPCCoder:];
-[_UISceneBarPositionResolver initWithPreferredBarPosition:];
-[_UISceneBarPositionResolver isEqual:];
-[_UISceneBarPositionResolver initWithRotatingPreferredVerticalBarPositionForPortraitAndLanscapeRight:];
-[_UISceneBarPositionResolver initWithRotatingPreferredVerticalBarPositionForPortraitAndLanscapeLeft:];
```
