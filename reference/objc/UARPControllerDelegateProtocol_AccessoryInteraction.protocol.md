# `UARPControllerDelegateProtocol` (protocol)

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 44 instance methods, 0 class methods

## Instance methods

```
-[UARPControllerDelegateProtocol sendMessageToAccessory:uarpMsg:error:];
-[UARPControllerDelegateProtocol accessoryTransportNeeded:isNeeded:];
-[UARPControllerDelegateProtocol assetAvailablityUpdateForAccessory:assetID:];
-[UARPControllerDelegateProtocol assetAvailablityUpdateForAccessoryID:assetID:];
-[UARPControllerDelegateProtocol assetSolicitationComplete:assetID:withStatus:];
-[UARPControllerDelegateProtocol assetSolicitationProgress:assetID:bytesReceived:bytesTotal:];
-[UARPControllerDelegateProtocol assetStagingPause:];
-[UARPControllerDelegateProtocol assetStagingResume:];
-[UARPControllerDelegateProtocol attestationCertificates:forSubjectKeyIdentifier:];
-[UARPControllerDelegateProtocol firmwareStagingComplete:assetID:withStatus:];
-[UARPControllerDelegateProtocol firmwareStagingProgress:assetID:bytesSent:bytesTotal:];
-[UARPControllerDelegateProtocol firmwareUpdateComplete:assetID:withStatus:];
-[UARPControllerDelegateProtocol firmwareUpdateProgress:assetID:bytesSent:bytesTotal:];
-[UARPControllerDelegateProtocol firmwareUpdateResult:vendorSpecificStatus:error:];
-[UARPControllerDelegateProtocol newUploader];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:appleModelNumber:error:];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:boardID:error:];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:chipID:error:];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:chipRevision:error:];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:ecid:error:];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:enableMixMatch:error:];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:epoch:error:];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:firmwareVersion:error:];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:friendlyName:error:];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:hardwareVersion:error:];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:hsmodelsDownloaded:error:];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:hsmodelsPreInstalled:error:];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:hwFusingType:error:];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:liveNonce:error:];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:manifestPrefix:error:];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:manufacturer:error:];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:modelName:error:];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:nonceHash:error:];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:nonceSeed:error:];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:productionMode:error:];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:securityDomain:error:];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:securityMode:error:];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:serialNumber:error:];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:stagedFirmwareVersion:error:];
-[UARPControllerDelegateProtocol queryCompleteForAccessory:stats:error:];
-[UARPControllerDelegateProtocol stagedFirmwareApplicationComplete:withStatus:];
-[UARPControllerDelegateProtocol stagedFirmwareRescindComplete:withStatus:];
-[UARPControllerDelegateProtocol supportedAccessories:forProductGroup:];
-[UARPControllerDelegateProtocol supportedAccessories:forProductGroup:isComplete:];
```
