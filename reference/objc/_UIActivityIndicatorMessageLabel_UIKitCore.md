# `_UIActivityIndicatorMessageLabel`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UILabel`
- 2 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _regularTextAttributes;
@"NSDictionary" _effectiveTextAttributes;
```

## Properties

```
@property (T@"NSDictionary",C,N,V_regularTextAttributes) regularTextAttributes;
@property (T@"NSDictionary",R,C,N,V_effectiveTextAttributes) effectiveTextAttributes;
@property (Td,R,N) verticalSpacingToSpinner;
```

## Class methods

```
+[_UIActivityIndicatorMessageLabel defaultRegularContentSizeTextAttributes];
```

## Instance methods

```
-[_UIActivityIndicatorMessageLabel setAttributedText:];
-[_UIActivityIndicatorMessageLabel traitCollectionDidChange:];
-[_UIActivityIndicatorMessageLabel setText:];
-[_UIActivityIndicatorMessageLabel _effectiveAttributesDerivedFromRegularTextAttributes:];
-[_UIActivityIndicatorMessageLabel _effectiveVerticalSpacingToSpinner];
-[_UIActivityIndicatorMessageLabel _ensureCapableOfCalculatingBaselineOffsets];
-[_UIActivityIndicatorMessageLabel _validatedAttributedString:];
-[_UIActivityIndicatorMessageLabel effectiveTextAttributes];
-[_UIActivityIndicatorMessageLabel initWithRegularTextAttributes:];
-[_UIActivityIndicatorMessageLabel regularTextAttributes];
-[_UIActivityIndicatorMessageLabel setEffectiveTextAttributes:];
-[_UIActivityIndicatorMessageLabel setRegularTextAttributes:];
-[_UIActivityIndicatorMessageLabel verticalSpacingToSpinner];
```
