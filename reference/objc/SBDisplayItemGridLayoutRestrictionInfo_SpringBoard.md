# `SBDisplayItemGridLayoutRestrictionInfo`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 11 instance methods, 1 class methods

## Instance variables

```
Q _cachedHash;
Q _layoutRestrictions;
{CGSize="width"d"height"d} _restrictedSize;
```

## Properties

```
@property (TQ,R,N,V_layoutRestrictions) layoutRestrictions;
@property (T{CGSize=dd},R,N,V_restrictedSize) restrictedSize;
```

## Class methods

```
+[SBDisplayItemGridLayoutRestrictionInfo layoutRestrictionInfoWithLayoutRestrictions:restrictedSize:];
```

## Instance methods

```
-[SBDisplayItemGridLayoutRestrictionInfo succinctDescriptionBuilder];
-[SBDisplayItemGridLayoutRestrictionInfo descriptionWithMultilinePrefix:];
-[SBDisplayItemGridLayoutRestrictionInfo succinctDescription];
-[SBDisplayItemGridLayoutRestrictionInfo hash];
-[SBDisplayItemGridLayoutRestrictionInfo description];
-[SBDisplayItemGridLayoutRestrictionInfo copyWithZone:];
-[SBDisplayItemGridLayoutRestrictionInfo isEqual:];
-[SBDisplayItemGridLayoutRestrictionInfo descriptionBuilderWithMultilinePrefix:];
-[SBDisplayItemGridLayoutRestrictionInfo _initWithLayoutRestrictions:restrictedSize:];
-[SBDisplayItemGridLayoutRestrictionInfo layoutRestrictions];
-[SBDisplayItemGridLayoutRestrictionInfo restrictedSize];
```
