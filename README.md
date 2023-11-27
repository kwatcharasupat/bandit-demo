# bandit-demo
<table class="dataframe" id="table-159">
  <thead>
    <tr style="text-align: center;">
      <th>Name</th>
      <th>Encoder</th>
      <th>Band</th>
      <th>Loss</th>
      <th>Mixture</th>
      <th>Speech</th>
      <th>Music</th>
      <th>Effects</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ground Truth</td>
      <td></td>
      <td></td>
      <td></td>
      <td><audio controls="controls"><source src=gt/159/mix.wav/></audio></td>
      <td><audio controls="controls"><source src=gt/159/speech.wav/></audio></td>
      <td><audio controls="controls"><source src=gt/159/music.wav/></audio></td>
      <td><audio controls="controls"><source src=gt/159/effects.wav/></audio></td>
    </tr>
    <tr>
      <td>BandIt</td>
      <td>Shared</td>
      <td>Music 64</td>
      <td>L1SNR</td>
      <td><audio controls="controls"><source src=gt/159/mix.wav/></audio></td>
      <td><audio controls="controls"><source src=dnr-3s-mus64-l1snr/159/speech.wav/></audio></td>
      <td><audio controls="controls"><source src=dnr-3s-mus64-l1snr/159/music.wav/></audio></td>
      <td><audio controls="controls"><source src=dnr-3s-mus64-l1snr/159/effects.wav/></audio></td>
    </tr>
    <tr>
      <td>BandIt</td>
      <td>Shared</td>
      <td>Vocals V7</td>
      <td>L2SNR</td>
      <td><audio controls="controls"><source src=gt/159/mix.wav/></audio></td>
      <td><audio controls="controls"><source src=dnr-3s-vox7-l2snr/159/speech.wav/></audio></td>
      <td><audio controls="controls"><source src=dnr-3s-vox7-l2snr/159/music.wav/></audio></td>
      <td><audio controls="controls"><source src=dnr-3s-vox7-l2snr/159/effects.wav/></audio></td>
    </tr>
    <tr>
      <td>BandIt</td>
      <td>Shared</td>
      <td>Vocals V7</td>
      <td>L1SNR</td>
      <td><audio controls="controls"><source src=gt/159/mix.wav/></audio></td>
      <td><audio controls="controls"><source src=dnr-3s-vox7-l1snr/159/speech.wav/></audio></td>
      <td><audio controls="controls"><source src=dnr-3s-vox7-l1snr/159/music.wav/></audio></td>
      <td><audio controls="controls"><source src=dnr-3s-vox7-l1snr/159/effects.wav/></audio></td>
    </tr>
    <tr>
      <td>BSRNN</td>
      <td>Separate</td>
      <td>Vocals V7</td>
      <td>L1</td>
      <td><audio controls="controls"><source src=gt/159/mix.wav/></audio></td>
      <td><audio controls="controls"><source src=dnr-bsrnn-lstm12-vox7-l1/159/speech.wav/></audio></td>
      <td><audio controls="controls"><source src=dnr-bsrnn-lstm12-vox7-l1/159/music.wav/></audio></td>
      <td><audio controls="controls"><source src=dnr-bsrnn-lstm12-vox7-l1/159/effects.wav/></audio></td>
    </tr>
  </tbody>
</table>
