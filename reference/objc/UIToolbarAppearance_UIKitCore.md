# `UIToolbarAppearance`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIBarAppearance`
- Protocols: `_UIBarButtonItemAppearanceChangeObserver`
- 2 instance variables, 7 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"UIBarButtonItemAppearance" _buttonAppearance;
@"UIBarButtonItemAppearance" _prominentButtonAppearance;
```

## Properties

```
@property (T@"UIBarButtonItemAppearance",C,N,V_buttonAppearance) buttonAppearance;
@property (T@"UIBarButtonItemAppearance",C,N,V_prominentButtonAppearance) prominentButtonAppearance;
@property (T@"UIBarButtonItemAppearance",C,N) doneButtonAppearance;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIToolbarAppearance supportsSecureCoding];
```

## Instance methods

```
-[UIToolbarAppearance prominentButtonAppearance];
-[UIToolbarAppearance setButtonAppearance:];
-[UIToolbarAppearance _checkEqualTo:];
-[UIToolbarAppearance _prominentButtonAppearance];
-[UIToolbarAppearance _describeInto:];
-[UIToolbarAppearance _decodeFromCoder:];
-[UIToolbarAppearance _setupDefaults];
-[UIToolbarAppearance setProminentButtonAppearance:];
-[UIToolbarAppearance _plainButtonAppearanceData];
-[UIToolbarAppearance encodeWithCoder:];
-[UIToolbarAppearance buttonAppearance];
-[UIToolbarAppearance doneButtonAppearance];
-[UIToolbarAppearance _plainButtonAppearance];
-[UIToolbarAppearance _prominentButtonAppearanceData];
-[UIToolbarAppearance _completeInit];
-[UIToolbarAppearance _barButtonItemDataChanged:];
-[UIToolbarAppearance _hashInto:];
-[UIToolbarAppearance _barButtonItemAppearanceChangedItemData:toItemData:fromItemData:];
-[UIToolbarAppearance _copyFromAppearance:];
-[UIToolbarAppearance setDoneButtonAppearance:];
```
