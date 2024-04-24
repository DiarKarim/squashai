using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MoveObj_UDP : MonoBehaviour
{
    void Start()
    {
        
    }

    void Update()
    {
        transform.position = new Vector3(UDPReceive_v1.eY,
                                         UDPReceive_v1.eZ,
                                         UDPReceive_v1.eX); 
    }
}
