# `_UICustomTraitStorage`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 5 properties, 23 instance methods, 1 class methods

## Instance variables

```
valuesByToken;
valuesByIdentifier;
lastPromotedAtTokenGeneration;
```

## Properties

```
@property (TB,N,R) isEmpty;
@property (Tq,N,R) count;
@property (T{?=@[4Q]},N,R) locked_specifiedTraitTokens;
@property (Tq,N,R) hash;
@property (T@"NSString",N,R) description;
```

## Class methods

```
+[_UICustomTraitStorage appendTraitChangeDescriptionsTo:includePrivate:fromTraits:toTraits:];
```

## Instance methods

```
-[_UICustomTraitStorage hasValueForTraitWithToken:];
-[_UICustomTraitStorage locked_hasValueForTraitWithToken:];
-[_UICustomTraitStorage locked_enumerateLegacyClientDefinedTraitsUsingBlock:];
-[_UICustomTraitStorage init];
-[_UICustomTraitStorage mergeFrom:];
-[_UICustomTraitStorage setValue:forTraitWithToken:dataType:acquireLock:];
-[_UICustomTraitStorage locked_specifiedTraitTokens];
-[_UICustomTraitStorage count];
-[_UICustomTraitStorage initWithCoder:encodedKeys:];
-[_UICustomTraitStorage mergeLegacyClientDefinedTraits:];
-[_UICustomTraitStorage removeValueForTraitWithToken:];
-[_UICustomTraitStorage isEmpty];
-[_UICustomTraitStorage initWithLegacyClientDefinedTraits:];
-[_UICustomTraitStorage encodeWithCoder:];
-[_UICustomTraitStorage hash];
-[_UICustomTraitStorage description];
-[_UICustomTraitStorage commonTraitTokensDifferingFrom:];
-[_UICustomTraitStorage objectForLegacyClientDefinedTraitWithName:];
-[_UICustomTraitStorage copyWithZone:];
-[_UICustomTraitStorage isEqual:];
-[_UICustomTraitStorage appendTraitDescriptionsTo:includePrivate:];
-[_UICustomTraitStorage setObject:forLegacyClientDefinedTraitWithName:];
-[_UICustomTraitStorage valueForTraitWithToken:dataType:defaultValue:acquireLock:];
```
