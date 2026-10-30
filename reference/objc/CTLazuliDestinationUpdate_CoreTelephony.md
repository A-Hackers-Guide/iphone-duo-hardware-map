# `CTLazuliDestinationUpdate`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _isBot;
@"CTLazuliDestination" _previous;
@"CTLazuliDestination" _discovered;
```

## Properties

```
@property (T@"CTLazuliDestination",&,N,V_previous) previous;
@property (T@"CTLazuliDestination",&,N,V_discovered) discovered;
@property (TB,N,V_isBot) isBot;
```

## Class methods

```
+[CTLazuliDestinationUpdate supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliDestinationUpdate setPrevious:];
-[CTLazuliDestinationUpdate previous];
-[CTLazuliDestinationUpdate encodeWithCoder:];
-[CTLazuliDestinationUpdate description];
-[CTLazuliDestinationUpdate initWithCoder:];
-[CTLazuliDestinationUpdate copyWithZone:];
-[CTLazuliDestinationUpdate isEqual:];
-[CTLazuliDestinationUpdate discovered];
-[CTLazuliDestinationUpdate initWithReflection:];
-[CTLazuliDestinationUpdate isBot];
-[CTLazuliDestinationUpdate isEqualToCTLazuliDestinationUpdate:];
-[CTLazuliDestinationUpdate setDiscovered:];
-[CTLazuliDestinationUpdate setIsBot:];
```
