# `_UIFocusMapRect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIFocusMapArea`
- 2 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"<UICoordinateSpace>" _coordinateSpace;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
```

## Properties

```
@property (T@"<UICoordinateSpace>",R,W,N,V_coordinateSpace) coordinateSpace;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_frame) frame;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIFocusMapRect coordinateSpace];
-[_UIFocusMapRect description];
-[_UIFocusMapRect intersectsRect:];
-[_UIFocusMapRect frame];
-[_UIFocusMapRect initWithFrame:coordinateSpace:];
-[_UIFocusMapRect intersectionWithRegion:inSnapshot:];
-[_UIFocusMapRect intersectsRegion:inSnapshot:];
```
