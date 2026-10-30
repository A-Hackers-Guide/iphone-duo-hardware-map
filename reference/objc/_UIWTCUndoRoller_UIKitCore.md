# `_UIWTCUndoRoller`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSMutableAttributedString" _rolledReplacement;
Q _offset;
B _hasFouled;
@"NSAttributedString" _evaluatedText;
```

## Properties

```
@property (T@"NSAttributedString",R,N) rolledReplacement;
@property (T@"NSAttributedString",R,N,V_evaluatedText) evaluatedText;
@property (TQ,R,N,V_offset) offset;
@property (TB,R,N,V_hasFouled) hasFouled;
```

## Instance methods

```
-[_UIWTCUndoRoller replaceRange:withText:];
-[_UIWTCUndoRoller offset];
-[_UIWTCUndoRoller evaluatedText];
-[_UIWTCUndoRoller hasFouled];
-[_UIWTCUndoRoller initWithEvaluatedText:offset:];
-[_UIWTCUndoRoller rolledReplacement];
```
