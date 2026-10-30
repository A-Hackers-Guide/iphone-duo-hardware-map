# `SymptomLinkAdvisoryAOPShim`

- Image: [`/System/Library/PrivateFrameworks/SymptomLinkAdvisoryAOPShim.framework/SymptomLinkAdvisoryAOPShim`](../userland/System__Library__PrivateFrameworks__SymptomLinkAdvisoryAOPShim.framework__SymptomLinkAdvisoryAOPShim.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 12 instance methods, 1 class methods

## Instance variables

```
^{_rpc_server_t=} _rpcServer;
^{tb_endpoint_s=(?=[96c]^v)} _forwardEndpoint;
{aluminium_aluminiumservice_s="connection"^{tb_connection_s}} _service;
B _serviceInitialized;
```

## Class methods

```
+[SymptomLinkAdvisoryAOPShim sharedInstance];
```

## Instance methods

```
-[SymptomLinkAdvisoryAOPShim initInternal];
-[SymptomLinkAdvisoryAOPShim dealloc];
-[SymptomLinkAdvisoryAOPShim connectWithError:];
-[SymptomLinkAdvisoryAOPShim teardown];
-[SymptomLinkAdvisoryAOPShim enableAutoLinkUpgradeWithError:];
-[SymptomLinkAdvisoryAOPShim disableAutoLinkUpgradeWithError:];
-[SymptomLinkAdvisoryAOPShim getTelemetryWithError:];
-[SymptomLinkAdvisoryAOPShim reportSnapshot:error:];
-[SymptomLinkAdvisoryAOPShim _convertInterfaceStats:toCStruct:];
-[SymptomLinkAdvisoryAOPShim _convertSnapshot:toCStruct:error:];
-[SymptomLinkAdvisoryAOPShim _hasRequiredEntitlement];
-[SymptomLinkAdvisoryAOPShim _setAutoLinkUpgradeEnabled:error:];
```
