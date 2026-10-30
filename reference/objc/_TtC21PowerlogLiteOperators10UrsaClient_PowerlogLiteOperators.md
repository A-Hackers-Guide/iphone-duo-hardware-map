# `_TtC21PowerlogLiteOperators10UrsaClient`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
_$sSo11CKContainerC container;
_$sSo13CKCodeServiceC codeService;
PowerlogLiteOperators.UrsaServiceAPIClient client;
_$sSS crKey;
_$sSS build;
_$sSS device;
_$sSS platformName;
Swift.Bool isBeta;
_$sScTyyt Swift.Never ? currentPeriodicTask;
_$sScTyyt Swift.Never ? currentAdmissionTask;
_$sScTyyt Swift.Never ? currentTelemetryTask;
```

## Instance methods

```
-[_TtC21PowerlogLiteOperators10UrsaClient init];
-[_TtC21PowerlogLiteOperators10UrsaClient cancel];
-[_TtC21PowerlogLiteOperators10UrsaClient shouldAdmitFor:impact:issueType:payload:flag:completionHandler:];
-[_TtC21PowerlogLiteOperators10UrsaClient getBuild];
-[_TtC21PowerlogLiteOperators10UrsaClient initClient:crKey:build:device:isiPad:isBeta:];
-[_TtC21PowerlogLiteOperators10UrsaClient periodicCheckSince:flag:completionHandler:];
-[_TtC21PowerlogLiteOperators10UrsaClient periodicCheckSince:tableUpdateEntries:flag:completionHandler:];
-[_TtC21PowerlogLiteOperators10UrsaClient reportPE:source:completionHandler:];
-[_TtC21PowerlogLiteOperators10UrsaClient reportTTR:completionHandler:];
-[_TtC21PowerlogLiteOperators10UrsaClient reportTelemetryEvent:payload:flag:completionHandler:];
-[_TtC21PowerlogLiteOperators10UrsaClient stressTest];
```
