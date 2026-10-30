# `BWExposureAnalyticsMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 25 instance variables, 0 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"NSString" _name;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _stateLock;
B _started;
I _numApertureBuckets;
^f _apertureBuckets;
^{?=qiIq} _apertureBucketDurations;
^Q _apertureBucketCounts;
{?="value"q"timescale"i"flags"I"epoch"q} _previousFrameDuration;
{?="value"q"timescale"i"flags"I"epoch"q} _previousFramePTS;
I _previousFrameAESignals;
i _previousFrameExposureMode;
f _previousFrameFNumber;
@"NSString" _previousFramePortType;
{?="value"q"timescale"i"flags"I"epoch"q} _totalDuration;
{?="value"q"timescale"i"flags"I"epoch"q} _fullAutoExposureDuration;
{?="value"q"timescale"i"flags"I"epoch"q} _aperturePriorityDuration;
{?="value"q"timescale"i"flags"I"epoch"q} _shutterPriorityDuration;
{?="value"q"timescale"i"flags"I"epoch"q} _aperturePlusShutterPriorityDuration;
{?="value"q"timescale"i"flags"I"epoch"q} _fullManualDuration;
Q _totalFrameCount;
Q _fullAutoFrameCount;
Q _aperturePriorityFrameCount;
Q _shutterPriorityFrameCount;
Q _aperturePlusShutterPriorityFrameCount;
Q _fullManualFrameCount;
```

## Class methods

```
+[BWExposureAnalyticsMonitor initialize];
```

## Instance methods

```
-[BWExposureAnalyticsMonitor _reset];
-[BWExposureAnalyticsMonitor dealloc];
-[BWExposureAnalyticsMonitor reset];
-[BWExposureAnalyticsMonitor stopMonitoring];
-[BWExposureAnalyticsMonitor totalDuration];
-[BWExposureAnalyticsMonitor variableApertureCameraBucketDurations];
-[BWExposureAnalyticsMonitor initWithName:];
-[BWExposureAnalyticsMonitor _updateDurationsAndFrameCountsForPTS:fNumber:AESignals:exposureMode:portType:];
-[BWExposureAnalyticsMonitor addMetadataFromSampleBuffer:];
-[BWExposureAnalyticsMonitor aperturePlusShutterPriorityModeDuration];
-[BWExposureAnalyticsMonitor aperturePriorityModeDuration];
-[BWExposureAnalyticsMonitor fullAutoExposureModeDuration];
-[BWExposureAnalyticsMonitor fullManualModeDuration];
-[BWExposureAnalyticsMonitor shutterPriorityModeDuration];
-[BWExposureAnalyticsMonitor startMonitoringWithApertureBuckets:];
-[BWExposureAnalyticsMonitor totalVariableApertureCameraDuration];
```
