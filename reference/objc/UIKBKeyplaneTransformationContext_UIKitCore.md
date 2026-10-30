# `UIKBKeyplaneTransformationContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _usesScriptSwitch;
@"UIKBTree" _activeKeyboard;
@"UIKBTree" _activeKeyplane;
@"NSString" _currentKeyplaneName;
@"UIKBScreenTraits" _screenTraits;
d _resizingOffset;
@"<UIKBKeyplaneTransformationContextKeyboardLoader>" _additionalKeyboardLoader;
{CGSize="width"d"height"d} _keyboardSize;
```

## Properties

```
@property (T@"UIKBTree",&,N,V_activeKeyboard) activeKeyboard;
@property (T@"UIKBTree",&,N,V_activeKeyplane) activeKeyplane;
@property (T{CGSize=dd},N,V_keyboardSize) keyboardSize;
@property (T@"NSString",&,N,V_currentKeyplaneName) currentKeyplaneName;
@property (T@"UIKBScreenTraits",&,N,V_screenTraits) screenTraits;
@property (TB,N,V_usesScriptSwitch) usesScriptSwitch;
@property (Td,N,V_resizingOffset) resizingOffset;
@property (T@"<UIKBKeyplaneTransformationContextKeyboardLoader>",N,V_additionalKeyboardLoader) additionalKeyboardLoader;
```

## Instance methods

```
-[UIKBKeyplaneTransformationContext setScreenTraits:];
-[UIKBKeyplaneTransformationContext setResizingOffset:];
-[UIKBKeyplaneTransformationContext screenTraits];
-[UIKBKeyplaneTransformationContext setKeyboardSize:];
-[UIKBKeyplaneTransformationContext keyboardSize];
-[UIKBKeyplaneTransformationContext resizingOffset];
-[UIKBKeyplaneTransformationContext activeKeyboard];
-[UIKBKeyplaneTransformationContext activeKeyplane];
-[UIKBKeyplaneTransformationContext additionalKeyboardLoader];
-[UIKBKeyplaneTransformationContext currentKeyplaneName];
-[UIKBKeyplaneTransformationContext setActiveKeyboard:];
-[UIKBKeyplaneTransformationContext setActiveKeyplane:];
-[UIKBKeyplaneTransformationContext setAdditionalKeyboardLoader:];
-[UIKBKeyplaneTransformationContext setCurrentKeyplaneName:];
-[UIKBKeyplaneTransformationContext setUsesScriptSwitch:];
-[UIKBKeyplaneTransformationContext usesScriptSwitch];
```
