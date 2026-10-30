# `CAFSoundDistribution`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 11 properties, 21 instance methods, 2 class methods

## Properties

```
@property (T@"CAFInt8Characteristic",R,N) balanceCharacteristic;
@property (T@"CAFInt8Characteristic",R,N) fadeCharacteristic;
@property (Tc,N) balance;
@property (T@"CAFInt8Range",R,N) balanceRange;
@property (TB,R,N) balanceDisabled;
@property (TB,R,N) balanceHidden;
@property (Tc,N) fade;
@property (T@"CAFInt8Range",R,N) fadeRange;
@property (TB,R,N) hasFade;
@property (TB,R,N) fadeDisabled;
@property (TB,R,N) fadeHidden;
```

## Class methods

```
+[CAFSoundDistribution serviceIdentifier];
+[CAFSoundDistribution observerProtocol];
```

## Instance methods

```
-[CAFSoundDistribution removeObserver:];
-[CAFSoundDistribution addObserver:];
-[CAFSoundDistribution registerObserver:];
-[CAFSoundDistribution name];
-[CAFSoundDistribution unregisterObserver:];
-[CAFSoundDistribution fade];
-[CAFSoundDistribution balance];
-[CAFSoundDistribution setBalance:];
-[CAFSoundDistribution setFade:];
-[CAFSoundDistribution hasFade];
-[CAFSoundDistribution registeredForBalance];
-[CAFSoundDistribution registeredForFade];
-[CAFSoundDistribution balanceDisabled];
-[CAFSoundDistribution balanceHidden];
-[CAFSoundDistribution balanceRange];
-[CAFSoundDistribution fadeDisabled];
-[CAFSoundDistribution fadeHidden];
-[CAFSoundDistribution fadeRange];
-[CAFSoundDistribution _characteristicDidUpdate:fromGroupUpdate:];
-[CAFSoundDistribution balanceCharacteristic];
-[CAFSoundDistribution fadeCharacteristic];
```
