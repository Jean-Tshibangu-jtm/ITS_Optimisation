
package veins;

import inet.node.inet.WirelessHost;

network VeinsScenario
{
    submodules:
        manager: Module {
            @display("i=block/network");
        }

        rsu[1]: WirelessHost {
            @display("p=100,100;i=block/wlan");
        }

        vehicle[10]: WirelessHost {
            @display("p=200,200;i=vehicle/car");
        }
}
