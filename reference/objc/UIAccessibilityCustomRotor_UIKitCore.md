# `UIAccessibilityCustomRotor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" uuid;
@ targetElement;
q systemRotorType;
@"NSAttributedString" _attributedName;
@? _itemSearchBlock;
```

## Properties

```
@property (T@"NSUUID",&,N,Vuuid) uuid;
@property (T@,W,N,VtargetElement) targetElement;
@property (Tq,N,VsystemRotorType) systemRotorType;
@property (T@"NSString",C,N) name;
@property (T@"NSAttributedString",C,N,V_attributedName) attributedName;
@property (T@?,C,N,V_itemSearchBlock) itemSearchBlock;
```

## Instance methods

```
-[UIAccessibilityCustomRotor uuid];
-[UIAccessibilityCustomRotor attributedName];
-[UIAccessibilityCustomRotor setUuid:];
-[UIAccessibilityCustomRotor setName:];
-[UIAccessibilityCustomRotor name];
-[UIAccessibilityCustomRotor systemRotorType];
-[UIAccessibilityCustomRotor itemSearchBlock];
-[UIAccessibilityCustomRotor initWithAttributedName:itemSearchBlock:];
-[UIAccessibilityCustomRotor initWithName:itemSearchBlock:];
-[UIAccessibilityCustomRotor initWithSystemType:itemSearchBlock:];
-[UIAccessibilityCustomRotor setAttributedName:];
-[UIAccessibilityCustomRotor setItemSearchBlock:];
-[UIAccessibilityCustomRotor setSystemRotorType:];
-[UIAccessibilityCustomRotor setTargetElement:];
-[UIAccessibilityCustomRotor targetElement];
```
