# `UISheetPresentationControllerDetent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCSecureCoding`, `NSSecureCoding`
- 6 instance variables, 11 properties, 18 instance methods, 14 class methods

## Instance variables

```
B __createdWithDeprecatedInitializer;
@"NSString" _identifier;
@"UIVisualEffect" _backgroundEffect;
q __type;
@? __internalBlock;
d __constant;
```

## Properties

```
@property (Tq,R,N,V__type) _type;
@property (T@?,R,N,V__internalBlock) _internalBlock;
@property (Td,R,N,V__constant) _constant;
@property (TB,R,N,V__createdWithDeprecatedInitializer) _createdWithDeprecatedInitializer;
@property (T@"NSString",R,N) _identifier;
@property (T@"NSString",R,N,V_identifier) identifier;
@property (T@"UIVisualEffect",&,N,V_backgroundEffect) backgroundEffect;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISheetPresentationControllerDetent supportsBSXPCSecureCoding];
+[UISheetPresentationControllerDetent supportsSecureCoding];
+[UISheetPresentationControllerDetent largeDetent];
+[UISheetPresentationControllerDetent customDetentWithIdentifier:resolver:];
+[UISheetPresentationControllerDetent _detentWithResolutionContextBlock:];
+[UISheetPresentationControllerDetent _maximumDetent];
+[UISheetPresentationControllerDetent _fullDetent];
+[UISheetPresentationControllerDetent _barDetent];
+[UISheetPresentationControllerDetent _detentWithIdentifier:resolutionContextBlock:];
+[UISheetPresentationControllerDetent _detentWithContainerViewBlock:];
+[UISheetPresentationControllerDetent mediumDetent];
+[UISheetPresentationControllerDetent _detentWithIdentifier:containerViewBlock:];
+[UISheetPresentationControllerDetent _detentWithIdentifier:constant:];
+[UISheetPresentationControllerDetent _minimumDetent];
```

## Instance methods

```
-[UISheetPresentationControllerDetent _type];
-[UISheetPresentationControllerDetent _setIdentifier:];
-[UISheetPresentationControllerDetent setBackgroundEffect:];
-[UISheetPresentationControllerDetent identifier];
-[UISheetPresentationControllerDetent initWithType:identifier:internalBlock:constant:];
-[UISheetPresentationControllerDetent _internalBlock];
-[UISheetPresentationControllerDetent _createdWithDeprecatedInitializer];
-[UISheetPresentationControllerDetent _constant];
-[UISheetPresentationControllerDetent resolvedValueInContext:];
-[UISheetPresentationControllerDetent backgroundEffect];
-[UISheetPresentationControllerDetent encodeWithCoder:];
-[UISheetPresentationControllerDetent description];
-[UISheetPresentationControllerDetent initWithCoder:];
-[UISheetPresentationControllerDetent encodeWithBSXPCCoder:];
-[UISheetPresentationControllerDetent initWithBSXPCCoder:];
-[UISheetPresentationControllerDetent _valueInResolutionContext:];
-[UISheetPresentationControllerDetent isEqual:];
-[UISheetPresentationControllerDetent _identifier];
```
