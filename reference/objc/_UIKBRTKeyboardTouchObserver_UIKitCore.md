# `_UIKBRTKeyboardTouchObserver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 23 instance methods, 0 class methods

## Instance variables

```
i _homeRowOffsetIndex;
@"NSArray" _rowOffsets;
@"NSArray" _rowXEdges;
@"NSArray" _rowYEdgesLeft;
@"NSArray" _rowYEdgesRight;
{CGPoint="x"d"y"d} _fCenter;
{CGPoint="x"d"y"d} _jCenter;
{CGSize="width"d"height"d} _keySize;
```

## Properties

```
@property (T{CGPoint=dd},N,V_fCenter) fCenter;
@property (T{CGPoint=dd},N,V_jCenter) jCenter;
@property (T{CGSize=dd},N,V_keySize) keySize;
@property (T@"NSArray",&,N,V_rowOffsets) rowOffsets;
@property (Ti,N,V_homeRowOffsetIndex) homeRowOffsetIndex;
@property (T@"NSArray",&,N,V_rowXEdges) rowXEdges;
@property (T@"NSArray",&,N,V_rowYEdgesLeft) rowYEdgesLeft;
@property (T@"NSArray",&,N,V_rowYEdgesRight) rowYEdgesRight;
```

## Instance methods

```
-[_UIKBRTKeyboardTouchObserver reset];
-[_UIKBRTKeyboardTouchObserver keySize];
-[_UIKBRTKeyboardTouchObserver fCenter];
-[_UIKBRTKeyboardTouchObserver jCenter];
-[_UIKBRTKeyboardTouchObserver addTouchLocation:withRadius:withIdentifier:];
-[_UIKBRTKeyboardTouchObserver addTouchLocation:withRadius:withTouchTime:withIdentifier:];
-[_UIKBRTKeyboardTouchObserver homeRowOffsetIndex];
-[_UIKBRTKeyboardTouchObserver moveTouchWithIdentifier:toLocation:withRadius:atTouchTime:];
-[_UIKBRTKeyboardTouchObserver removeTouchWithIdentifier:];
-[_UIKBRTKeyboardTouchObserver removeTouchWithIdentifier:touchCancelled:];
-[_UIKBRTKeyboardTouchObserver rowOffsets];
-[_UIKBRTKeyboardTouchObserver rowXEdges];
-[_UIKBRTKeyboardTouchObserver rowYEdgesLeft];
-[_UIKBRTKeyboardTouchObserver rowYEdgesRight];
-[_UIKBRTKeyboardTouchObserver setFCenter:];
-[_UIKBRTKeyboardTouchObserver setHomeRowOffsetIndex:];
-[_UIKBRTKeyboardTouchObserver setJCenter:];
-[_UIKBRTKeyboardTouchObserver setKeySize:];
-[_UIKBRTKeyboardTouchObserver setRowOffsets:];
-[_UIKBRTKeyboardTouchObserver setRowXEdges:];
-[_UIKBRTKeyboardTouchObserver setRowYEdgesLeft:];
-[_UIKBRTKeyboardTouchObserver setRowYEdgesRight:];
-[_UIKBRTKeyboardTouchObserver updateWithFCenter:jCenter:keySize:rowOffsets:homeRowOffsetIndex:];
```
