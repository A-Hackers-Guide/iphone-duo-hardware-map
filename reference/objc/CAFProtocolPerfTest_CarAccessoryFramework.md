# `CAFProtocolPerfTest`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 16 properties, 30 instance methods, 3 class methods

## Properties

```
@property (T@"CAFInt32Characteristic",R,N) testInt32Characteristic;
@property (T@"CAFInt16Characteristic",R,N) testInt16Characteristic;
@property (T@"CAFUInt32Characteristic",R,N) testUInt32Characteristic;
@property (T@"CAFUInt16Characteristic",R,N) testUInt16Characteristic;
@property (T@"CAFStringCharacteristic",R,N) testStringCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) testString2Characteristic;
@property (Ti,R,N) testInt32;
@property (T@"CAFInt32Range",R,N) testInt32Range;
@property (Ts,N) testInt16;
@property (T@"CAFInt16Range",R,N) testInt16Range;
@property (TI,R,N) testUInt32;
@property (T@"CAFUInt32Range",R,N) testUInt32Range;
@property (TS,R,N) testUInt16;
@property (T@"CAFUInt16Range",R,N) testUInt16Range;
@property (T@"NSString",R,N) testString;
@property (T@"NSString",C,N) testString2;
```

## Class methods

```
+[CAFProtocolPerfTest serviceIdentifier];
+[CAFProtocolPerfTest indexBy];
+[CAFProtocolPerfTest observerProtocol];
```

## Instance methods

```
-[CAFProtocolPerfTest removeObserver:];
-[CAFProtocolPerfTest addObserver:];
-[CAFProtocolPerfTest registerObserver:];
-[CAFProtocolPerfTest name];
-[CAFProtocolPerfTest unregisterObserver:];
-[CAFProtocolPerfTest testString];
-[CAFProtocolPerfTest setTestString2:];
-[CAFProtocolPerfTest registeredForTestInt16];
-[CAFProtocolPerfTest registeredForTestInt32];
-[CAFProtocolPerfTest registeredForTestString];
-[CAFProtocolPerfTest registeredForTestString2];
-[CAFProtocolPerfTest registeredForTestUInt16];
-[CAFProtocolPerfTest registeredForTestUInt32];
-[CAFProtocolPerfTest setTestInt16:];
-[CAFProtocolPerfTest testInt16];
-[CAFProtocolPerfTest testInt32];
-[CAFProtocolPerfTest testString2];
-[CAFProtocolPerfTest testUInt16];
-[CAFProtocolPerfTest testUInt32];
-[CAFProtocolPerfTest testUInt16Range];
-[CAFProtocolPerfTest testUInt32Range];
-[CAFProtocolPerfTest _characteristicDidUpdate:fromGroupUpdate:];
-[CAFProtocolPerfTest testInt16Characteristic];
-[CAFProtocolPerfTest testInt16Range];
-[CAFProtocolPerfTest testInt32Characteristic];
-[CAFProtocolPerfTest testInt32Range];
-[CAFProtocolPerfTest testString2Characteristic];
-[CAFProtocolPerfTest testStringCharacteristic];
-[CAFProtocolPerfTest testUInt16Characteristic];
-[CAFProtocolPerfTest testUInt32Characteristic];
```
