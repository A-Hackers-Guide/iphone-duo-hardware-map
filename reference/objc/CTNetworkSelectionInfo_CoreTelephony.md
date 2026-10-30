# `CTNetworkSelectionInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
Q _selectionState;
Q _selectionMode;
@"CTNetwork" _selection;
```

## Properties

```
@property (TQ,N,V_selectionState) selectionState;
@property (TQ,N,V_selectionMode) selectionMode;
@property (T@"CTNetwork",&,N,V_selection) selection;
```

## Class methods

```
+[CTNetworkSelectionInfo supportsSecureCoding];
```

## Instance methods

```
-[CTNetworkSelectionInfo selection];
-[CTNetworkSelectionInfo setSelection:];
-[CTNetworkSelectionInfo setSelectionState:];
-[CTNetworkSelectionInfo encodeWithCoder:];
-[CTNetworkSelectionInfo description];
-[CTNetworkSelectionInfo initWithCoder:];
-[CTNetworkSelectionInfo copyWithZone:];
-[CTNetworkSelectionInfo selectionState];
-[CTNetworkSelectionInfo selectionMode];
-[CTNetworkSelectionInfo setSelectionMode:];
```
