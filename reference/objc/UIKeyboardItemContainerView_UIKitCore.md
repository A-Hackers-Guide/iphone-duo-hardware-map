# `UIKeyboardItemContainerView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIInputSetHostView`
- 5 instance variables, 5 properties, 12 instance methods, 2 class methods

## Instance variables

```
@"UILayoutGuide" _belowInputLayoutGuide;
@"UILayoutGuide" _inputViewLayoutGuide;
@"UILayoutGuide" _assistantLayoutGuide;
@"UILayoutGuide" _aboveAssistantLayoutGuide;
@"NSArray" _guideConstraints;
```

## Properties

```
@property (T@"UILayoutGuide",&,N,V_belowInputLayoutGuide) belowInputLayoutGuide;
@property (T@"UILayoutGuide",&,N,V_inputViewLayoutGuide) inputViewLayoutGuide;
@property (T@"UILayoutGuide",&,N,V_assistantLayoutGuide) assistantLayoutGuide;
@property (T@"UILayoutGuide",&,N,V_aboveAssistantLayoutGuide) aboveAssistantLayoutGuide;
@property (T@"NSArray",&,N,V_guideConstraints) guideConstraints;
```

## Class methods

```
+[UIKeyboardItemContainerView requiresConstraintBasedLayout];
+[UIKeyboardItemContainerView _notifyOnExplicitLayout];
```

## Instance methods

```
-[UIKeyboardItemContainerView constrainGuidesIfNeeded];
-[UIKeyboardItemContainerView belowInputLayoutGuide];
-[UIKeyboardItemContainerView inputViewLayoutGuide];
-[UIKeyboardItemContainerView setAssistantLayoutGuide:];
-[UIKeyboardItemContainerView setInputViewLayoutGuide:];
-[UIKeyboardItemContainerView setBelowInputLayoutGuide:];
-[UIKeyboardItemContainerView aboveAssistantLayoutGuide];
-[UIKeyboardItemContainerView setGuideConstraints:];
-[UIKeyboardItemContainerView guideConstraints];
-[UIKeyboardItemContainerView initWithFrame:];
-[UIKeyboardItemContainerView assistantLayoutGuide];
-[UIKeyboardItemContainerView setAboveAssistantLayoutGuide:];
```
