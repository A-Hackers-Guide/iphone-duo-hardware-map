# `UISliderTrackConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSCoding`, `_UISliderTickProvidingConfiguration`, `_UISliderConfiguration`
- 1 instance variables, 11 properties, 22 instance methods, 2 class methods

## Instance variables

```
_configuration;
```

## Properties

```
@property (TB,N) allowsTickValuesOnly;
@property (Tf,N) neutralValue;
@property (Tf,N) minimumEnabledValue;
@property (Tf,N) maximumEnabledValue;
@property (T@"NSArray",N,R) ticks;
@property (Tq,N,R) behavior;
@property (Tq,N,R) tickStyle;
@property (Td,N,R) neutralPosition;
@property (Tf,N,R) snappingDistance;
@property (TB,N,R) ticksAreEvenlySpaced;
@property (Tq,N,R) hash;
```

## Class methods

```
+[UISliderTrackConfiguration configurationWithNumberOfTicks:];
+[UISliderTrackConfiguration configurationWithTicks:];
```

## Instance methods

```
-[UISliderTrackConfiguration tickStyle];
-[UISliderTrackConfiguration maximumEnabledValue];
-[UISliderTrackConfiguration init];
-[UISliderTrackConfiguration ticks];
-[UISliderTrackConfiguration minimumEnabledValue];
-[UISliderTrackConfiguration behavior];
-[UISliderTrackConfiguration snappingDistance];
-[UISliderTrackConfiguration encodeWithCoder:];
-[UISliderTrackConfiguration hash];
-[UISliderTrackConfiguration initWithCoder:];
-[UISliderTrackConfiguration neutralPosition];
-[UISliderTrackConfiguration copyWithZone:];
-[UISliderTrackConfiguration setMinimumEnabledValue:];
-[UISliderTrackConfiguration isEqual:];
-[UISliderTrackConfiguration ticksAreEvenlySpaced];
-[UISliderTrackConfiguration setMaximumEnabledValue:];
-[UISliderTrackConfiguration adjustPositionForTargetPosition:adjustedPosition:startPosition:endPosition:];
-[UISliderTrackConfiguration allowsTickValuesOnly];
-[UISliderTrackConfiguration initWithTicks:number:evenlySpaced:];
-[UISliderTrackConfiguration neutralValue];
-[UISliderTrackConfiguration setAllowsTickValuesOnly:];
-[UISliderTrackConfiguration setNeutralValue:];
```
