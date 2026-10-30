# `_UIContentViewEditingConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 6 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _useTextInputAsLabel;
B _selectAllTextWhenEditingBegins;
@? _didEndHandler;
@? _shouldBeginHandler;
@? _shouldChangeHandler;
@? _shouldEndHandler;
```

## Properties

```
@property (TB,N,V_useTextInputAsLabel) useTextInputAsLabel;
@property (TB,N,V_selectAllTextWhenEditingBegins) selectAllTextWhenEditingBegins;
@property (T@?,R,C,N,V_didEndHandler) didEndHandler;
@property (T@?,C,N,V_shouldBeginHandler) shouldBeginHandler;
@property (T@?,C,N,V_shouldChangeHandler) shouldChangeHandler;
@property (T@?,C,N,V_shouldEndHandler) shouldEndHandler;
```

## Instance methods

```
-[_UIContentViewEditingConfiguration shouldBeginHandler];
-[_UIContentViewEditingConfiguration setShouldBeginHandler:];
-[_UIContentViewEditingConfiguration copyWithZone:];
-[_UIContentViewEditingConfiguration isEqual:];
-[_UIContentViewEditingConfiguration didEndHandler];
-[_UIContentViewEditingConfiguration initWithDidEndHandler:];
-[_UIContentViewEditingConfiguration selectAllTextWhenEditingBegins];
-[_UIContentViewEditingConfiguration setSelectAllTextWhenEditingBegins:];
-[_UIContentViewEditingConfiguration setShouldChangeHandler:];
-[_UIContentViewEditingConfiguration setShouldEndHandler:];
-[_UIContentViewEditingConfiguration setUseTextInputAsLabel:];
-[_UIContentViewEditingConfiguration shouldChangeHandler];
-[_UIContentViewEditingConfiguration shouldEndHandler];
-[_UIContentViewEditingConfiguration useTextInputAsLabel];
```
