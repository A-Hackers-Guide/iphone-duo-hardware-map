# `BLSHEnvironmentDateSpecifier`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSEnvironmentDateSpecifying`
- 2 instance variables, 8 properties, 12 instance methods, 3 class methods

## Instance variables

```
@"BLSAlwaysOnDateSpecifier" _dateSpecifier;
@"<BLSHBacklightSceneHostEnvironment>" _environment;
```

## Properties

```
@property (T@"BLSAlwaysOnDateSpecifier",R,N,V_dateSpecifier) dateSpecifier;
@property (T@"<BLSHBacklightSceneHostEnvironment>",R,N,V_environment) environment;
@property (T@,R,N) userObject;
@property (T@"NSString",R,C,N) environmentIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSHEnvironmentDateSpecifier specifierWithPresentationDate:fidelity:environment:];
+[BLSHEnvironmentDateSpecifier specifierWithPresentationDate:fidelity:environment:userObject:];
+[BLSHEnvironmentDateSpecifier specifierWithPresentationDate:fidelity:environment:userObject:lowPowerRenderingPresentationTime:];
```

## Instance methods

```
-[BLSHEnvironmentDateSpecifier bls_loggingString];
-[BLSHEnvironmentDateSpecifier bls_shortLoggingString];
-[BLSHEnvironmentDateSpecifier environmentIdentifier];
-[BLSHEnvironmentDateSpecifier hash];
-[BLSHEnvironmentDateSpecifier description];
-[BLSHEnvironmentDateSpecifier isEqual:];
-[BLSHEnvironmentDateSpecifier lowPowerRenderingPresentationTime];
-[BLSHEnvironmentDateSpecifier environment];
-[BLSHEnvironmentDateSpecifier userObject];
-[BLSHEnvironmentDateSpecifier dateSpecifier];
-[BLSHEnvironmentDateSpecifier initWithPresentationDate:fidelity:environment:userObject:];
-[BLSHEnvironmentDateSpecifier initWithPresentationDate:fidelity:environment:userObject:lowPowerRenderingPresentationTime:];
```
