# `CTCellIdInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 6 instance methods, 2 class methods

## Instance variables

```
@"NSNumber" _cellId;
@"NSNumber" _baseId;
```

## Properties

```
@property (T@"NSNumber",R,N,V_cellId) cellId;
@property (T@"NSNumber",R,N,V_baseId) baseId;
```

## Class methods

```
+[CTCellIdInfo supportsSecureCoding];
+[CTCellIdInfo cellIdInfoFromCellId:baseId:];
```

## Instance methods

```
-[CTCellIdInfo cellId];
-[CTCellIdInfo encodeWithCoder:];
-[CTCellIdInfo baseId];
-[CTCellIdInfo description];
-[CTCellIdInfo initWithCoder:];
-[CTCellIdInfo copyWithZone:];
```
