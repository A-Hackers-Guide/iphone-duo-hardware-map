# `UITextFormattingCoordinator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIFontPickerViewControllerDelegate`
- 1 instance variables, 5 properties, 6 instance methods, 3 class methods

## Instance variables

```
@"<UITextFormattingCoordinatorDelegate>" _delegate;
```

## Properties

```
@property (T@"<UITextFormattingCoordinatorDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UITextFormattingCoordinator isFontPanelVisible];
+[UITextFormattingCoordinator textFormattingCoordinatorForWindowScene:];
+[UITextFormattingCoordinator toggleFontPanel:];
```

## Instance methods

```
-[UITextFormattingCoordinator fontPickerViewControllerDidPickFont:];
-[UITextFormattingCoordinator initWithWindowScene:];
-[UITextFormattingCoordinator setDelegate:];
-[UITextFormattingCoordinator setSelectedAttributes:isMultiple:];
-[UITextFormattingCoordinator delegate];
-[UITextFormattingCoordinator updateTextAttributesWithConversionHandler:];
```
