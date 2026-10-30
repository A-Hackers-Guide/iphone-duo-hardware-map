# `SFAnalyticsSampler`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 3 properties, 12 instance methods, 0 class methods

## Instance variables

```
d _samplingInterval;
@"NSObject<OS_dispatch_source>" _timer;
@"NSString" _name;
@? _block;
i _notificationToken;
# _clientClass;
B _oncePerReport;
B _activeTimer;
```

## Properties

```
@property (Td,N,V_samplingInterval) samplingInterval;
@property (T@"NSString",R,N,V_name) name;
@property (TB,R,N,V_oncePerReport) oncePerReport;
```

## Instance methods

```
-[SFAnalyticsSampler newTimer];
-[SFAnalyticsSampler samplingInterval];
-[SFAnalyticsSampler dealloc];
-[SFAnalyticsSampler setSamplingInterval:];
-[SFAnalyticsSampler name];
-[SFAnalyticsSampler initWithName:interval:block:clientClass:];
-[SFAnalyticsSampler oncePerReport];
-[SFAnalyticsSampler pauseSampling];
-[SFAnalyticsSampler resumeSampling];
-[SFAnalyticsSampler sampleNow];
-[SFAnalyticsSampler setupOnceTimer];
-[SFAnalyticsSampler setupPeriodicTimer];
```
