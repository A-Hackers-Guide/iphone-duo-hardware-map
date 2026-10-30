# `SBDodgingModel`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSMutableCopying`
- 4 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _identifiers;
@"NSMutableDictionary" _centersForIdentifiers;
@"NSMutableDictionary" _sizesForIdentifiers;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _referenceBounds;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_identifiers) identifiers;
@property (T@"NSMutableDictionary",&,N,V_centersForIdentifiers) centersForIdentifiers;
@property (T@"NSMutableDictionary",&,N,V_sizesForIdentifiers) sizesForIdentifiers;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_referenceBounds) referenceBounds;
```

## Instance methods

```
-[SBDodgingModel referenceBounds];
-[SBDodgingModel identifiers];
-[SBDodgingModel mutableCopyWithZone:];
-[SBDodgingModel setIdentifiers:];
-[SBDodgingModel setReferenceBounds:];
-[SBDodgingModel description];
-[SBDodgingModel initWithReferenceBounds:];
-[SBDodgingModel sizeForIdentifier:];
-[SBDodgingModel modelByModifyingModelWithBlock:];
-[SBDodgingModel centerForIdentifier:];
-[SBDodgingModel centersForIdentifiers];
-[SBDodgingModel setCentersForIdentifiers:];
-[SBDodgingModel setSizesForIdentifiers:];
-[SBDodgingModel sizesForIdentifiers];
```
