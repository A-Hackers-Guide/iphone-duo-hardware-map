# `_UIVelocityIntegrator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 16 properties, 31 instance methods, 0 class methods

## Instance variables

```
{deque<_UIVelocityIntegratorDataSample, std::allocator<_UIVelocityIntegratorDataSample>>="__map_"{__split_buffer<_UIVelocityIntegratorDataSample *, std::allocator<_UIVelocityIntegratorDataSample *>>="__first_"^^{_UIVelocityIntegratorDataSample}"__begin_"^^{_UIVelocityIntegratorDataSample}"__end_"^^{_UIVelocityIntegratorDataSample}""{?="__cap_"^^{_UIVelocityIntegratorDataSample}}}"__start_"Q""{?="__size_"Q}} _samples;
B _prefersDirectionlessAcceleration;
B _useSampleWindowForDifferentiation;
d _minimumRequiredMovement;
d _hysteresisTimeInterval;
q _maxNumberOfSamples;
@"_UIVelocityIntegratorFilter" _positionFilter;
@"_UIVelocityIntegratorFilter" _velocityFilter;
@"_UIVelocityIntegratorFilter" _accelerationFilter;
d _resetHysteresisOnSampleThetaDiff;
@? _didResetHysteresisOnThetaDiffHandler;
(?=""{?="x"d"y"d"z"d"_padding"d}"vector") _totalTranslation;
```

## Properties

```
@property (Td,N,V_minimumRequiredMovement) minimumRequiredMovement;
@property (T{CGPoint=dd},R,N) position;
@property (T{CGVector=dd},R,N) velocity;
@property (T{CGVector=dd},R,N) acceleration;
@property (T{CGVector=dd},R,N) offset;
@property (Td,N,V_hysteresisTimeInterval) hysteresisTimeInterval;
@property (Tq,N,V_maxNumberOfSamples) maxNumberOfSamples;
@property (TB,N,V_prefersDirectionlessAcceleration) prefersDirectionlessAcceleration;
@property (TB,N,V_useSampleWindowForDifferentiation) useSampleWindowForDifferentiation;
@property (T@"_UIVelocityIntegratorFilter",&,N,V_positionFilter) positionFilter;
@property (T@"_UIVelocityIntegratorFilter",&,N,V_velocityFilter) velocityFilter;
@property (T@"_UIVelocityIntegratorFilter",&,N,V_accelerationFilter) accelerationFilter;
@property (T(?={?=dddd}),R,N) position3D;
@property (T(?={?=dddd}),R,N) offset3D;
@property (T(?={?=dddd}),R,N) velocity3D;
@property (T(?={?=dddd}),R,N) acceleration3D;
```

## Instance methods

```
-[_UIVelocityIntegrator addSample:];
-[_UIVelocityIntegrator position];
-[_UIVelocityIntegrator hysteresisTimeInterval];
-[_UIVelocityIntegrator accelerationFilter];
-[_UIVelocityIntegrator init];
-[_UIVelocityIntegrator minimumRequiredMovement];
-[_UIVelocityIntegrator acceleration3D];
-[_UIVelocityIntegrator prefersDirectionlessAcceleration];
-[_UIVelocityIntegrator position3D];
-[_UIVelocityIntegrator acceleration];
-[_UIVelocityIntegrator reset];
-[_UIVelocityIntegrator addSample:withTimestamp:];
-[_UIVelocityIntegrator velocity];
-[_UIVelocityIntegrator setHysteresisTimeInterval:];
-[_UIVelocityIntegrator setMaxNumberOfSamples:];
-[_UIVelocityIntegrator setMinimumRequiredMovement:];
-[_UIVelocityIntegrator hasVelocity];
-[_UIVelocityIntegrator setPositionFilter:];
-[_UIVelocityIntegrator addSample3D:];
-[_UIVelocityIntegrator setVelocityFilter:];
-[_UIVelocityIntegrator setUseSampleWindowForDifferentiation:];
-[_UIVelocityIntegrator setPrefersDirectionlessAcceleration:];
-[_UIVelocityIntegrator offset3D];
-[_UIVelocityIntegrator velocity3D];
-[_UIVelocityIntegrator positionFilter];
-[_UIVelocityIntegrator maxNumberOfSamples];
-[_UIVelocityIntegrator velocityFilter];
-[_UIVelocityIntegrator addSample3D:withTimestamp:];
-[_UIVelocityIntegrator useSampleWindowForDifferentiation];
-[_UIVelocityIntegrator offset];
-[_UIVelocityIntegrator setAccelerationFilter:];
```
