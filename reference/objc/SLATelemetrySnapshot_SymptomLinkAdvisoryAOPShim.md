# `SLATelemetrySnapshot`

- Image: [`/System/Library/PrivateFrameworks/SymptomLinkAdvisoryAOPShim.framework/SymptomLinkAdvisoryAOPShim`](../userland/System__Library__PrivateFrameworks__SymptomLinkAdvisoryAOPShim.framework__SymptomLinkAdvisoryAOPShim.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 17 instance methods, 0 class methods

## Instance variables

```
I _periodDurationSec;
I _snapshotsProcessed;
I _recommendationChanges;
I _frictionEventsWiFi;
I _frictionEventsBT;
I _stallEventsWiFi;
I _stallEventsBT;
I _liveLinkAdvisories;
```

## Properties

```
@property (TI,N,V_periodDurationSec) periodDurationSec;
@property (TI,N,V_snapshotsProcessed) snapshotsProcessed;
@property (TI,N,V_recommendationChanges) recommendationChanges;
@property (TI,N,V_frictionEventsWiFi) frictionEventsWiFi;
@property (TI,N,V_frictionEventsBT) frictionEventsBT;
@property (TI,N,V_stallEventsWiFi) stallEventsWiFi;
@property (TI,N,V_stallEventsBT) stallEventsBT;
@property (TI,N,V_liveLinkAdvisories) liveLinkAdvisories;
```

## Instance methods

```
-[SLATelemetrySnapshot init];
-[SLATelemetrySnapshot stallEventsWiFi];
-[SLATelemetrySnapshot frictionEventsBT];
-[SLATelemetrySnapshot frictionEventsWiFi];
-[SLATelemetrySnapshot liveLinkAdvisories];
-[SLATelemetrySnapshot periodDurationSec];
-[SLATelemetrySnapshot recommendationChanges];
-[SLATelemetrySnapshot snapshotsProcessed];
-[SLATelemetrySnapshot stallEventsBT];
-[SLATelemetrySnapshot setFrictionEventsBT:];
-[SLATelemetrySnapshot setFrictionEventsWiFi:];
-[SLATelemetrySnapshot setLiveLinkAdvisories:];
-[SLATelemetrySnapshot setPeriodDurationSec:];
-[SLATelemetrySnapshot setRecommendationChanges:];
-[SLATelemetrySnapshot setSnapshotsProcessed:];
-[SLATelemetrySnapshot setStallEventsBT:];
-[SLATelemetrySnapshot setStallEventsWiFi:];
```
