# `_UIFindNavigatorViewLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 12 instance variables, 21 properties, 40 instance methods, 0 class methods

## Instance variables

```
B _replaceFieldVisible;
B _usesCompactStyling;
B _usesAssistantBarHeight;
B _usesSymbolForDoneButton;
B _usesNextAndPreviousArrows;
@"UIButton" _nextResultButton;
@"UIButton" _previousResultButton;
@"UIButton" _doneButton;
@"UIButton" _replaceButton;
@"UIView" _searchTextField;
@"UIView" _replaceTextField;
q _assistantBarStyle;
```

## Properties

```
@property (T@"UIButton",&,N,V_nextResultButton) nextResultButton;
@property (T@"UIButton",&,N,V_previousResultButton) previousResultButton;
@property (T@"UIButton",&,N,V_doneButton) doneButton;
@property (T@"UIButton",&,N,V_replaceButton) replaceButton;
@property (T@"UIView",&,N,V_searchTextField) searchTextField;
@property (T@"UIView",&,N,V_replaceTextField) replaceTextField;
@property (TB,N,V_replaceFieldVisible) replaceFieldVisible;
@property (TB,N,V_usesCompactStyling) usesCompactStyling;
@property (TB,N,V_usesAssistantBarHeight) usesAssistantBarHeight;
@property (Tq,N,V_assistantBarStyle) assistantBarStyle;
@property (T{CGSize=dd},R,N) preferredContentSize;
@property (T@"UIFont",R,N) preferredTextFieldFont;
@property (T@"UIColor",R,N) preferredOpaqueBackgroundColor;
@property (T@"UIImageSymbolConfiguration",R,N) preferredSymbolConfigurationForImageForTextFields;
@property (T@"NSString",R,N) preferredMaximumContentSizeCategory;
@property (Td,R,N) preferredCornerRadius;
@property (Td,R,N) preferredHorizontalPadding;
@property (Td,R,N) preferredVerticalPadding;
@property (TB,R,N) showsReplaceInOptionsMenu;
@property (TB,R,N,V_usesSymbolForDoneButton) usesSymbolForDoneButton;
@property (TB,R,N,V_usesNextAndPreviousArrows) usesNextAndPreviousArrows;
```

## Instance methods

```
-[_UIFindNavigatorViewLayout setDoneButton:];
-[_UIFindNavigatorViewLayout doneButton];
-[_UIFindNavigatorViewLayout setAssistantBarStyle:];
-[_UIFindNavigatorViewLayout searchTextField];
-[_UIFindNavigatorViewLayout preferredCornerRadius];
-[_UIFindNavigatorViewLayout assistantBarStyle];
-[_UIFindNavigatorViewLayout preferredContentSize];
-[_UIFindNavigatorViewLayout setSearchTextField:];
-[_UIFindNavigatorViewLayout isEqual:];
-[_UIFindNavigatorViewLayout _preferredIntrinsicRowHeight];
-[_UIFindNavigatorViewLayout _setAndActivateConstraints];
-[_UIFindNavigatorViewLayout addMaterialToViewIfNeeded:];
-[_UIFindNavigatorViewLayout applyStyleToFieldIfNeeded:];
-[_UIFindNavigatorViewLayout commonButtonConfigWithGlass:withCompletion:];
-[_UIFindNavigatorViewLayout commonButtonConfigWithImageName:isAccessory:];
-[_UIFindNavigatorViewLayout commonButtonConfigWithTitle:isGlass:];
-[_UIFindNavigatorViewLayout nextResultButton];
-[_UIFindNavigatorViewLayout preferredHorizontalPadding];
-[_UIFindNavigatorViewLayout preferredMaximumContentSizeCategory];
-[_UIFindNavigatorViewLayout preferredOpaqueBackgroundColor];
-[_UIFindNavigatorViewLayout preferredSymbolConfigurationForImageForTextFields];
-[_UIFindNavigatorViewLayout preferredTextFieldFont];
-[_UIFindNavigatorViewLayout preferredVerticalPadding];
-[_UIFindNavigatorViewLayout prepareForLayout];
-[_UIFindNavigatorViewLayout previousResultButton];
-[_UIFindNavigatorViewLayout replaceButton];
-[_UIFindNavigatorViewLayout replaceFieldVisible];
-[_UIFindNavigatorViewLayout replaceTextField];
-[_UIFindNavigatorViewLayout setNextResultButton:];
-[_UIFindNavigatorViewLayout setPreviousResultButton:];
-[_UIFindNavigatorViewLayout setReplaceButton:];
-[_UIFindNavigatorViewLayout setReplaceFieldVisible:];
-[_UIFindNavigatorViewLayout setReplaceTextField:];
-[_UIFindNavigatorViewLayout setUsesAssistantBarHeight:];
-[_UIFindNavigatorViewLayout setUsesCompactStyling:];
-[_UIFindNavigatorViewLayout showsReplaceInOptionsMenu];
-[_UIFindNavigatorViewLayout usesAssistantBarHeight];
-[_UIFindNavigatorViewLayout usesCompactStyling];
-[_UIFindNavigatorViewLayout usesNextAndPreviousArrows];
-[_UIFindNavigatorViewLayout usesSymbolForDoneButton];
```
