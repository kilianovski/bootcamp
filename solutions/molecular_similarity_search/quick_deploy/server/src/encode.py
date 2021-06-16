from rdkit import DataStructs, Chem
from rdkit.Chem import AllChem
from src.config import VECTOR_DIMENSION

#Convert from smile to vector
def smiles_to_vector(smiles):
    mols = Chem.MolFromSmiles(smiles)
    fp = AllChem.GetMorganFingerprintAsBitVect(mols, 2, VECTOR_DIMENSION*8)
    hex_fp = DataStructs.BitVectToFPSText(fp)
    vec = list(bytes.fromhex(hex_fp))
    return vec